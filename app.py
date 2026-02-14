import streamlit as st
from components.header import render_header
from components.skills import analyze_skills
from components.analytics import render_analytics
from components.roadmap import render_roadmap
from components.legend import render_legend
from utils.parser import extract_text_from_pdf
from components.salary import render_salary_estimator
from components.report import render_download_button


st.set_page_config(page_title="Career Intelligence Suite", layout="wide")

render_header()

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
role = st.selectbox("Select Target Role",
                    ["AI Engineer", "Frontend Developer", "Data Analyst"])
if uploaded_file:

    resume_text = extract_text_from_pdf(uploaded_file)
    st.success("Resume processed successfully.")

    skills, missing, match_percentage = analyze_skills(resume_text, role)

    render_analytics(skills, missing, match_percentage)

    render_salary_estimator(role, match_percentage)

    render_download_button(role, skills, missing, match_percentage)

    render_roadmap(role, missing)

    render_legend()
