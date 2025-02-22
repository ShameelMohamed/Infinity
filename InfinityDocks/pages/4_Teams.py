import streamlit as st

st.set_page_config(page_title="Teams", page_icon="", layout="wide", initial_sidebar_state="collapsed")

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
# Load the CSS into Streamlit
st.markdown(page_bg_css, unsafe_allow_html=True)
st.title(" Teams ")
# Sample data for team members
team_members = [
    {"role": "President", "name": "Rajesh Sharma", "bio": "As the President of this shipyard, I bring 25 years of experience in shipbuilding and innovation. My focus is on efficiency, safety, and cutting-edge design, ensuring we meet global standards while fostering teamwork and excellence.", "image": "https://i.imgur.com/IXXjd0t.jpeg"},
    
    {"role": "Head Officer", "name": "Priya Iyer", "bio": "Expert in shipbuilding operations.", "image": "https://i.imgur.com/MJCVu22.jpeg"},
    {"role": "Head Officer", "name": "Amit Patel", "bio": "Specialist in shipyard logistics.", "image": "https://i.imgur.com/tLKaaCz.jpeg"},
    {"role": "Head Officer", "name": "Neha Verma", "bio": "Ensuring quality and safety standards.", "image": "https://i.imgur.com/VehQcEe.jpeg"},
    
    {"role": "Manager", "name": "Vikram Reddy", "bio": "Managing daily shipyard activities.", "image": "https://i.imgur.com/cGLyiRP.jpeg"},
    {"role": "Manager", "name": "Anjali Desai", "bio": "Overseeing supply chain and procurement.", "image": "https://i.imgur.com/rAqAbMw.jpeg "},
    {"role": "Manager", "name": "Rohit Nair", "bio": "Leading shipyard workforce operations.", "image": "https://i.imgur.com/dTnePHP.jpeg"},
    
    {"role": "Supervisor", "name": "Kavita Joshi", "bio": "Supervising dock operations.", "image": "https://i.imgur.com/RXqwhDF.jpeg"},
    {"role": "Supervisor", "name": "Arun Mehta", "bio": "Ensuring smooth repair workflows.", "image": "https://i.imgur.com/Ba9Wd1J.jpeg"},
    {"role": "Supervisor", "name": "Sneha Kapoor", "bio": "Managing safety and compliance.", "image": "https://i.imgur.com/GeVCODw.jpeg"},
    {"role": "Supervisor", "name": "Manoj Bhatia", "bio": "Coordinating ship maintenance.", "image": "https://i.imgur.com/1aMbOlg.jpeg"},
    {"role": "Supervisor", "name": "Pooja Agarwal", "bio": "Overseeing shipyard logistics.", "image": "https://i.imgur.com/7eqV9wp.jpeg"},
    {"role": "Supervisor", "name": "Sandeep", "bio": "Ensuring deadlines are met.", "image": "https://i.imgur.com/9aSzXg3.jpeg"},
    
    {"role": "Lead Engineer", "name": "Rakesh Gupta", "bio": "Expert in ship structures.", "image": "https://i.imgur.com/JRouHAK.jpeg"},
    {"role": "Lead Engineer", "name": "Divya Menon", "bio": "Leads propulsion innovations.", "image": "https://i.imgur.com/tpWFj5C.jpeg"},
    {"role": "Lead Engineer", "name": "Kunal Saxena", "bio": "Marine electronics specialist.", "image": "https://i.imgur.com/jHRnt1R.jpeg"},
    {"role": "Lead Engineer", "name": "Swati Choudhary", "bio": "Ensures structural integrity.", "image": "https://i.imgur.com/ONcSNoa.jpeg"},
    {"role": "Lead Engineer", "name": "Harish Kulkarni", "bio": "Develops eco-friendly ships.", "image": "https://i.imgur.com/yT36kOu.jpeg"},
    {"role": "Lead Engineer", "name": "Meera Gopal", "bio": "Enhances hull designs.", "image": "https://i.imgur.com/dXv8Mz9.jpeg"},
    {"role": "Lead Engineer", "name": "Nikhil", "bio": "Automation and controls expert.", "image": "https://i.imgur.com/MpVbmP5.jpeg"},
    {"role": "Lead Engineer", "name": "Aisha Khan", "bio": "Optimizes ship engines.", "image": "https://i.imgur.com/sbtqTbN.jpeg"},
]

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

# Function to display team members in structured columns
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

# Display each role in structured rows and columns
display_team_section("President", "President", 1)
display_team_section("Head Officers", "Head Officer", 3)
display_team_section("Managers", "Manager", 3)
display_team_section("Supervisors", "Supervisor", 3)
display_team_section("Lead Engineers", "Lead Engineer", 3)
