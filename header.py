import streamlit as st

def render_header():
    st.markdown("""
    <style>
    body { background-color: #0f172a; }
    .hero {
        background: linear-gradient(90deg, #1e293b, #0f172a);
        padding: 20px;
        border-radius: 10px;
    }
    .hero-title { font-size: 28px; font-weight: 700; color: #f8fafc; }
    .hero-sub { color: #94a3b8; font-size: 14px; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">
    <div class="hero-title">Career Intelligence Platform</div>
    <div class="hero-sub">
    Skill Mapping • Gap Intelligence • Career Readiness Analytics
    </div>
    </div>
    <br>
    """, unsafe_allow_html=True)
