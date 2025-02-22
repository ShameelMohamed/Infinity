import streamlit as st
import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore

# Set page title
st.set_page_config(page_title="Services & Products", page_icon="🚢", layout="wide", initial_sidebar_state="collapsed")

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
    
    /* Style the table */
    table {{
        width: 100%;
        border-collapse: collapse;
        border: 2px solid #333;
        font-size: 18px;  /* Increase font size */
    }}
    
    th {{
        background-color: #222;
        color: white;
        font-weight: bold;
        padding: 10px;
        border: 2px solid #333;
        font-size: 20px;
    }}
    
    td {{
        padding: 10px;
        border: 2px solid #333;
        font-size: 18px;
    }}
</style>
"""
st.markdown(page_bg_css, unsafe_allow_html=True)

# Page Header
st.title("🚢 Services & Products")

# Buttons for different services
col1, col2, col3, col4, col5 = st.columns(5)

show_facilities = False  # Flag to track if Facilities should be displayed
show_financials = False
show_marineengineering = False
show_shipbuilding = False
show_shiprepair=False
with col1:
    if st.button("Ship Building", use_container_width=True):
        show_shipbuilding = True

with col2:
    if st.button("Ship Repair", use_container_width=True):
        show_shiprepair=True

with col3:
    if st.button("Marine Engineering", use_container_width=True):
        show_marineengineering = True

with col4:
    if st.button("Financials", use_container_width=True):
        show_financials = True

with col5:
    if st.button("Facilities", use_container_width=True):
        show_facilities = True

# Display Ship Building Division details and Facilities Table if the button was clicked
if show_facilities:

    st.title("Facilities")
    st.subheader("⚓ Ship Building Division")
    
    st.markdown("""
    **"Built 220 Quality Ships & Offshore platforms comprising Defence, Maritime, and Oil Sectors."**  
    HSL’s yard is spread over an area of about **300,000 Sq.Mtrs.** Workshops and facilities are systematically planned  
    and functionally laid out to ensure unidirectional flow of material.  

    The steel processing facilities consist of:  
    - A stockyard to hold **30,000 tons** of steel  
    - Modern **plate and section treatment plant**  
    - **NC gas cutting machines** and **heavy-duty presses**  
    - **Self-elevating trucks** capable of handling blocks up to **250 tonnes**  
    - Large **prefabrication shops** with **overhead travelling cranes**  

    The **Hull Construction Facilities** include a **modern Covered Building Dock** and **three Slipways**.  
    Cutting, Welding, and Assembly of steel to any specification is handled with care and accuracy  
    by skilled operators who undergo continuous training.  

    The **long Outfitting Quay** is equipped with **self-contained services and facilities**.  
    **Versatile machinery** and **labour-saving devices** in Hull Outfitting, Engineering, and Electrical shops  
    help minimize outfitting cycle time.
    """)

    st.subheader(" Shipyard Facilities")

    # Data for facilities
    data = {
        "S.No": [1, 2, 3, 4, 5, 6, 7, 8],
        "Facility": [
            "Covered Building Dock", "Slipway 2", "Wet Basin South", "Slipway 4",
            "Outfitting Quay", "Wet Basin North", "Slipway 3", "Dry-dock"
        ],
        "Size (m)": [
            "240 x 53", "140 x 22.7", "226 x 10", "195 x 28",
            "460", "168 x 10", "195 x 28", "244 x 38"
        ],
        "Capacity (DWT)": [
            "80000", "Suitable for small crafts", "50000", "30000",
            "2 to 3 ships up to 50000", "30000", "30000", "70000"
        ],
        "Cranage": [
            "(150T EOT -2 100T LL-1)", "(100T&60T-1 Each)", "40T", "(Under augmentation)",
            "(120T &50T-1 Each-10T-2.5T-1)(Under augmentation)", "20T", "(Under augmentation)", "40T"
        ]
    }

    # Convert data to DataFrame
    df = pd.DataFrame(data)

    # Apply custom styles to the table
    styled_table = df.style.set_properties(**{
        'border': '2px solid black',
        'font-size': '18px'
    }).set_table_styles([
        {'selector': 'th', 'props': [('background-color', '#222'), ('color', 'white'), ('font-weight', 'bold'), ('border', '2px solid black'), ('font-size', '20px')]},
        {'selector': 'td', 'props': [('border', '2px solid black'), ('padding', '10px')]}
    ])

    # Display the styled table
    st.write(styled_table, unsafe_allow_html=True)

if show_financials:
    st.title("Annual Returns")
    # Define custom CSS for card styling and background image
    st.title("")
    background_css = """
    <style>
        /* Card Styles */
        .card {
            background-color: rgba(0, 0, 0, 0.65);
            width: 100%;
            border-radius: 20px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            transition: transform 0.1s, box-shadow 0.2s;
            cursor: pointer;
            text-align: center;
        }
        .card:hover {
            transform: translateY(-10px);
            box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.15);
        }
        .card img {
            width: 100%;
            height: 150px;
            object-fit: cover;
        }
        .card-title {
            font-size: 20px;
            font-weight: bold;
            margin: 10px 0;
            color: white;
        }
        .card-text {
            font-size: 14px;
            margin: 0 10px 10px;
            color: white;
        }
        .card-button {
            background-color: purple;
            color: white;
            text-decoration: none;
            padding: 10px 15px;
            border-radius: 5px;
            display: inline-block;
            margin-bottom: 15px;
            transition: background-color 0.1s;
        }
        .card-button:hover {
            background-color: purple;
        }
        
    </style>
    """

    # Inject the CSS into the page
    st.markdown(background_css, unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)

    
    with col1:
        st.markdown(
            """
            <div class="card" onclick="window.location.href='https://hslvizag.in/hsl-cms/media/AR_2022_23.pdf'">
                <div class="card-title">2022-23</div>
                <a class="card-button" href="https://hslvizag.in/hsl-cms/media/AR_2022_23.pdf" onclick="window.location.href='https://hslvizag.in/hsl-cms/media/AR_2022_23.pdf'; return false;">Explore</a>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="card" onclick="window.location.href='https://hslvizag.in/hsl-cms/media/AR%202021_22.pdf'">
                <div class="card-title">2021-22</div>
                <a class="card-button" href="https://hslvizag.in/hsl-cms/media/AR%202021_22.pdf" onclick="window.location.href='https://hslvizag.in/hsl-cms/media/AR%202021_22.pdf'; return false;">Explore</a>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """
            <div class="card" onclick="window.location.href='https://hslvizag.in/hsl-cms/media/AR%202020_21.pdf'">
                <div class="card-title">2020-21</div>
                <a class="card-button" href="https://hslvizag.in/hsl-cms/media/AR%202020_21.pdf" onclick="window.location.href='https://hslvizag.in/hsl-cms/media/AR%202020_21.pdf'; return false;">Explore</a>
            </div>
            """,
            unsafe_allow_html=True,
        )
if show_marineengineering:
    st.title("Marine Engineering Faculty and Trainers")
    # Custom CSS for styling
    st.markdown("""
        <style>
            .card {
                background: #ffffff;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                text-align: center;
                padding: 20px;
                margin: 10px;
                transition: 0.3s;
                min-height: 250px;
            }
            .card:hover {
                transform: scale(1.05);
            }
            .card img {
                width: 100px;
                height: 100px;
                border-radius: 50%;
                object-fit: cover;
                margin-bottom: 10px;
            }
            .card h3 {
                margin: 10px 0 5px;
                font-size: 18px;
                color: #2C3E50;
            }
            .card p {
                font-size: 14px;
                color: #555;
                min-height: 50px;
            }
            .section-title {
                font-size: 22px;
                font-weight: bold;
                margin-top: 30px;
                margin-bottom: 10px;
                text-align: center;
                border-bottom: 2px solid #ddd;
                padding-bottom: 5px;
            }
        </style>
    """, unsafe_allow_html=True)
    team_members = [
    {"role": "Chief Marine Engineer", "name": "Dr. Arvind Rao", "bio": "With over 30 years in marine engineering, I specialize in ship propulsion systems and fuel efficiency. My mission is to innovate and educate the next generation of marine engineers.", "image": "https://i.imgur.com/IXXjd0t.jpeg"},
    
    {"role": "Senior Faculty", "name": "Dr. Priya Nair", "bio": "Expert in naval architecture and hydrodynamics.", "image": "https://i.imgur.com/MJCVu22.jpeg"},
    {"role": "Senior Faculty", "name": "Prof. Amit Tandon", "bio": "Specialist in marine power systems.", "image": "https://i.imgur.com/tLKaaCz.jpeg"},
    {"role": "Senior Faculty", "name": "Dr. Neha Srinivasan", "bio": "Ensuring high safety and sustainability standards in ship engineering.", "image": "https://i.imgur.com/VehQcEe.jpeg"},
    
    {"role": "Trainer", "name": "Capt. Vikram Reddy", "bio": "Training cadets in marine operations and safety.", "image": "https://i.imgur.com/cGLyiRP.jpeg"},
    {"role": "Trainer", "name": "Anjali Desai", "bio": "Oversees training in marine equipment handling.", "image": "https://i.imgur.com/rAqAbMw.jpeg"},
    {"role": "Trainer", "name": "Rohit Nair", "bio": "Leads practical training in engine room operations.", "image": "https://i.imgur.com/dTnePHP.jpeg"},
    ]
    def display_team_section(title, role, num_columns):
        filtered_members = [member for member in team_members if member["role"] == role]
        if filtered_members:
            st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)
            cols = st.columns(num_columns)
            for index, member in enumerate(filtered_members):
                with cols[index % num_columns]:
                    st.markdown(f"""
                        <div class="card">
                            <img src="{member['image']}" alt="{member['name']}">
                            <h3>{member['name']}</h3>
                            <p><strong>{member['role']}</strong></p>
                            <p>{member['bio']}</p>
                        </div>
                    """, unsafe_allow_html=True)
    display_team_section("Chief Marine Engineer", "Chief Marine Engineer", 1)
    display_team_section("Senior Faculty", "Senior Faculty", 3)
    display_team_section("Trainers", "Trainer", 3)


if show_shipbuilding:
    st.markdown("""
        <style>
            .title {
                font-size: 32px;
                font-weight: bold;
                color: #FFFFFF;  /* Bright White */
                text-align: center;
                margin-bottom: 20px;
            }
            .subheader {
                font-size: 24px;
                font-weight: bold;
                color: #FFFFFF;  /* Bright White */
                margin-top: 20px;
                margin-bottom: 10px;
            }
            .content {
                font-size: 18px;
                color: #FFFFFF;  /* Bright White */
                line-height: 1.6;
            }
            .highlight {
                font-weight: bold;
                color: #FFD700;  /* Gold highlight for emphasis */
            }
            body {
                background-color: #1E1E1E;  /* Dark background for contrast */
            }
        </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown('<div class="title">🚢 Advanced Technologies in Shipbuilding</div>', unsafe_allow_html=True)

    # Subheader & Technologies
    st.markdown('<div class="subheader">⚙️ Computer-Aided Design & Manufacturing (CAD/CAM)</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Modern ships are designed using <span class="highlight">3D modeling and simulation</span> for precision and efficiency.</div>', unsafe_allow_html=True)

    st.markdown('<div class="subheader">🔧 Automated Welding & Robotics</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Shipyards employ <span class="highlight">robotic welding and automation</span> to enhance structural integrity and reduce build time.</div>', unsafe_allow_html=True)

    st.markdown('<div class="subheader">🌊 Hydrodynamic Simulation & Testing</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Advanced <span class="highlight">computational fluid dynamics (CFD)</span> simulations optimize hull performance and fuel efficiency.</div>', unsafe_allow_html=True)

    st.markdown('<div class="subheader">🔋 Green & Sustainable Technologies</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Adoption of <span class="highlight">LNG fuel, hybrid propulsion</span>, and <span class="highlight">zero-emission technologies</span> for eco-friendly operations.</div>', unsafe_allow_html=True)

    st.markdown('<div class="subheader">🛰️ Smart Navigation & IoT Integration</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Implementation of <span class="highlight">AI-driven navigation systems</span> and real-time monitoring for enhanced safety.</div>', unsafe_allow_html=True)
    st.title("")
    

    # Initialize Firestore (only once) - OUTSIDE THE CONDITIONAL BLOCK
    if not firebase_admin._apps:
        cred = credentials.Certificate("your_firebase_credentials.json")  # Replace with your actual path
        firebase_admin.initialize_app(cred)

    db = firestore.client()

    # Debugging: Check if show_shipbuilding is True
    st.write(f"show_shipbuilding: {show_shipbuilding}")

    
    st.title("")

    if "show_form" not in st.session_state:
            st.session_state.show_form = False

    if st.button("🛒 Order Now", use_container_width=True):
            st.session_state.show_form = True  # Show form when clicked

    # **Display the Order Form when Button is Clicked**
    if st.session_state.show_form:
        st.subheader("📜 Order Form")

        # Input fields
        amount = st.number_input("💰 Budget/Amount (in USD)", min_value=100000, step=50000)

        technology_options = ["Advanced Composite", "Aluminum Construction", "Steel Shipbuilding", "Hybrid Propulsion"]
        technology = st.selectbox("🛠 Preferred Shipbuilding Technology", technology_options)

        ship_types = ["Oil Tanker", "Cargo Ship", "Container Ship", "Fishing Vessel", "Naval Ship"]
        ship_type = st.selectbox("🚢 Ship Type", ship_types)

        # Submit button
        if st.button("📤 Submit Order", use_container_width=True):
            # Save order to Firestore
            order_data = {
                "amount": amount,
                "technology": technology,
                "ship_type": ship_type
            }
            db.collection("ship_orders").add(order_data)

            # Success message
            st.success("✅ Your order has been submitted successfully!")
        st.subheader("📝 Repair Complaint Form")

        # Input fields
        ship_model = st.text_input("🚢 Ship Model")
        year_of_manufacture = st.number_input("📅 Year of Manufacture", min_value=1950, max_value=2025, step=1)

        ship_types = ["Oil Tanker", "Cargo Ship", "Container Ship", "Fishing Vessel", "Naval Ship", "Cruise Ship"]
        ship_type = st.selectbox("🚢 Ship Type", ship_types)

        issue_description = st.text_area("⚠️ Describe the Issue")

        # Submit button
        if st.button("📤 Submit Complaint", use_container_width=True):
            # Save order to Firestore
            order_data = {
                "ship_model": ship_model,
                "year_of_manufacture": year_of_manufacture,
                "ship_type": ship_type,
                "issue_description": issue_description
            }
            db.collection("ship_repair_complaints").add(order_data)

            # Success message
            st.success("✅ Your order has been submitted successfully!")
if show_shiprepair:
    # Dummy data for ship repair status
    repair_data = [
        {"ship_model": "Titanic-X", "year": 2010, "type": "Oil Tanker", "status": "In Progress"},
        {"ship_model": "Voyager-22", "year": 2015, "type": "Cargo Ship", "status": "Completed"},
        {"ship_model": "Sea Hawk", "year": 2020, "type": "Fishing Vessel", "status": "Pending"},
        {"ship_model": "Ocean King", "year": 2018, "type": "Naval Ship", "status": "Awaiting Parts"},
        {"ship_model": "Marine Star", "year": 2012, "type": "Container Ship", "status": "Inspection Ongoing"},
        {"ship_model": "Neptune Wave", "year": 2016, "type": "Cruise Ship", "status": "Under Maintenance"},
    ]

    # Define colors based on status
    status_colors = {
        "In Progress": "#FFA500",   # Orange
        "Completed": "#4CAF50",     # Green
        "Pending": "#FF6347",       # Red
        "Awaiting Parts": "#FFD700", # Gold
        "Inspection Ongoing": "#1E90FF",  # Blue
        "Under Maintenance": "#8A2BE2",  # Purple
    }

    # Custom CSS for hover effect and equal spacing
    st.markdown("""
        <style>
            .card {
                padding: 20px;
                border-radius: 10px;
                background-color: #2E2E2E;
                color: white;
                font-size: 16px;
                text-align: center;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .card:hover {
                transform: scale(1.05);
                box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.3);
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center;'>🛠 Current Ship Repair Status</h2>", unsafe_allow_html=True)
        # Display cards in a grid layout (3 cards per row)
    for i in range(0, len(repair_data), 3):
        cols = st.columns(3)  # Creates 3 equal columns per row
        for j in range(3):
            if i + j < len(repair_data):  # Ensure no out-of-bounds error
                repair = repair_data[i + j]
                with cols[j]:
                    st.markdown(f"""
                        <div class="card">
                            <b>🚢 {repair['ship_model']}</b><br>
                            📅 {repair['year']}<br>
                            🛳 {repair['type']}<br>
                            <span style='color: {status_colors[repair["status"]]};'><b>🔧 {repair["status"]}</b></span>
                        </div>
                    """, unsafe_allow_html=True)