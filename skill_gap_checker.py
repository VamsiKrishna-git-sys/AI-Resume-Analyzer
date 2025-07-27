def extract_skills(text):
    text = text.lower()
    keywords = [
    # Programming Languages
    "python", "java", "javascript", "c", "c++", "c#", "go", "typescript", "kotlin", "swift", "r", "matlab", "bash", "shell",

    # Web Development
    "html", "css", "html-css", "react", "angular", "vue", "next.js", "node.js", "flask", "django",

    # Databases
    "sql", "mysql", "postgresql", "sqlite", "nosql", "mongodb", "cassandra", "redis", "oracle", "firebase",

    # Cloud Platforms
    "aws", "azure", "gcp", "google cloud", "heroku", "digitalocean",

    # DevOps & Tools
    "docker", "kubernetes", "jenkins", "git", "github", "gitlab", "ci/cd", "terraform", "ansible",

    # Data Science & ML
    "pandas", "numpy", "scikit-learn", "tensorflow", "keras", "pytorch", "opencv", "nltk", "spacy", "huggingface",
    "matplotlib", "seaborn", "power bi", "tableau", "machine learning", "deep learning", "nlp", "data analysis",

    # Cybersecurity
    "network security", "penetration testing", "ethical hacking", "owasp", "siem",

    # Testing
    "unit testing", "pytest", "junit", "selenium", "cypress", "postman", "api testing",

    # Soft Skills
    "communication", "teamwork", "collaboration", "leadership", "time management", "problem solving",
    "adaptability", "critical thinking", "conflict resolution", "creativity", "emotional intelligence",

    # Business & Management
    "agile", "scrum", "kanban", "project management", "product management", "business analysis",
    "stakeholder management", "requirements gathering", "presentation skills",

    # Mobile Development
    "android", "ios", "react native", "flutter",

    # Marketing & Analytics
    "seo", "sem", "google analytics", "email marketing", "social media marketing", "hootsuite", "buffer",

    # Finance & Accounting
    "financial modeling", "excel", "sap", "quickbooks", "tally",

    # Healthcare
    "hipaa", "ehr", "electronic health records", "medical terminology",

    # Design
    "ui design", "ux design", "figma", "adobe xd", "sketch", "photoshop", "illustrator", "canva",

    # Trending Technologies
    "generative ai", "prompt engineering","llm", "lang chain", "blockchain", "web3", "vr", "quantum computing",
    "low-code", "no-code", "bubble", "outsystems", "chatbot development", "dialogflow", "rasa"
]

    return list(set([kw for kw in keywords if kw in text]))

def check_skill_gap(resume_text, jd_text):
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    missing = list(set(jd_skills) - set(resume_skills))
    extra = list(set(resume_skills) - set(jd_skills))

    return {
        "Resume Skills": resume_skills,
        "JD Required Skills": jd_skills,
        "Missing Skills": missing,
        "Extra/Bonus Skills": extra
    }
