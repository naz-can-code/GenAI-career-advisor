import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
# Note: Use "gemini-2.5-flash" or "gemini-2.0-flash-exp"
MODEL = os.getenv("GOOGLE_MODEL", "gemini-2.5-flash")

if not API_KEY:
    raise RuntimeError("Missing GOOGLE_API_KEY in .env file.")

genai.configure(api_key=API_KEY)

app = Flask(__name__)
CORS(app)


# ADD THIS PART:
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generate-prompt', methods=['POST'])
def generate_prompt():
    data = request.get_json() or {}

    # Extract all values sent from the HTML form
    name = data.get('name', 'User')
    situation = data.get('situation', 'Not specified')
    studies = data.get('studies', [])
    goal = data.get('goal', 'Not specified')
    subject = data.get('subject', 'Not specified')
    workstyle = data.get('workstyle', 'Not specified')
    problem_style = data.get('problemStyle', 'Not specified')
    task_pref = data.get('taskPreference', 'Not specified')
    personality = data.get('personalityType', 'Not specified')

    studies_text = ', '.join(studies) if isinstance(studies, list) else str(studies)

    # Construct the detailed prompt
    prompt = (
    f"You are a professional career advisor.\n\n"
    f"Provide personalised career advice for the person below:\n\n"
    f"Name: {name}\n"
    f"Situation: {situation}\n"
    f"Education: {studies_text}\n"
    f"Primary Objective: {goal}\n"
    f"Subjects They Enjoy: {subject}\n"
    f"What They Enjoy Most: {workstyle}\n"
    f"Problem Solving Style: {problem_style}\n"
    f"Task Preference: {task_pref}\n"
    f"Personality Description: {personality}\n\n"
    "Based on this profile:\n"
    "1. Write a short motivational paragraph.\n"
    "2. Suggest 3 highly suitable career paths.\n"
    "3. Explain WHY those careers match their personality.\n"
    "4. Give 3 clear next steps.\n\n"
    
    "IMPORTANT: Format your response exactly as follows:\n\n"
    "=== MOTIVATION ===\n"
    "(Write the motivational paragraph here)\n\n"
    "=== CAREER PATHS ===\n"
    "1. Career Title\n"
    "- Explanation\n\n"
    "2. Career Title\n"
    "- Explanation\n\n"
    "3. Career Title\n"
    "- Explanation\n\n"
    "=== NEXT STEPS ===\n"
    "1. Step one\n"
    "2. Step two\n"
    "3. Step three\n\n"
    "Do not add extra sections. Keep it clean, structured, and easy to read."
    )

    try:
        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(prompt)
        ai_text = response.text
        
        return jsonify({
            'success': True, 
            'response': ai_text,
            'token_usage': {
                'input_tokens': 'Calculated by API',
                'output_tokens': 'Calculated by API',
                'total_tokens': 'N/A'
            }
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
