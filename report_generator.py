from fpdf import FPDF
import json
import os

def save_as_json(report_data, output_path):
    with open(output_path, "w") as f:
        json.dump(report_data, f, indent=4)

class PDFReport(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 14)
        self.cell(0, 10, "Resume Evaluation Report", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def draw_line(self, text, font="Helvetica", style="", size=12, height=6, add_spacing=True):
        self.set_font(font, style=style, size=size)
        self.multi_cell(0, height, text)
        if add_spacing:
            self.ln(1)


COMMON_SKILLS = [
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

def extract_skills(text, COMMON_SKILLS):
    text = text.lower()
    return {skill for skill in COMMON_SKILLS if skill.lower() in text}

def compute_match_score(resume_text, jd_text, COMMON_SKILLS):
    resume_skills = extract_skills(resume_text, COMMON_SKILLS)
    jd_skills = extract_skills(jd_text, COMMON_SKILLS)

    if not jd_skills:
        return 0, [], []

    overlap = resume_skills & jd_skills
    score = (len(overlap) / len(jd_skills)) * 100
    return round(score, 2), list(overlap), list(set(jd_skills) - set(resume_skills))

def save_as_pdf(report_data, output_path):
    pdf = PDFReport()
    pdf.alias_nb_pages()
    pdf.add_page()

    draw_line = pdf.draw_line

    # Feedback
    feedback_data = report_data.get("LLM Feedback", "")
    if isinstance(feedback_data,dict):
        feefback_text = f"Feedback: {feedback_data.get('Feedback', '')}\n\nScore: {feedback_data.get('score', '')}"
    else:
        feedback_text = feedback_data
    draw_line("\nFeedback on Resume:", font="Helvetica", style="B", size=12)
    draw_line(feedback_text)


    # Summary and Hiring Verdict
    summary_data = report_data.get("LLM Summary & Verdict", "")
    if isinstance(summary_data, dict):
        summary_text = f"Summary: {summary_data.get('summary', '')}\n\nVerdict: {summary_data.get('verdict', '')}"
    else:
        summary_text = summary_data
    draw_line("\nSummary & Hiring Verdict:", font="Helvetica", style="B", size=12)
    draw_line(summary_text)

    # Skills Comparison
    draw_line("Skill Gap Analysis:", font="Helvetica", style="B", size=12, height=8)

    skill_gap = report_data.get("Skill Gap Analysis", {})
    for category, skills in skill_gap.items():
        draw_line(f"{category}:", font="Helvetica", style="B", size=11, height=7)
        if skills:
            draw_line("- " + ", ".join(skills), height=6)
        else:
            draw_line("- None", height=6)


    # Resume Match Score
    draw_line("\nResume Match Score:", font="Helvetica", style="B", size=12)
    draw_line(f"Score: {report_data.get('Match Score', 'N/A')}")


    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf.output(output_path)
    return output_path
