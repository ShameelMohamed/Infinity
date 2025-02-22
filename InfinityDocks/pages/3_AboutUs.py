import streamlit as st

st.set_page_config(page_title="About Us", page_icon="☘️", layout="wide", initial_sidebar_state="collapsed")

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
    
    /* Increase font size */
    .title-text {{
        font-size: 32px !important;
        font-weight: bold;
    }}
    .content-text {{
        font-size: 20px !important;
        line-height: 1.6;
    }}
    .header-text {{
        font-size: 26px !important;
        font-weight: bold;
        margin-top: 20px;
    }}
</style>
"""
# Load the CSS into Streamlit
st.markdown(page_bg_css, unsafe_allow_html=True)

# Main container for About Us page
with st.container():
    st.markdown('<div class="title-text">☘️ About Us</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-text">- Hindustan Shipyard Limited (HSL), established in 1941, is strategically located on the eastern coast of the Indian subcontinent in Visakhapatnam, Andhra Pradesh. It is the nation\'s premier shipbuilding organization, catering to the needs of shipbuilding, ship repairs, submarine construction and refits, as well as the design and construction of complex and state-of-the-art offshore and onshore structures.</div>', unsafe_allow_html=True)
    
    # Vision Section
    st.markdown('<div class="header-text">Our Vision</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-text">- To be a global leader in shipyard services by integrating technology, sustainability, and craftsmanship.</div>', unsafe_allow_html=True)
    
    # Mission Section
    st.markdown('<div class="header-text">Our Mission</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-text">- To continuously innovate and improve financial performance in construction & repair of vessels within contractual time, cost and quality standards.</div>', unsafe_allow_html=True)
    
    # Core Values Section
    st.markdown('<div class="header-text">Our Core Values</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-text">- Excellence – We deliver superior craftsmanship and service quality.<br>- Innovation – We embrace technology to drive efficiency and growth.<br>- Integrity – We uphold transparency, ethics, and trust in all operations.<br>- Sustainability – We prioritize eco-friendly practices and responsible shipbuilding.<br>- Customer-Centricity – We build lasting relationships through responsive and efficient services.</div>', unsafe_allow_html=True)
    
    
    


# Get in Touch Section
st.header("Get in Touch")
st.markdown(
    """
    Feel free to reach out to us:

    📧 **Shameel Mohamed A**  
    [🔗 LinkedIn](https://www.linkedin.com/in/shameelmohamedx8)  
    shameelmohamed2005@gmail.com

    📧 **Farhan Hussain Z**  
    [🔗 LinkedIn](linkedin.com/in/farhan-hussain-309a642a3)  
    z.farhanhussain@gmail.com   


    Efficiency, Innovation, and Excellence at Every Dock."""
    )

# Footer (Optional)
st.write("---")
st.caption("Thank you for visiting! We’re committed to growing with you.")
