import streamlit as st

def render_salary_estimator(role, match_percentage):

    st.subheader("Salary Projection Estimate")

    base_salary = 0

    if role == "AI Engineer":
        base_salary = 1200000
    elif role == "Frontend Developer":
        base_salary = 800000
    elif role == "Data Analyst":
        base_salary = 900000

    projected_salary = int(base_salary * (match_percentage / 100))

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Current Market Base (₹)", f"{base_salary:,}")

    with col2:
        st.metric("Estimated Offer Potential (₹)", f"{projected_salary:,}")

    st.write("Note: Projection adjusts base market salary according to skill match percentage.")
