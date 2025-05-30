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
