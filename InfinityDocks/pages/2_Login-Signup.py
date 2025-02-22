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


# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate(dict(st.secrets["firebase"]))
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login_page():
    st.title("Login & Signup Page")
    option = st.radio("Choose an option:", ["Login", "Sign Up"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = ""
    
    if option == "Sign Up":
        confirm_password = st.text_input("Confirm Password", type="password")
    
    if st.button("Submit"):
        if option == "Sign Up" and password != confirm_password:
            st.error("Passwords do not match")
        else:
            users_ref = db.collection("credentials")
            if option == "Sign Up":
                users_ref.add({"email": email, "password": password})
                st.success("Signup Successful! Please login.")
            else:
                docs = users_ref.where("email", "==", email).where("password", "==", password).stream()
                if any(docs):
                    st.session_state.logged_in = True
                    st.success("Login Successful!")
                    st.title("Inventory Management System")
    
                    # View Available Stock
                    st.header("📦 Available Stock")
                    warehouse = st.selectbox("Select Warehouse", ["Main Dock", "Storage Yard", "Offshore Site"])
                    stock_type = st.selectbox("Stock Type", ["Machinery", "Spare Parts", "Raw Materials"])
                    
                    availability = st.selectbox("Availability", ["In Stock", "Low Stock", "Out of Stock"])
                    
                    stock_data = pd.DataFrame({
                        "Warehouse": ["Main Dock", "Storage Yard", "Offshore Site"],
                        "Stock Type": ["Machinery", "Spare Parts", "Raw Materials"],
                        "Stock Name": ["Engine", "Propeller", "Steel Sheets"],
                        "Availability": ["In Stock", "Low Stock", "Out of Stock"],
                    })
                    st.table(stock_data)
                    
                    # Stock History & Reports
                    st.header("📊 Stock Movement Trends")
                    stock_movement = pd.DataFrame({
                        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
                        "Stock In": [500, 600, 550, 700, 650],
                        "Stock Out": [300, 400, 350, 450, 500]
                    })
                    fig = px.line(stock_movement, x="Month", y=["Stock In", "Stock Out"], markers=True)
                    st.plotly_chart(fig)
                    
                    # Communication & Support
                    st.header("📞 Communication & Support")
                    st.markdown("**Mail with Shipyard Support**: support@shipyard.com")
                    st.markdown("**Forum & Discussion Board**: [Visit Forum](#)")
                    st.markdown("**Request a Callback**: [Click Here](#)")

                else:
                    st.error("Invalid Credentials")

if not st.session_state.logged_in:
    login_page()

    
