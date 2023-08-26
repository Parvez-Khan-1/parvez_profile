from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "photo.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Parvez Khan | ML Engineer"
PAGE_ICON = ":wave:"
NAME = "Parvez Khan"
DESCRIPTION = """
Lead Machine Learning Engineer Specializing in Scalable ML/NLP System Development.
"""
EMAIL = "ParvezPathan09@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/parvezkhan-pathan-389065105/",
    "GitHub": "https://github.com/Parvez-Khan-1",
    "StackOverflow": "https://stackoverflow.com/users/5536013/parvez-khan",
}

PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns([1, 3])
with col1:
    st.image(profile_pic, width=150)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Executive Summary")
st.write(
    """
- ✔️ Lead Machine Learning Engineer with over 7+ years of experience in NLP and Machine Learning.
- ✔️ Specializes in transforming concepts into customer-ready products by productionizing ideas.
- ✔️ Enthusiastic about re-engineering processes using advanced NLP, ML, and Deep Learning techniques.
- ✔️ Demonstrates strong proficiency in developing SDKs and APIs for Data Scientist Workbenches.
"""
)

# # --- SKILLS ---
# st.write('\n')
# st.subheader("Key Skills")
# st.write(
#     """
# - 👩‍💻 Programming Languages: Python & R
# - ☀ Python Frameworks: Flask, FastAPI, Streamlit, Plotly, Locust
# - 🚀 ML/DL Frameworks and Tool: H2O.ai, H2O Driverless AI, XGBoost, Tensorflow, Pytorch, Keras
# - 📊 Data Visualization: Plotly, Dash, Kibana, Matplotlib, Seaborn
# - 📚 Machine Learning: Regression Analysis, Classification, Clustering, Dimensionality Reduction, Evaluation Techniques, Optimization Techniques.
# - 🧠 Deep Learning: CNN, RNN, LSTM, Encoders, Transformers, Language Modelling
# - 🖺 Natural Language Processing: Language Modeling, Named Entity Recognition, Summarization, Classification, Question Answering, Coreference Resolution.
# - 🗄️ Databases: Postgres, Snowflake, MongoDB
# - ⏭ Big Data: PySpark and Hive
# - 🛠 MLOps: Git/Bitbucket, Docker, Kubernetes, Feature Store, Experiment Store (MLFlow), Model Deployment and Monitoring, Drift Monitoring, Splunk.
# """
# )
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Apply a predefined theme
# st.set_page_config(page_title="Resume", page_icon=":clipboard:")
import streamlit as st
import pandas as pd

# --- SKILLS ---
st.write('\n')
st.subheader("Key Skills")

skills_data = [
    ("Programming Languages", "Python & R", "⭐⭐⭐⭐⭐"),
    ("Python Frameworks", "Flask, FastAPI, Streamlit, Plotly, Locust", "⭐⭐⭐⭐"),
    ("ML/DL Frameworks and Tools", "H2O.ai, H2O Driverless AI, XGBoost, Tensorflow, Pytorch, Keras", "⭐⭐⭐⭐"),
    ("Data Visualization", "Plotly, Dash, Kibana, Matplotlib, Seaborn", "⭐⭐⭐"),
    ("Machine Learning", "Regression Analysis, Classification, Clustering, Dimensionality Reduction, Evaluation Techniques, Optimization Techniques", "⭐⭐⭐⭐⭐"),
    ("Deep Learning", "CNN, RNN, LSTM, Encoders, Transformers, Language Modelling", "⭐⭐⭐⭐"),
    ("Natural Language Processing", "Language Modeling, Named Entity Recognition, Summarization, Classification, Question Answering, Coreference Resolution", "⭐⭐⭐⭐"),
    ("Databases", "Postgres, Snowflake, MongoDB", "⭐⭐⭐"),
    ("Big Data", "PySpark and Hive", "⭐⭐⭐"),
    ("MLOps", "Git/Bitbucket, Docker, Kubernetes, Feature Store, Experiment Store (MLFlow), Model Deployment and Monitoring, Drift Monitoring, Splunk", "⭐⭐⭐⭐")
]

df_skills = pd.DataFrame(skills_data, columns=["Skill Area", "Skills", "Expertise"])

# Add custom CSS to enhance table styling
st.markdown("""
<style>
table {
    width: 100%;
    border-collapse: collapse;
}
th, td {
    padding: 10px;
    text-align: center;
    border-bottom: 1px solid #e0e0e0;
}
th {
    background-color: #f5f5f5;
}
tr:hover {
    background-color: #f0f0f0;
}
</style>
""", unsafe_allow_html=True)

# Display the table
st.table(df_skills.set_index('Skill Area'))


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Lead Machine Learning Engineer | Mastercard**")
st.write("07/2019 - Present")
st.write(
    """
- ► Used PowerBI and SQL to redefine and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**NLP Engineer | Synerzip Softech India Pvt Ltd**")
st.write("05/2017 - 07/2019")
st.write(
    """
- ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales efforts by 12%
- ► Modeled targets likely to renew and presented analysis to leadership, which led to a YoY revenue increase of $300K
- ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Software Engineer | TechnowingsInc**")
st.write("10/2015 - 04/2017")
st.write(
    """
- ► Devised KPIs using SQL across the company website in collaboration with cross-functional teams to achieve a 120% jump in organic traffic
- ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
- ► Collaborated with the analyst team to oversee the end-to-end process surrounding customers' return data
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")

st.write("🏆", "**Data Scientist Workbench | Mastercard**")
st.write(
    """
- ► Used PowerBI and SQL to redefine and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

st.write('\n')
st.write("🏆", "**Settlement Predictor | Mastercard**")
st.write(
    """
- ► Used PowerBI and SQL to redefine and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

st.write('\n')
st.write("🏆", "**Merchants Data Standardization**")
st.write(
    """
- ► Used PowerBI and SQL to redefine and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

st.write('\n')
st.write("🏆", "**Accelerating Cancer Cure**")
st.write(
    """
- ► Used PowerBI and SQL to redefine and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)