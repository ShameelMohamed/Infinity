import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Tenders", page_icon="🚢", layout="wide", initial_sidebar_state="collapsed")

# ✅ Background Styling
page_bg_css = """
<style>
    header { visibility: hidden; }
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

# ✅ Initialize Firebase (Only Once)
if not firebase_admin._apps:
    try:
        cred = credentials.Certificate(dict(st.secrets["firebase"]))
        firebase_admin.initialize_app(cred)
    except Exception as e:
        st.error(f"Firebase Initialization Error: {e}")

db = firestore.client()

# ✅ Session State for Authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ✅ Admin Login
st.title("🔒 Admin Panel")
password = st.text_input("Enter Password", type="password")

if st.button("Login") and not st.session_state.authenticated:
    if password == "admin123":
        st.session_state.authenticated = True
        st.rerun()  # Refresh UI to show content
    else:
        st.error("❌ Incorrect password. Try again!")

# ✅ Show Content Immediately After Authentication
if st.session_state.authenticated:
    st.success("✅ Access Granted!")

    # ✅ Show Static Page Content First
    st.subheader("📌 Grievances")
    grievances_container = st.empty()

    st.subheader("📌 Tender Bids")
    tender_bids_container = st.empty()

    st.subheader("📌 Ship Orders")
    ship_orders_container = st.empty()

    st.header("📊 Dashboard Overview")

    # ✅ Sample Data for Charts (Displays Instantly)
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

    # ✅ Display Charts
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
    fig3 = px.line(revenue_data, x='Month', y='Revenue', title="Monthly Revenue")
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

    # ✅ Fetch Firestore Data in Background (Displays Once Loaded)
    def fetch_and_display_data():
        try:
            grievances = db.collection("grievances").stream()
            grievances_data = [{"id": doc.id, **doc.to_dict()} for doc in grievances]
            grievances_df = pd.DataFrame(grievances_data)
            grievances_container.dataframe(grievances_df)

            tender_bids = db.collection("tender_bids").stream()
            tender_bids_data = [{"id": doc.id, **doc.to_dict()} for doc in tender_bids]
            tender_bids_df = pd.DataFrame(tender_bids_data)
            tender_bids_container.dataframe(tender_bids_df)

            ship_orders = db.collection("ship_orders").stream()
            ship_orders_data = [{"id": doc.id, **doc.to_dict()} for doc in ship_orders]
            ship_orders_df = pd.DataFrame(ship_orders_data)
            ship_orders_container.dataframe(ship_orders_df)

        except Exception as e:
            st.error(f"Error fetching Firestore data: {e}")

    fetch_and_display_data()
