import streamlit as st

def home():
    # Creating a two-column layout
    col1, col2 = st.columns([2, 1])

    with col1:
        st.title("👋 Vishnu Priya K")
        st.write("📌 **Ex-Intern @ Edunet Foundation, YBI Foundation.**")  
        st.write("🎯 **Aspiring Data Science Student**")  

        st.header("🌟 Welcome to My Portfolio")
        st.markdown(
            """
            🚀 Explore my journey in **Data Science and AI**.  
            Here, you'll find details about:  
            - 🎓 **Education**  
            - 💼 **Internship Experience**  
            - 🏆 **Certifications**  
            - 📊 **Projects**  
            - 🛠️ **Skills & Tools**  
            - 📞 **How to Contact Me**  
            """
        )

    with col2:
        st.image("vishnu priya photo.png", caption="Vishnu Priya K", width=200)

# To run the function in a Streamlit app, call home() inside Streamlit's main logic.
if __name__ == "__main__":
    home()
