import fitz  # PyMuPDF
from gemini_feedback import get_resume_feedback
from summarizer import generate_summary_and_verdict
from report_generator import save_as_pdf, compute_match_score, COMMON_SKILLS
from ner_parser import extract_entities
from skill_gap_checker import check_skill_gap
import re

def analyze_resume_from_file(file, jd_text):
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    resume_text = "\n".join([page.get_text() for page in pdf])

    feedback = get_resume_feedback(resume_text, jd_text)
    summary = generate_summary_and_verdict(resume_text, jd_text)

    score_match = re.search(r'[Ss]core[:\s-]*?(\d+(?:\.\d+)?)(?:\s*/10)?', feedback)
    score = float(score_match.group(1)) if score_match else 7.0

    skill_analysis = check_skill_gap(resume_text, jd_text)

    match_score, matched_skills, missing_skills = compute_match_score(resume_text, jd_text, COMMON_SKILLS)

    report_data = {
        "Skill Gap Analysis": skill_analysis,
        "LLM Feedback": feedback,
        "LLM Summary & Verdict": summary,
        "Score": score,
        "Match Score": match_score,
        "Matched Skills": matched_skills,
        "Missing Skills": missing_skills
    }

    report_path = save_as_pdf(report_data, "reports/resume_report.pdf")
    report_data["Report Path"] = report_path
    return report_data



