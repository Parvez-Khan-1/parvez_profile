import plotly.graph_objects as go
from pathlib import Path
from PIL import Image
import streamlit as st
import pandas as pd
import plotly.express as px


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


SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/parvezkhan-pathan-389065105/",
    "GitHub": "https://github.com/Parvez-Khan-1",
    "Stackoverflow": "https://stackoverflow.com/users/5536013/parvez-khan",
    "Medium": "https://medium.com/@parvezpathan09",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


EMAIL = "ParvezPathan09@gmail.com"

# --- HERO SECTION ---
col1, col2 = st.columns([1, 3])
with col1:
    st.image(profile_pic, width=150)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    # with st.expander("Contact Information"):
    #     st.write("📫", EMAIL)
    #     st.download_button(
    #         label=" 📄 Download Resume",
    #         data=PDFbyte,
    #         file_name=resume_file.name,
    #         mime="application/octet-stream",
    #     )
st.write('\n')

# --- SOCIAL LINKS ---
with st.container():
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):

        icon = "🤝"

        if platform == "LinkedIn":
            icon = "🚀"

        if platform == "GitHub":
            icon = "👨‍💻"

        if platform == "Medium":
            icon = "Ⓜ"

        cols[index].markdown(f"{icon} [{platform}]({link})", unsafe_allow_html=True)

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

# Apply a predefined theme
# st.set_page_config(page_title="Resume", page_icon=":clipboard:")
import streamlit as st
import pandas as pd

# --- SKILLS ---
st.write('\n')
st.subheader("Key Skills")

skills_data = [
    ("Programming Languages", "Python & R", "⭐⭐⭐⭐⭐", 5),
    ("Python Frameworks", "Flask, FastAPI, Streamlit, Plotly, Locust", "⭐⭐⭐⭐", 4.5),
    ("ML/DL Frameworks and Tools", "H2O.ai, H2O Driverless AI, XGBoost, Tensorflow, Pytorch, Keras", "⭐⭐⭐⭐", 4),
    ("Data Visualization", "Plotly, Dash, Kibana, Matplotlib, Seaborn", "⭐⭐⭐", 3),
    ("Machine Learning", "Regression Analysis, Classification, Clustering, Dimensionality Reduction, Evaluation Techniques, Optimization Techniques", "⭐⭐⭐⭐⭐", 5),
    ("Deep Learning", "CNN, RNN, LSTM, Encoders, Transformers, Language Modelling", "⭐⭐⭐⭐", 4.1),
    ("Natural Language Processing", "Language Modeling, Named Entity Recognition, Summarization, Classification, Question Answering, Coreference Resolution", "⭐⭐⭐⭐", 4.3),
    ("Databases", "Postgres, Snowflake, MongoDB", "⭐⭐⭐", 3),
    ("Big Data", "PySpark and Hive", "⭐⭐⭐", 2.8),
    ("MLOps", "Git/Bitbucket, Docker, Kubernetes, Feature Store, Experiment Store (MLFlow), Model Deployment and Monitoring, Drift Monitoring, Splunk", "⭐⭐⭐⭐", 4.1)
]

# Extract skills and expertise levels for plotting
df_skills = pd.DataFrame(skills_data, columns=["Skill Area", "Skills", "Expertise", "ExpertiseLevel"])
skills = df_skills['Skill Area'].str.split(', ', expand=True)
# df_skills.sort_values(by=['ExpertiseLevel'], ascending=False, inplace=True)
# Create a grouped bar chart using Plotly Express
fig = px.bar(
    df_skills,
    x="Skill Area",
    y="ExpertiseLevel",
    color="ExpertiseLevel",
    color_continuous_scale="Viridis",  # You can adjust the color scale
    hover_data={"Skills": True},  # Include "Skills" in hover data
    labels={"Skills": "Skills: "},  # Set label for hover template
)

# Update hover template to include "Skills"
fig.update_traces(
    hovertemplate="%{yaxis.title.text}: %{y}<br>%{customdata[0]}",
    selector=dict(type="bar"),
)

# Update layout for better visualization
fig.update_layout(
    xaxis_title="Skill Area",
    yaxis_title="Expertise Level",
    showlegend=True,  # Show color scale legend
    coloraxis_colorbar_title="Expertise Level",
)

# Display the Plotly figure using Streamlit
st.write('\n')
st.plotly_chart(fig)

# df_skills = pd.DataFrame(skills_data, columns=["Skill Area", "Skills", "Expertise",  "ExpertiseLevel"])
# df_skills = df_skills[["Skill Area", "Skills"]]
# # Display the table
# st.table(df_skills.set_index('Skill Area'))



# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# Define all jobs
all_jobs = [
    ("🚧", "Lead Machine Learning Engineer | Mastercard", "07/2019 - Present",
     """
     - ► Used PowerBI and SQL to redefine and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
     - ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
     - ► Redesigned data model through iterations that improved predictions by 12%
     """),

    ("🚧", "NLP Engineer | Synerzip Softech India Pvt Ltd", "05/2017 - 07/2019",
     """
     - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales efforts by 12%
     - ► Modeled targets likely to renew and presented analysis to leadership, which led to a YoY revenue increase of $300K
     - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
     """),

    # ... Add more job entries here
]

# Display the first two jobs
displayed_jobs = all_jobs[:2]
for job in displayed_jobs:
    st.write('\n')
    st.write(job[0], "**" + job[1] + "**")
    st.write(job[2])
    st.write(job[3])

# "Show All" button to pop up a window with all jobs
if len(all_jobs) > 2:
    if st.button("Show All"):
        st.write('\n')
        st.subheader("All Work History")
        st.write("---")
        for job in all_jobs:
            st.write('\n')
            st.write(job[0], "**" + job[1] + "**")
            st.write(job[2])
            st.write(job[3])

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

# Sidebar content
st.sidebar.title("Jump to Section")
sections = ["Executive-Summary", "Key-Skills", "Work-History", "Projects-Accomplishments"]

# Create a dynamic anchor for each section
for section in sections:
    st.sidebar.markdown(f'<a href="#{section.lower()}">{section}</a>', unsafe_allow_html=True)

# # Add some space below the sidebar
# st.sidebar.markdown('<div style="height: 20vh;"></div>', unsafe_allow_html=True)
#
# # Content sections
# st.markdown("<div id='Introduction'></div>", unsafe_allow_html=True)
# st.markdown("## Introduction")
# st.write("This is the introduction section.")
#
# st.markdown("<div id='Content'></div>", unsafe_allow_html=True)
# st.markdown("## Content")
# st.write("This is the content section.")
#
# st.markdown("<div id='Projects & Accomplishments'></div>", unsafe_allow_html=True)
# st.markdown("## Projects & Accomplishments")
# st.write("This is the Projects & Accomplishments")

# Function to read and update view count from a file
def update_view_count():
    try:
        with open("view_count.txt", "r") as f:
            count = int(f.read())
    except FileNotFoundError:
        count = 0

    count += 1

    with open("view_count.txt", "w") as f:
        f.write(str(count))

    return count


# Get the current view count
view_count = update_view_count()

st.markdown("<p class='view-count'>Views: %d</p>" % view_count, unsafe_allow_html=True)
