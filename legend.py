import streamlit as st

def render_legend():

    st.subheader("Analytics Interpretation Guide")

    st.write("Executive Gauge:")
    st.write("- Green indicates achieved competency level.")
    st.write("- Dark indicates remaining skill gap.")

    st.write("Heatmap:")
    st.write("- Brighter cells indicate stronger proficiency.")
    st.write("- Darker cells indicate skill gaps.")
