import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

st.set_page_config(page_title="Vigilance", page_icon="🚢", layout="wide", initial_sidebar_state="collapsed")

# Initialize Firebase Admin (Only once)
if not firebase_admin._apps:
    cred = credentials.Certificate("your_firebase_credentials.json")  # Replace with actual path
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Page Title
st.title("🚨 Vigilance ")

# Background GIF & Header Removal
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

# Initialize session state for button clicks
if "active_section" not in st.session_state:
    st.session_state.active_section = "None"

# Columns for buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Guidelines", use_container_width=True):
        st.session_state.active_section = "Guidelines"

with col2:
    if st.button("Grievances", use_container_width=True):
        st.session_state.active_section = "Grievances"

with col3:
    if st.button("FAQs", use_container_width=True):
        st.session_state.active_section = "FAQs"

# Display Guidelines
if st.session_state.active_section == "Guidelines":
    st.markdown("""
    ### 🛡️ Overview of the Vigilance Department
    The Vigilance Department plays a crucial role in ensuring **ethical practices** within the shipyard.
    Our mission is to promote **transparency, accountability, and integrity** while preventing unethical behavior.
    If you witness any **fraud, corruption, or misconduct**, report it immediately.
    """)

    st.markdown("""
    ### 📜 Vigilance Guidelines
    - **Integrity & Ethics**: Employees must adhere to the highest ethical standards.
    - **Prevention of Fraud**: Any suspicious activities should be reported without delay.
    - **Zero Tolerance for Corruption**: Bribery and corrupt practices are strictly prohibited.
    - **Confidentiality Assured**: All reports are handled with utmost confidentiality.
    - **Whistleblower Protection**: Employees reporting unethical behavior are safeguarded against retaliation.
    """)

    st.markdown("""
    ### 📞 Contact Vigilance Officers
    - **Chief Vigilance Officer**: Mr. John Doe  
      📧 Email: **cvo@shipyard.com**  
      📞 Phone: **+1 234 567 8900**

    - **Deputy Vigilance Officer**: Ms. Jane Smith  
      📧 Email: **dvo@shipyard.com**  
      📞 Phone: **+1 987 654 3210**

    🔹 *For anonymous complaints, use our secure reporting portal [here](#).* 
    """)

    st.success("⚠️ Remember: Ethical conduct is the foundation of a strong and transparent organization!")

# Display Grievance Reporting Form
if st.session_state.active_section == "Grievances":
    st.title("🚨 Report an Issue")

    # Store form state
    if "grievance_form" not in st.session_state:
        st.session_state.grievance_form = {
            "name": "",
            "complaint_type": "Fraudulent Activities",
            "description": ""
        }

    # Name (Optional)
    name = st.text_input("👤 Your Name (Optional)", value=st.session_state.grievance_form["name"])

    # Type of Complaint (Dropdown)
    complaint_types = ["Fraudulent Activities", "Corruption", "Safety Violations", "Harassment or Misconduct"]
    complaint_type = st.selectbox("⚠️ Type of Complaint", complaint_types, index=complaint_types.index(st.session_state.grievance_form["complaint_type"]))

    # Detailed Description
    description = st.text_area("📄 Detailed Description", height=150, value=st.session_state.grievance_form["description"])

    # Update session state with new inputs
    st.session_state.grievance_form["name"] = name
    st.session_state.grievance_form["complaint_type"] = complaint_type
    st.session_state.grievance_form["description"] = description

    # Submit Button
    if st.button("✅ Submit Report", use_container_width=True):
        if description.strip():
            # Prepare data
            complaint_data = {
                "name": name if name else "Anonymous",
                "complaint_type": complaint_type,
                "description": description,
                "status": "Pending"
            }

            # Upload to Firestore
            db.collection("grievances").add(complaint_data)

            # Clear form fields after submission
            st.session_state.grievance_form = {
                "name": "",
                "complaint_type": "Fraudulent Activities",
                "description": ""
            }

            # Success message
            st.success("✅ Your complaint has been submitted confidentially!")
        else:
            st.error("⚠️ Please provide a detailed description of the issue.")

# Display FAQs using expanders
if st.session_state.active_section == "FAQs":
    st.title("❓ Frequently Asked Questions (FAQs)")

    with st.expander("🔍 What is the role of the Vigilance Department?"):
        st.write("The Vigilance Department ensures ethical practices, transparency, and integrity within the shipyard. It investigates reports of misconduct, fraud, or corruption.")

    with st.expander("📢 How can I report unethical activities?"):
        st.write("You can report unethical activities through our **Grievance Reporting System**. Reports can be anonymous, and we ensure confidentiality.")

    with st.expander("⚖️ Will my identity be protected if I file a complaint?"):
        st.write("Yes, we follow strict confidentiality protocols. Your identity will remain anonymous unless you choose to disclose it.")

    with st.expander("🚨 What types of complaints can I file?"):
        st.write("You can report **fraud, corruption, safety violations, harassment, or other misconduct** through the grievance system.")

    with st.expander("📞 How can I contact the Vigilance Officer directly?"):
        st.write("You can reach out to the Chief Vigilance Officer at **cvo@shipyard.com** or **+1 234 567 8900**.")

    with st.expander("📅 How long does it take to resolve a grievance?"):
        st.write("The resolution time depends on the nature and complexity of the complaint. We aim to address all grievances as soon as possible.")

    with st.expander("🔎 What happens after I submit a grievance?"):
        st.write("Your complaint is reviewed by the vigilance team. If necessary, an investigation is initiated, and actions are taken accordingly.")

    with st.expander("🛡️ What protections are in place for whistleblowers?"):
        st.write("We have a **zero-retaliation policy**. Employees reporting ethical violations are protected from any form of retaliation.")
