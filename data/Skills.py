import streamlit as st

def skills():
    st.title("🚀 My Skills & Tools")
    st.markdown("---")

    # Define skills and tools with ratings (out of 5)
    technical_skills = {
        "Azure Cloud Foundation Basics": 3,
        "Data Analysis": 3,
        "Python": 3,
        "Java Basics": 2,
        "Data Visualization": 3,
        "Data Preprocessing": 3,
        "Excel": 2,
    }

    soft_skills = {
        "Public Speaking": 3,
        "Presentation Skills": 3,
        "Teamwork & Collaboration": 3,
        "Time Management": 5,
        "Adaptability": 4
    }

    tools = {
        "Visual Studio Code": 4,
        "Power BI": 3,
        "Google Colab & Jupyter Notebook": 4,
        "Azure Cloud": 3,
        "Microsoft Office (Excel, PPT, Word)": 3,
        "GitHub": 3
    }

    # Function to generate star rating
    def get_stars(rating, max_stars=5):
        full_star = "★"
        empty_star = "☆"
        return full_star * rating + empty_star * (max_stars - rating)

    # Layout with three columns
    col1, col2, col3 = st.columns(3)

    # Display Technical Skills
    with col1:
        st.subheader("💻 Technical Skills")
        for skill, rating in technical_skills.items():
            st.write(f"**{skill}**: {get_stars(rating)}")

    # Display Soft Skills
    with col2:
        st.subheader("🧠 Soft Skills")
        for skill, rating in soft_skills.items():
            st.write(f"**{skill}**: {get_stars(rating)}")

    # Display Tools
    with col3:
        st.subheader("🛠️ Tools & Platforms")
        for tool, rating in tools.items():
            st.write(f"**{tool}**: {get_stars(rating)}")

    st.markdown("---")

# To run in a Streamlit app, call skills() inside Streamlit's main logic
if __name__ == "__main__":
    skills()
