import streamlit as st

def home():
    # Two-column layout (left: text, right: photo)
    col1, col2 = st.columns([3, 1])

    with col1:
        # Name and role
        st.markdown(
            "<h2 style='font-family:Georgia; color:#8B4513;'>👋 Hi, I'm Vishnu Priya K</h2>",  
            unsafe_allow_html=True
        )
        st.markdown(
            "<h3 style='font-family:Trebuchet MS; color:#000000; font-size:18px;'>📌 Ex-Intern @ Edunet Foundation | YBI Foundation</h3>",
            unsafe_allow_html=True
        )
        st.markdown(
            "<h4 style='color:#008080;'>🎯 Aspiring Data Scientist | Software Engineer</h4>",
            unsafe_allow_html=True
        )

        # Intro paragraph
        st.markdown(
            """
            <div style="font-size:17px; line-height:1.7; text-align:justify; margin-bottom:20px;">
            I am a passionate <b>Artificial Intelligence and Machine Learning student</b>, 
            with strong interest in both <b>Data Science</b> and <b>Software Engineering</b>.  
            Through internships, projects, and certifications, I am building skills to solve 
            real-world challenges and create impactful solutions.  
            </div>
            """,
            unsafe_allow_html=True
        )

        # Welcome Section
        st.subheader("🌟 Welcome to My Portfolio")
        st.markdown(
            """
            🚀 Explore my journey in **Data Science and Software Development**.  
            - 🎓 **Education**  
            - 💼 **Internship Experience**  
            - 🏆 **Certifications**  
            - 📊 **Projects**  
            - 🛠️ **Skills & Tools**  
            - 📞 **Contact Information**  
            """
        )

        # Aim Section
        st.markdown(
            """
            ### 🎯 My Aim
            My ultimate goal is to leverage <b>Data Science and Software Engineering</b>  
            to build innovative solutions that create impact in industries like  
            <i>Healthcare, Finance, and Technology</i>.  

            I aim to secure a role in a **good company with a good position** as a  
            <b>Software Engineer or Data Scientist</b>, where I can keep learning, innovating, and contributing.  
            """,
            unsafe_allow_html=True
        )

    with col2:
        # Right corner photo
        st.markdown("<div style='text-align:right; margin-top:10px;'>", unsafe_allow_html=True)
        st.image("vishnu priya photo.png", caption="👋 Vishnu Priya K", width=220)
        st.markdown("</div>", unsafe_allow_html=True)


# Run app
if __name__ == "__main__":
    home()
