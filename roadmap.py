import streamlit as st

def render_roadmap(role, missing):

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("30-Day Strategic Improvement Roadmap")

    for skill in missing:

        st.markdown(f"### Skill Gap: {skill}")

        if skill == "Deep Learning":
            st.write("Current Gap: Limited exposure to neural networks and advanced architectures.")
            st.write("Free Learning Resources:")
            st.markdown("- [DeepLearning.AI Course](https://www.deeplearning.ai/)")
            st.markdown("- [Neural Networks Explained (YouTube)](https://www.youtube.com/watch?v=aircAruvnKk)")
            st.write("Practical Task:")
            st.write("- Build a simple neural network using TensorFlow.")

        elif skill == "TensorFlow":
            st.write("Current Gap: Framework-level implementation skills missing.")
            st.write("Free Learning Resources:")
            st.markdown("- [TensorFlow Official Tutorials](https://www.tensorflow.org/tutorials)")
            st.markdown("- [TensorFlow Beginner Guide](https://www.youtube.com/results?search_query=tensorflow+tutorial+beginner)")
            st.write("Practical Task:")
            st.write("- Implement image classification using MNIST dataset.")

        elif skill == "MLOps":
            st.write("Current Gap: Model deployment and lifecycle management not covered.")
            st.write("Free Learning Resources:")
            st.markdown("- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)")
            st.markdown("- [Docker Getting Started](https://docs.docker.com/get-started/)")
            st.write("Practical Task:")
            st.write("- Containerize a trained ML model and deploy locally.")

        elif skill == "Advanced React":
            st.write("Current Gap: Advanced state handling and performance optimization.")
            st.write("Free Learning Resources:")
            st.markdown("- [React Official Documentation](https://react.dev/learn)")
            st.markdown("- [React Hooks Guide](https://www.youtube.com/results?search_query=react+hooks+tutorial)")
            st.write("Practical Task:")
            st.write("- Build a multi-page React dashboard with routing.")

        elif skill == "Next.js":
            st.write("Current Gap: Server-side rendering and routing framework knowledge missing.")
            st.write("Free Learning Resources:")
            st.markdown("- [Next.js Official Docs](https://nextjs.org/docs)")
            st.markdown("- [Next.js Crash Course](https://www.youtube.com/results?search_query=nextjs+tutorial)")
            st.write("Practical Task:")
            st.write("- Convert existing React app into Next.js app.")

        elif skill == "Optimization":
            st.write("Current Gap: Performance tuning and scalability practices missing.")
            st.write("Free Learning Resources:")
            st.markdown("- [Web Performance Guide](https://web.dev/performance/)")
            st.markdown("- [Lighthouse Tool Guide](https://developer.chrome.com/docs/lighthouse/)")
            st.write("Practical Task:")
            st.write("- Improve Lighthouse score above 90.")

        elif skill == "Advanced SQL":
            st.write("Current Gap: Complex queries and performance tuning not covered.")
            st.write("Free Learning Resources:")
            st.markdown("- [SQLBolt](https://sqlbolt.com/)")
            st.markdown("- [Kaggle SQL Course](https://www.kaggle.com/learn/sql)")
            st.write("Practical Task:")
            st.write("- Write complex joins and optimize queries.")

        elif skill == "Power BI":
            st.write("Current Gap: Dashboard building and business reporting missing.")
            st.write("Free Learning Resources:")
            st.markdown("- [Microsoft Power BI Learning](https://learn.microsoft.com/en-us/training/powerplatform/power-bi)")
            st.write("Practical Task:")
            st.write("- Create a professional sales dashboard.")

        elif skill == "Statistics":
            st.write("Current Gap: Statistical reasoning and hypothesis testing weak.")
            st.write("Free Learning Resources:")
            st.markdown("- [Khan Academy Statistics](https://www.khanacademy.org/math/statistics-probability)")
            st.write("Practical Task:")
            st.write("- Perform hypothesis testing on sample dataset.")

        st.markdown("---")

    st.markdown('</div>', unsafe_allow_html=True)
