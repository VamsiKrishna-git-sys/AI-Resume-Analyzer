import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY") # replace with your API key

model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def get_resume_feedback(resume_text, jd_text):
    prompt = f"""
You are a resume evaluator AI.

Compare the following resume and job description (JD), and:
1. Give feedback on alignment with the role
2. Mention key highlights or missing points
3. Give a score out of 10

### RESUME:
{resume_text}

### JOB DESCRIPTION:
{jd_text}

Respond in this format:

Feedback:
- ...
- ...

Score: x/10
"""
    response = model.generate_content(prompt)
    return response.text

