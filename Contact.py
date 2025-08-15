
import streamlit as st

def contact():
    st.title("📞 Contact Me")
    st.markdown("---")

    st.write("### How to Reach Me:")
    st.markdown(
        """
         - 📧 Email: [My Mail ID](mailto:vishnupriyaanjalai2004@gmail.com)     
         - 💼 LinkedIn: [My LinkedIn Profile](https://www.linkedin.com/in/vishnupriya72/)     
         - 🖥️ GitHub: [My Repository](https://github.com/vishnupriya63)  
        """
    )
        # Resume download button
    with open("Vishnu Priya Resume.pdf", "rb") as resume_file:
        st.download_button(
            label="Download Resume",
            data=resume_file,
            file_name="Vishnu Priya Resume.pdf",
            mime="application/pdf"
            )
if __name__ == "__main__":
    contact()