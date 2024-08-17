import streamlit as st

# Configure the page
st.set_page_config(
    page_title="My Jane Street Application",
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
    st.title("My Jane Street Application")

    st.markdown("""
    ### Why Jane Street?
    - Research Driven
    - Big on Technology
    - In-House Software Building

    ### How I heard about Jane Street?
    Wikipedia (https://en.wikipedia.org/wiki/OCaml)

    ### Why am I looking for a new position?
    I learned a lot during my summer internship at AFD but I believe that Jane Street's research and technology oriented culture would be a perfect fit for me.
    """)

# About Me Page - Additional Info
elif page == "About Me":
    st.title("About Me")
    st.write("Here you can provide a brief introduction about yourself, your background, and your interests.")

# Resume Page
elif page == "Resume":
    st.title("My Resume")
    
    # Embed PDF of your resume
    resume_url = "https://your-resume-url.com/resume.pdf"
    st.markdown(f"[Click here to view my resume]({resume_url})", unsafe_allow_html=True)

# Contact Page - Links to GitHub and LinkedIn
elif page == "Contact":
    st.title("Contact Me")
    st.write("Feel free to reach out to me through the following channels:")

    # Links to GitHub and LinkedIn
    st.markdown("[GitHub](https://github.com/coasensi)")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/charles-odend-hal/)")

# Footer
st.sidebar.write("---")
st.sidebar.write("© 2024 Charles")
