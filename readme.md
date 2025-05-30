# ResumeRadar

ResumeRadar is a simple web app that helps job seekers check how well their resume matches a job description by calculating a match score based on keyword overlap. It works similarly to an ATS (Applicant Tracking System) score by highlighting missing keywords and giving a percentage match.

---

## Features

- Upload your resume in PDF format.
- Paste a job description.
- Get a match score (%) indicating how well your resume fits the job.
- See a list of important missing keywords to improve your resume.

---

## Tech Stack

- Backend: Python, Flask, PyMuPDF (fitz), Flask-CORS
- Frontend: HTML, Bootstrap, JavaScript (Fetch API)

---

## Installation & Setup

1. **Clone the repo** (or create your project folder):

   ```bash
   mkdir ResumeRadar
   cd ResumeRadar

2. **Create a Python virtual environment** (optional but recommended):
python -m venv venv
.\venv\Scripts\activate      # Windows
source venv/bin/activate     # macOS/Linux

3. **Install dependencies**:
pip install flask flask-cors pymupdf

4. **Create app.py and paste the backend code**:
from flask import Flask, request, jsonify
from flask_cors import CORS
import fitz  # PyMuPDF

app = Flask(__name__)
CORS(app)

def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

@app.route('/match', methods=['POST'])
def match_resume():
    resume_file = request.files['resume']
    jd_text = request.form['jd']

    resume_text = extract_text_from_pdf(resume_file)

    # Normalize and split words
    jd_words = set(jd_text.lower().split())
    resume_words = set(resume_text.lower().split())

    matching_words = jd_words.intersection(resume_words)

    if len(jd_words) == 0:
        match_score = 0
    else:
        match_score = int((len(matching_words) / len(jd_words)) * 100)

    missing_words = list(jd_words - resume_words)

    return jsonify({
        'score': match_score,
        'missing_keywords': missing_words
    })

if __name__ == '__main__':
    app.run(debug=True)

5. **Create index.html with the frontend code** (make sure it points to the backend at http://127.0.0.1:5000/match).

6. **Run the backend server**:

python app.py
Open index.html in your browser (double click or open via a local server).

**How It Works**
Upload a PDF resume.

Paste the job description text.

The backend extracts the resume text from the PDF.

It compares keywords from the job description to the resume.

Calculates a match percentage.

Returns missing keywords.

Frontend displays the score and missing keywords.

Usage Tips
Aim for a higher match score by including more relevant keywords in your resume.

Review missing keywords to tailor your resume better for the specific job.

Use the tool to optimize your resume before applying.

Future Improvements
Add smarter text preprocessing (remove punctuation, handle synonyms).

Use TF-IDF or NLP for better matching.

Add user authentication and saving resumes/jobs.

Deploy the app online for wider access.

Add feedback or resume improvement suggestions.