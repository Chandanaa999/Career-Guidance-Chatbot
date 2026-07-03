import streamlit as st

st.set_page_config(page_title="Career Guidance Chatbot", page_icon="🎓", layout="centered")

st.title("🎓 Career Guidance Chatbot")
st.write("Welcome! Get career suggestions based on your interests and skills.")

name = st.text_input("Enter your Name")

education = st.selectbox(
    "Select your Education Level",
    ["10th Pass","12th Pass","Diploma","Engineering","Graduate"]
)

interest = st.selectbox(
    "Select Your Area of Interest",
    ["Programming","Web Development","Artificial Intelligence",
     "Data Science","Cyber Security","Networking",
     "Business Analytics","Graphic Design"]
)

if st.button("Get Career Suggestions"):
    if name:
        st.success(f"Hello, {name}! Based on your interest in {interest}, here are some career options:")

        careers = {
            "Programming": ["Software Developer","Backend Developer","Full Stack Developer","Application Developer"],
            "Web Development": ["Frontend Developer","Full Stack Developer","UI Developer","Web Designer"],
            "Artificial Intelligence": ["AI Engineer","Machine Learning Engineer","Deep Learning Engineer","AI Researcher"],
            "Data Science": ["Data Analyst","Data Scientist","Business Intelligence Analyst","Data Engineer"],
            "Cyber Security": ["Cyber Security Analyst","Ethical Hacker","Security Engineer","Information Security Specialist"],
            "Networking": ["Network Engineer","Cloud Engineer","System Administrator","Network Security Engineer"],
            "Business Analytics": ["Business Analyst","Data Analyst","Product Analyst","Operations Analyst"],
            "Graphic Design": ["Graphic Designer","UI/UX Designer","Product Designer","Creative Designer"]
        }

        for career in careers[interest]:
            st.write(f"✅ {career}")

        st.subheader("Recommended Skills")
        for skill in ["Communication Skills","Problem Solving","Programming Knowledge","Teamwork","Analytical Thinking"]:
            st.write(f"- {skill}")
    else:
        st.warning("Please enter your name.")
