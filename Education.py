import streamlit as st

def education():
    st.title("🎓 My Education")
    st.markdown("---")

    st.write("## Academic Background")
    
    st.markdown(
        """
        ### 🎓 **Bachelor of Technology in Artificial Intelligence & Machine Learning**  
        - 🏫 **Institution**: K Ramakrishnan College of Engineering  
        - 📅 **Duration**: 2022 - Present    
        
        ### 🏫 **12th Grade**  
        - 🏫 **Institution**: MPB Government Girls Hr. Sec. School
        - 📅 **Duration**: 2021 - 2022  

        ### 🏫 **10th Grade**  
        - 🏫 **Institution**: MPB Government Girls Hr. Sec. School
        - 📅 **Duration**: 2019 - 2020   
        """
    )

    st.markdown("---")

# To run the function in a Streamlit app, call education() inside Streamlit's main logic.
if __name__ == "__main__":
    education()
