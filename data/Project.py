import streamlit as st

def projects():
    st.title("🚀 My Internship & Self Projects")
    st.markdown("---")
    st.write("Here are some of the projects I've worked on:")

    # Project 1: Wind Power Generation Forecasting
    st.subheader("🌬️ Project 1: Wind Power Generation Forecasting")
    st.write("📌 **Description**: Predicts the amount of electricity that will be produced by wind turbines based on weather data and turbine conditions.")
    st.write("🛠️ **Tools**: Python, Visual Studio Code, Excel, PowerBI ")
    st.markdown(
        """
        **🔹 Key Features:**  
        - 🌬️📊 Uses wind speed, direction, and atmospheric data for accurate short-term and long-term power forecasting.  
        - 🤖📈 Employs ML models like Linear Regression, Random Forest, and XGBoost for predictive accuracy.
        - 🧹⚙️ Performs data cleaning, scaling, and feature engineering to enhance model input quality. 
        """
    )
    st.write("[GitHub Repository](https://github.com/vishnupriya63/Wind-Power-Generation-Forecasting)")

    st.markdown("---")

    # Project 2:  Medical diagnosis
    st.subheader("🧬 Project 2:  Medical diagnosis")
    st.write("📌 **Description**: The process of identifying a disease or condition by analyzing a patient's symptoms, medical history, and test results.")
    st.write("🛠️ **Tools**: Python, Visual Studio Code, Excel, PowerBI, Streamlit")
    st.markdown(
        """
        **🔹 Key Features:**  
        - 📥 Gathers health records from medical datasets for analysis.  
        - 🧹 Removes errors, scales values, and prepares data for modeling.  
        - 📈 Measures performance using accuracy, precision, and recall. 
        """
    )
    st.write("[GitHub Repository](https://github.com/vishnupriya63/Medical-diagnosis)")

    st.markdown("---")

    # Project 3: Mileage Prediction-Regression Analysis
    st.subheader("🔮 Project 3: Mileage Prediction-Regression Analysis")
    st.write("📌 **Description**:  Mileage prediction regression analysis estimates a vehicle's fuel efficiency based on features like cylinders, weight, and horsepower.")
    st.write("🛠️ **Tools**: Python, Visual Studio Code, Excel, PowerBI")
    st.markdown(
        """
        **🔹 Key Features:**  
        - 🔢 Predicts mileage using numerical input features like horsepower, weight, and acceleration.  
        - 🔍 Identifies relationships between variables and fuel efficiency through data analysis and visualization.
        - 🛠️ Enhances prediction accuracy using preprocessing steps like normalization and feature encoding. 
        """
    )
    st.write("[GitHub Repository](https://github.com/vishnupriya63/Mileage-Prediction-Regression-analysis)")

    st.markdown("---")



# To run the function in a Streamlit app, call projects() inside Streamlit's main logic.
if __name__ == "__main__":
    projects()
