import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")  

model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def generate_summary_and_verdict(resume_text, jd_text):
    prompt = f"""
Compare the RESUME and the JOB DESCRIPTION.

Give a concise summary of strengths, weaknesses, and final hiring verdict (yes/maybe/no).

### RESUME:
{resume_text}

### JD:
{jd_text}

Return in this format:

Summary:
- ...

Verdict: [Yes/Maybe/No] with reason
"""
    response = model.generate_content(prompt)
    return response.text
