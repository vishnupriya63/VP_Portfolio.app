import streamlit as st
from Home import home
from Experience import experience
from Education import education
from Certification import certification
from Project import projects
from Skills import skills
from Contact import contact

# Set layout to wide and page title
st.set_page_config(layout="wide", page_title="Portfolio")

# Sidebar menu options
menu = [
    ("Home", "🏠"),
    ("Experience", "🏢"),
    ("Education", "🎓"),
    ("Certification", "📜"),
    ("Projects", "📂"),
    ("Skills & Tools", "🛠️"),
    ("Contact", "📞"),
]

# Sidebar navigation - always visible
with st.sidebar:
    selected = st.radio("Go to", [f"{icon} {name}" for name, icon in menu])

# Extract the text name (e.g., "Home") for routing
choice = selected.split(" ", 1)[1]

# Page routing
if choice == "Home":
    home()
elif choice == "Experience":
    experience()
elif choice == "Education":
    education()
elif choice == "Certification":
    certification()
elif choice == "Projects":
    projects()
elif choice == "Skills & Tools":
    skills()
elif choice == "Contact":
    contact()
