import streamlit as st
from analyze_resume import analyze_resume_from_file
import base64
import os

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI Resume Analyzer")

uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description")

if st.button("Analyze") and uploaded_resume and job_description:
    with st.spinner("Analyzing..."):
        result = analyze_resume_from_file(uploaded_resume, job_description)


        #  Gemini Feedback
        st.subheader("📝 Feedback on Resume")
        st.write(result.get("LLM Feedback", "Not Available"))

        #  Summary & Verdict
        st.subheader("🧠 Summary & Verdict")
        verdict_data = result.get("LLM Summary & Verdict", {})
        if isinstance(verdict_data, dict):
            st.write(f"**Summary:** {verdict_data.get('summary', 'N/A')}")
            st.write(f"**Verdict:** {verdict_data.get('verdict', 'N/A')}")
        else:
            st.write(verdict_data)

        # Skill gap Analysis
        st.subheader("📊 Skill Analysis")
        skill_gap = result.get("Skill Gap Analysis", {})
        if skill_gap:
            st.write("**Resume Skills:**", ", ".join(skill_gap.get("Resume Skills", [])))
            st.write("**JD Required Skills:**", ", ".join(skill_gap.get("JD Required Skills", [])))
            st.write("**Missing Skills:**", ", ".join(skill_gap.get("Missing Skills", [])))
            st.write("**Extra/Bonus Skills:**", ", ".join(skill_gap.get("Extra/Bonus Skills", [])))
        else:
            st.write("No skill gap analysis available.")

        #  Resume Match Score
        st.subheader("✅ Resume Match Score")
        st.write(f"**Overall Match Score**: {result.get('Match Score', 'N/A')}%")
        
        # Download Report
        st.subheader("📥 Download Report")
        pdf_path = "reports/resume_report.pdf"
        if os.path.exists(pdf_path):
            with open(pdf_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                href = f'<a href="data:application/pdf;base64,{base64_pdf}" download="resume_report.pdf">Download PDF Report</a>'
                st.markdown(href, unsafe_allow_html=True)
