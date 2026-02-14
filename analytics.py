import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def render_analytics(skills, missing, match_percentage):

    readiness_score = match_percentage / 100

    st.subheader("Executive Readiness Gauge")

    fig_gauge, ax_gauge = plt.subplots(figsize=(2,2), dpi=200)

    ax_gauge.pie(
        [readiness_score, 1-readiness_score],
        startangle=90,
        colors=["#4ade80", "#334155"],
        wedgeprops=dict(width=0.18)
    )

    ax_gauge.text(0, 0, f"{match_percentage}%", ha='center', va='center', fontsize=8)
    ax_gauge.set(aspect="equal")
    ax_gauge.axis("off")

    st.pyplot(fig_gauge)

    st.subheader("Skill Heatmap")

    labels = skills + missing
    values = [0.8 if s in skills else 0.3 for s in labels]
    heat = np.array(values).reshape(1,-1)

    fig_heat, ax_heat = plt.subplots(figsize=(4,0.8), dpi=200)

    ax_heat.imshow(heat, aspect='auto', cmap="viridis")
    ax_heat.set_xticks(np.arange(len(labels)))
    ax_heat.set_xticklabels(labels, rotation=25, ha='right', fontsize=6)
    ax_heat.set_yticks([])

    for spine in ax_heat.spines.values():
        spine.set_visible(False)

    st.pyplot(fig_heat)
