import streamlit as st
import pandas as pd

# Set wide layout
st.set_page_config(layout="wide")

# Load data
@st.cache_data
def load_data(year=2025):
    df = pd.read_csv(f"Data/ccmt_{str(year)}_data.csv")
    return df

# df = load_data(year_choice=2025)

# --- Sidebar Filters ---
st.sidebar.header("🎯 Filter Options")

# 0. Year Type
year_choice = st.sidebar.radio(
    "Select Year Type",
    options=[2025, 2024, 2023, 2022, 2021],
    index=0
)

if year_choice != 2026:
    df = load_data(year_choice)  # Reload data for selected year

# Helper: Extract institute type
def get_institute_type(name):
    if not isinstance(name, str):
        return "OTHER"

    name = name.lower()

    if "indian institute of technology" in name:
        return "IIT"
    elif "indian institute of information technology" in name:
        return "IIIT"
    elif "national institute of technology" in name:
        return "NIT"
    else:
        return "OTHER"

df["Institute Type"] = df["Institute"].apply(get_institute_type)



# 1. Institute Type
institute_choice = st.sidebar.radio(
    "Select Institute Type",
    options=["ALL", "IIT", "NIT", "IIIT"],
    index=0
)

if institute_choice != "ALL":
    df = df[df["Institute Type"] == institute_choice]

# 2. PG Program filter
pg_programs = df["PG Program"].unique().tolist()
pg_selected = st.sidebar.multiselect(
    "Select PG Programs (optional)",
    options=pg_programs,
    default=[]  # Initially empty
)

# --- Special Filters ---
st.sidebar.markdown("### 🔍 Special Program Filters")

special_filter = st.sidebar.radio(
    "Quick Filter by Program Type",
    options=["None", "CS-programs", "AIML-programs"],
    index=0
)

# Apply special program filters if selected

cs_program_list = ['Computer Science & Engineering',
 'Computer Science and Engineering with Specialization in Data Science and Artificial Intelligence',
 'Computer Science',
 'Dual Degree M.Tech. - Ph.D in IT  with specialization in Machine Learning, Robotics and Human Computer Interaction Group',
 'Computer Science and Engineering with Specialization in Artificial Intelligence and Data Science',
 'Computer Science & Information Security',
 'Computer Integrated Manufacturing',
 'Computer Science & Engineering (Artificial Intelligence)',
 'Computer Science and  Engineering (Cyber Security)',
 'Computer Science & Technology',
 'Computer Aided Design Manufacture and Engineering',
 'M.Tech. IT with specialization in Machine Learning, Robotics and Human Computer Interaction Group',
 'Computer Engineering (Cyber Security)',
 'Computer Science & Engineering (Information Security)',
 'Computer Aided Design & Manufacturing',
 'Computer Networking',
 'Computer Engineering',
 'Computer Science & Engineering in (Artificial Intelligence & Data Science)',
 'Computer Science & Engineering (Analytics)']

aiml_program_list = [ 'Computer Science and Engineering with Specialization in Data Science and Artificial Intelligence',
 'Data Science',
 'M.Tech. IT  with specialization in Software and Data Engineering Group',
 'Artificial Intelligence',
 'Data Science & Engineering',
 'Dual Degree M.Tech. - Ph.D in IT  with specialization in Machine Learning, Robotics and Human Computer Interaction Group',
 'Computer Science and Engineering with Specialization in Artificial Intelligence and Data Science',
 'M.Tech in Artificial Intelligence',
 'M.Tech in Data Science',
 'Machine Learning and Computing',
 'M.Tech in Artificial Intelligence and Machine Learning',
 'Signal Processing and Machine Learning',
 'Data Analytics',
 'Artificial Intelligence & Data Science',
 'Computer Science & Engineering (Artificial Intelligence)',
 'Dual Degree M.Tech. - Ph.D  in IT with specialization in Software and Data Engineering Group',
 'Artificial Intelligence and Machine Learning',
 'M.Tech. IT with specialization in Machine Learning, Robotics and Human Computer Interaction Group',
 'Data Science and Engineering',
 'Computational and Data Science',
 'Industrial Engineering and Data Analytics',
 'Computer Science & Engineering in (Artificial Intelligence & Data Science)',
 'Machine Intelligence and Automation']


if special_filter == "CS-programs":
    df = df[df["PG Program"].isin(cs_program_list)]

elif special_filter == "AIML-programs":
    df = df[df["PG Program"].isin(aiml_program_list)]

# Apply user-selected PG Programs if any
if pg_selected:
    df = df[df["PG Program"].isin(pg_selected)]

# 3. Category filter
categories = sorted(
    df["Category"].dropna().astype(str).unique().tolist()
)
categories = ["All"] + categories

category_selected = st.sidebar.selectbox(
    "Select Category",
    options=categories
)

if category_selected != "All":
    df = df[df["Category"] == category_selected]


# 4. GATE Score input
user_gate_score = st.sidebar.number_input(
    "Enter your GATE score",
    min_value=0,
    value=1000,
    step=1
)

# Final filter by GATE score
df["Min GATE Score"] = pd.to_numeric(df["Min GATE Score"], errors="coerce")
df = df[df["Min GATE Score"] <= user_gate_score]

# --- Display Result ---
st.title("🎓 CCMT Program Finder")
st.markdown(
    """
Developed by Shivam.
[Contact](https://shivamgyardhna.github.io/Shivam_portfolioo/)
"""
)
# Data source note
st.markdown(
    """
    **ℹ️ Note:** This data is based on [CCMT Counselling 2025 official records](https://admissions.nic.in/CCMT/Applicant/Report/orcrreport.aspx?enc=Nm7QwHILXclJQSv2YVS+7oyfr3QTMnD485kebzU4RQjHPShCZV1JNhAqXFSs1WVi).
    """
)

st.markdown(f"### Showing {len(df)} matching programs")
st.dataframe(df.reset_index(drop=True), use_container_width=True)