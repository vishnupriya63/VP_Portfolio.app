import streamlit as st

def experience():
    st.title("💼 Internship Experience")
    st.markdown("---")

    # Edunet Foundation Internship
    st.write("## Green AI Intern (Virtual) - Edunet Foundation")
    st.write("📅 **Duration**: April 2025 - May2025")
    st.write("📌 **Project**: Wind Power Generation Forecasting")
    st.markdown(
        """
        **🔹 Tasks:**  
        - 🧹  Cleaned missing values, handled outliers, scaled features, and engineered new ones. 
        - 🔍  Used GridSearchCV to optimize model performance.
        -  🔮 Planned real-time forecasting with live weather data for smart grid support.

        **🛠️ Tools Used:** Python, Google Colab, Power BI
        """
    )
    st.write("[View Certificate](https://drive.google.com/file/d/1Nx_VaNfcFhbNvu9VKVOD6ywdqTxtb9Ox/view?usp=drivesdk)")

    st.markdown("---")
    st.write("## 🤖 AI Internship (Virtual) - Edunet Foundation")
    st.write("📅 **Duration**: December 2024 - January 2025")
    st.write("📌 **Project**: Medical  Diagnosis ")
    st.markdown(
        """
        **🔹 Tasks:**  
        -  📊 Classifies diseases with probability scores (used for binary outcomes).
        -  🧠 Classifies patients into categories using optimal decision boundaries.
        -  🧑‍⚕️ Clinical Support: Aims to assist doctors with early and reliable diagnostic insights.

        **🛠️ Tools Used:** Python, Streamlit, Visual Studio Code, Power BI, MS Excel, MS Word
        """
    )
    st.write("[View Certificate](https://drive.google.com/file/d/1NsxQ6aLflrhGXukaTmhf4Lf42eIIdQQ5/view?usp=drivesdk)")

    st.markdown("---")
    st.write("## 📊 AIML Intern (Virtual) - YBI Foundation")
    st.write("📅 **Duration**: Jun2024 - July 2024")
    st.write("📌 **Project**: Mileage Prediction Regression")
    st.markdown(
        """
        **🔹 Tasks:**  
        - 🧹 Perform data preprocessing by handling missing values, scaling features, and encoding categorical variables.
        - 📊 Visualize data using plots like heatmaps and scatter plots to understand feature relationships.
        - 🔮 Build and evaluate a regression model to predict future car mileage (mpg) accurately.

        **🛠️ Tools Used:** Python , Visual Studio Code, Power BI, MS Excel   
        """
    )
    st.write("[View Certificate](https://drive.google.com/file/d/15R3WNOAZc9-2R7j8kxdv6VFLZC0M7JAt/view?usp=drivesdk)")

    st.markdown("---")

# To run the function in a Streamlit app, call experience() inside Streamlit's main logic.
if __name__ == "__main__":
    experience()
