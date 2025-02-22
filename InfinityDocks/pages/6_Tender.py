import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

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

# ✅ Initialize Firebase Firestore only ONCE
if not firebase_admin._apps:
    cred = credentials.Certificate("your_firebase_credentials.json")  # Replace with your actual path
    firebase_admin.initialize_app(cred)

db = firestore.client()  # Firestore Database

# ✅ Initialize session state for form visibility
if "show_tender_form" not in st.session_state:
    st.session_state.show_tender_form = False

# ✅ Functions to handle form visibility
def show_apply_form():
    st.session_state.show_tender_form = True

# 🎯 **Tender Page Header**
st.markdown("<h1 style='text-align: center;'>📜 Shipyard Tenders</h1>", unsafe_allow_html=True)

# 🔍 **Open Tenders Section**
st.markdown("### 🔹 Open Tenders")

# 📝 Dummy Data for Open Tenders
tender_data = pd.DataFrame({
    "Tender Name": ["Hull Inspection", "Engine Overhaul", "Deck Refinishing", "Safety Equipment Upgrade", "Navigation System Update"],
    "Description": ["Inspection of hull integrity", "Complete engine service", "Repaint & restore deck", "Upgrade to latest safety standards", "Install modern GPS & radar"],
    "Deadline": ["2025-03-15", "2025-04-10", "2025-05-01", "2025-06-20", "2025-07-30"],
    "Bid Range ($)": ["50K - 100K", "200K - 500K", "75K - 150K", "100K - 300K", "150K - 400K"]
})

# 📋 **Display Open Tenders Table**
st.table(tender_data)

# 🎯 **Apply for Tender Button**
st.markdown("### 🏆 Apply for a Tender")
st.button("✍️ Apply Now", on_click=show_apply_form, use_container_width=True)

# 📝 **Tender Application Form**
if st.session_state.show_tender_form:
    st.markdown("### 📩 Submit Your Bid")

    # 🔹 Form Inputs
    company_name = st.text_input("🏢 Company / Individual Name")
    contact = st.text_input("📞 Contact Details")
    bid_amount = st.number_input("💰 Bid Amount ($)", min_value=5000, step=5000)

    # **Submit Button**
    if st.button("📤 Submit Bid", use_container_width=True):
        if company_name and contact and bid_amount:
            bid_data = {
                "company_name": company_name,
                "contact": contact,
                "bid_amount": bid_amount
            }

            try:
                db.collection("tender_bids").add(bid_data)
                st.success("✅ Bid submitted successfully! We will review your application.")
                
                # Hide form after submission
                st.session_state.show_tender_form = False
            except Exception as e:
                st.error(f"❌ Error submitting bid: {e}")
        else:
            st.warning("⚠️ Please fill in all required fields.")
