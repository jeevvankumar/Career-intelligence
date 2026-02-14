def analyze_skills(text, role):

    skills = []

    if "python" in text:
        skills.append("Python")
    if "machine learning" in text:
        skills.append("Machine Learning")
    if "react" in text:
        skills.append("React")
    if "sql" in text:
        skills.append("SQL")

    if role == "AI Engineer":
        missing = ["Deep Learning", "TensorFlow", "MLOps"]
        match = 65
    elif role == "Frontend Developer":
        missing = ["Advanced React", "Next.js", "Optimization"]
        match = 70
    else:
        missing = ["Advanced SQL", "Power BI", "Statistics"]
        match = 68

    return skills, missing, match
