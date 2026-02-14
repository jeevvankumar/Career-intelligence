from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
import streamlit as st
import os

def generate_report(role, skills, missing, match_percentage):

    file_path = "career_report.pdf"
    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Career Intelligence Report", styles["Title"]))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph(f"Target Role: {role}", styles["Normal"]))
    elements.append(Paragraph(f"Match Percentage: {match_percentage}%", styles["Normal"]))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph("Extracted Skills:", styles["Heading2"]))
    skill_list = [ListItem(Paragraph(skill, styles["Normal"])) for skill in skills]
    elements.append(ListFlowable(skill_list))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph("Missing Skills:", styles["Heading2"]))
    missing_list = [ListItem(Paragraph(skill, styles["Normal"])) for skill in missing]
    elements.append(ListFlowable(missing_list))

    doc.build(elements)

    return file_path


def render_download_button(role, skills, missing, match_percentage):

    if st.button("Generate Downloadable Report"):

        file_path = generate_report(role, skills, missing, match_percentage)

        with open(file_path, "rb") as f:
            st.download_button(
                label="Download Career Report PDF",
                data=f,
                file_name="Career_Report.pdf",
                mime="application/pdf"
            )
