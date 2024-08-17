import streamlit as st

# Configure the page
st.set_page_config(
    page_title="My Portfolio",
    page_icon=":briefcase:",
    layout="wide",
)

# Load company logo
# logo_url = "C:/Users/odend/OneDrive/Desktop/github/candidature/jane street"
# st.sidebar.image(logo_url, use_column_width=True)

# Add navigation options
st.sidebar.title("Navigation")
pages = ["Home", "About Me", "Resume", "Contact"]
page = st.sidebar.radio("Go to", pages)

# Home Page - Fit Questions
if page == "Home":
    st.title("Welcome to My Portfolio")
    st.subheader("Common Fit Questions")

    st.markdown("""
    ### Why should we hire you?
    I'm a highly motivated and results-oriented individual with a strong background in [Your Field]. My experiences in [Relevant Experiences] make me an ideal fit for this role.

    ### What are your strengths?
    My key strengths include [List of Strengths], which have helped me achieve [Relevant Achievements].

    ### What are your weaknesses?
    While I strive for perfection, I have learned to balance this with the understanding that some projects require a practical approach to deadlines and available resources.
    """)

# About Me Page - Additional Info
elif page == "About Me":
    st.title("About Me")
    st.write("Here you can provide a brief introduction about yourself, your background, and your interests.")

# Resume Page
elif page == "Resume":
    st.title("My Resume")
    
    # Embed PDF of your resume
    resume_url = "https://your-resume-url.com/resume.pdf"  # Replace with your resume URL or path
    st.markdown(f"[Click here to view my resume]({resume_url})", unsafe_allow_html=True)

# Contact Page - Links to GitHub and LinkedIn
elif page == "Contact":
    st.title("Contact Me")
    st.write("Feel free to reach out to me through the following channels:")

    # Links to GitHub and LinkedIn
    st.markdown("[GitHub](https://github.com/your-username)")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/your-username/)")

# Footer
st.sidebar.write("---")
st.sidebar.write("© 2024 My Portfolio")
