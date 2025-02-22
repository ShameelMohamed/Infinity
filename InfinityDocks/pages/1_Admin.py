import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import plotly.express as px
st.set_page_config(page_title="Tenders", page_icon="🚢", layout="wide", initial_sidebar_state="collapsed")


page_bg_css = """
<style>
    /* Hide the app header */
    header {
        visibility: hidden;
    }
    .stApp {
        background: url("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWx4ZWwyNTY0MTFhdXhmcHNlZHl6ajNubzhnbDVnemtwZHpzN2c3eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hFhygTRHt4jvGQo52q/giphy.gif");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }
</style>
"""
st.markdown(page_bg_css, unsafe_allow_html=True)


# Initialize Firebase if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate("st.secrets["firebase"]")  # Replace with your actual path
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Session state for authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Admin authentication
st.title("🔒 Admin Panel")
password = st.text_input("Enter Password", type="password")

if st.button("Login"):
    if password == "admin123":
        st.session_state.authenticated = True
    else:
        st.error("Incorrect password. Try again!")

if st.session_state.authenticated:
    st.success("✅ Access Granted!")

    # Fetching Firebase Data
    def fetch_collection(collection_name):
        try:
            docs = db.collection(collection_name).stream()
            data = [{"id": doc.id, **doc.to_dict()} for doc in docs]
            return pd.DataFrame(data)
        except Exception as e:
            st.error(f"Error fetching {collection_name}: {e}")
            return pd.DataFrame()

    grievances_df = fetch_collection("grievances")
    tender_bids_df = fetch_collection("tender_bids")
    ship_orders_df = fetch_collection("ship_orders")

    # Display Firebase Collections
    st.subheader("📌 Grievances")
    st.dataframe(grievances_df)

    st.subheader("📌 Tender Bids")
    st.dataframe(tender_bids_df)

    st.subheader("📌 Ship Orders")
    st.dataframe(ship_orders_df)

    # Dashboard Section
    st.header("📊 Dashboard Overview")
    
    # Dummy Data for Charts
    shipment_status = pd.DataFrame({
        "Status": ["Completed", "In-Transit", "Delayed"],
        "Count": [50, 30, 10]
    })
    stock_summary = pd.DataFrame({
        "Item": ["Steel", "Paint", "Oil", "Spare Parts"],
        "Stock": [100, 50, 20, 80]
    })
    revenue_data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Revenue": [50000, 60000, 70000, 65000, 80000]
    })

    # Charts
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📦 Total Shipments")
        fig1 = px.pie(shipment_status, values='Count', names='Status', title='Shipment Status')
        st.plotly_chart(fig1)
    
    with col2:
        st.subheader("📊 Stock Summary")
        fig2 = px.bar(stock_summary, x='Item', y='Stock', title='Stock Levels')
        st.plotly_chart(fig2)
    
    st.subheader("💰 Revenue & Financial Reports")
    fig3 = px.line(revenue_data, x='Month', y='Revenue', title='Monthly Revenue')
    st.plotly_chart(fig3)

    st.subheader("📝 Recent Export Requests")
    export_requests = pd.DataFrame({
        "Order ID": [101, 102, 103],
        "Status": ["Pending", "Shipped", "Delivered"]
    })
    st.dataframe(export_requests)

    st.subheader("👤 User Activities")
    user_logs = pd.DataFrame({
        "User": ["Alice", "Bob", "Charlie"],
        "Activity": ["Submitted Tender", "Checked Ship Status", "Uploaded Document"]
    })
    st.dataframe(user_logs)
else:
    st.warning("Please enter the correct password to access the admin panel.")
