import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Shipyard Home", layout="wide")

# Background CSS
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

# Footer with Contact Details
st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 10px;
            right: 30px;
            background-color: #1E1E1E;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 8px;
            box-shadow: 2px 2px 10px rgba(255, 255, 255, 0.2);
        }
    </style>
    <div class="footer">
        📍 Hindustan Shipyard, Vizag | 📞 Contact: +91 9876543210 | ✉ Email: support@shipyard.com
    </div>
""", unsafe_allow_html=True)

# Map of Hindustan Shipyard, Vizag
st.markdown("## 📍 Hindustan Shipyard, Vizag")

# Initialize map centered at Hindustan Shipyard
map = folium.Map(location=[17.6983, 83.2913], zoom_start=15)
folium.Marker([17.6983, 83.2913], popup="Hindustan Shipyard, Vizag", tooltip="Hindustan Shipyard").add_to(map)

# Display Map
st_folium(map, width=900, height=500)

# Shipyard Data Section
st.markdown("## 💀 Shipyard Insights & Operations")

# Random Shipyard Data
shipyard_data = {
    "Total Ships Built": 125,
    "Ships Under Construction": 8,
    "Ships Repaired This Year": 45,
    "Total Workforce": "5,200+ Employees",
    "Export Revenue (2024)": "$1.2 Billion",
    "Ongoing Defense Projects": 6
}

# Display Data as Key-Value Pairs
for key, value in shipyard_data.items():
    st.markdown(f"**{key}:** {value}")

# Display Recent Shipbuilding Projects (Dummy Table)
st.markdown("### ⚓ Recent Shipbuilding Projects")

ship_projects = pd.DataFrame({
    "Project Name": ["INS Vikrant", "Cargo Carrier X", "Naval Frigate Y", "Oil Tanker Z", "Luxury Yacht A"],
    "Completion Status": ["Completed", "Under Construction", "Under Construction", "Design Phase", "Completed"],
    "Expected Delivery": ["2023", "2025", "2026", "2027", "2023"]
})

st.table(ship_projects)

# Display Recent Repair Work (Dummy Table)
st.markdown("### 🛠 Recent Repair Work")
repair_data = pd.DataFrame({
    "Ship Name": ["Sea Explorer", "Ocean Guardian", "Titan Marine", "Hawk Carrier", "Blue Voyager"],
    "Repair Status": ["Completed", "In Progress", "Pending", "Completed", "In Progress"],
    "Issue": ["Engine Overhaul", "Hull Repair", "Navigation System Upgrade", "Deck Reinforcement", "Fuel System Repair"]
})

st.table(repair_data)

# Display Image at the Last
st.image("https://tse2.mm.bing.net/th?id=OIP.T_opll1SQqwYoouWp-ZXWQHaDS&pid=Api&P=0&h=180", use_column_width=True)
