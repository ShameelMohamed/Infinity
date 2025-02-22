import streamlit as st

st.set_page_config(page_title="Contact Us", page_icon="", layout="wide", initial_sidebar_state="collapsed")

# Background GIF & Header Removal
page_bg_css = f"""
<style>
    /* Hide the app header */
    header {{
        visibility: hidden;
    }}
    .stApp {{
        background: url("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWx4ZWwyNTY0MTFhdXhmcHNlZHl6ajNubzhnbDVnemtwZHpzN2c3eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hFhygTRHt4jvGQo52q/giphy.gif");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }}
</style>
"""
st.markdown(page_bg_css, unsafe_allow_html=True)
st.title(" Important Contacts ")

# Styling for Cards (Including Hover Effect)
st.markdown(
    """
    <style>
        .card {
            background: #ffffff;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            margin: 10px;
            transition: transform 0.1s ease-in-out, box-shadow 0.1s ease-in-out;
        }
        .card:hover {
            transform: translateY(-10px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }
        .card h3 {
            color: #003366;
            margin-bottom: 10px;
        }
        .card p {
            margin: 5px 0;
            color: #555;
        }
        .card a {
            color: #007bff;
            text-decoration: none;
            font-weight: bold;
        }
        .card a:hover {
            text-decoration: underline;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Contact Information
contacts = [
    {"name": "Business Development", "email": "mprojectsdo@hslvizag.in", "phone": "+91 9493792680"},
    {"name": "C&MD Secretariat", "email": "cmdoffice@hslvizag.in", "phone": "+91 891 2577 404 / 437"},
    {"name": "Admin", "email": "sm.adm@hslvizag.in", "phone": "+91 9493792130"},
    {"name": "Company Secretary", "email": "cs@hslvizag.in", "phone": "+91 9493792639"},
    {"name": "Corporate Planning", "email": "agmcp@hslvizag.in", "phone": "+91 9493792639"},
    {"name": "Finance", "email": "mfinancetax@hslvizag.in", "phone": "+91 9493792806 / 2236"},
    {"name": "Material Management", "email": "smpurchase@hslvizag.in", "phone": "+91 9493792052"},
    {"name": "Outsourcing", "email": "mos@hslvizag.in", "phone": "+91 9493792216"},
    {"name": "Safety", "email": "dgmsafety@hslvizag.in", "phone": "+91 9493792488"},
    {"name": "Security & Fire", "email": "sm.secfs@hslvizag.in", "phone": "+91 9493792123"},
    {"name": "Ship Repairs (SRC)", "email": "dgmsrcom@hslvizag.in", "phone": "+91 9493792950"},
    {"name": "Submarine Repair", "email": "msubplb@hslvizag.in", "phone": "+91 9493792671 / 2519"},
    {"name": "Recruitment", "email": "recruitment@hslvizag.in", "phone": "+91 9493792969"},
    {"name": "Vigilance", "email": "vigilance@hslvizag.in", "phone": "+91 9493792004"},
    {"name": "Public Relations (PRO)", "email": "neelimab.k356@hslvizag.in", "phone": "+91 9493792230"},
    {"name": "Information Technology", "email": "webservices@hslvizag.in", "phone": "+91 9493792103"},
    {"name": "RTI & Disciplinary Actions", "email": "rti@hslvizag.in", "phone": "+91 9493792804"},
    
]

# Display Cards in a Grid Layout
cols_per_row = 3  # Number of cards per row

for i in range(0, len(contacts), cols_per_row):
    cols = st.columns(cols_per_row)
    for j in range(cols_per_row):
        if i + j < len(contacts):
            contact = contacts[i + j]
            with cols[j]:
                st.markdown(
                    f"""
                    <div class="card">
                        <h3>{contact["name"]}</h3>
                        <p>Email: <a href="mailto:{contact["email"]}">{contact["email"]}</a></p>
                        <p>Phone: {contact["phone"]}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
