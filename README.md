# 🤖 AI Resume Analyzer

An intelligent Resume Analyzer that compares resumes with job descriptions, provides AI-powered feedback, highlights skill gaps, and generates professional reports.

## Features

- Generates smart feedback using **gemini-1.5-flash-latest** model
- Summarizes resume and provides a hiring verdict
- Analyzes Resume skills with skills required in Job Description 
- Computes Resume Match Score against a Job Description
- Exports a clean, well-structured PDF report

## How It Works

1. Upload your **resume** (`.pdf`) and a **job description** (`.txt`)
2. The app will:
   - Parse key details
   - Analyze skills and gaps
   - Get feedback
   - Compute match score
3. Get a complete PDF report

## 🛠 Tech Stack

- `Python 3.11+`
- `Streamlit` for frontend
- `fpdf` for PDF generation
- `Gemini Pro` (via `google.generativeai`)
- `PyMuPDF` for resume parsing

## 📁 Project Structure

resume_analyzer/
├── app.py # ✅ Streamlit frontend
├── analyze_resume.py # ✅ Main backend orchestrator
├── gemini_feedback.py # Gemini prompt logic
├── summarizer.py # Gemini-based summarizer
├── report_generator.py # PDF & JSON report generation
├── skill_gap_checker.py # Skill Gap Detection
├── ner_parser.py # Entity Extraction
├── sample_resume.pdf
├── sample_jd.txt
├── reports/ # Stores generated reports
│ ├── resume_report.pdf
