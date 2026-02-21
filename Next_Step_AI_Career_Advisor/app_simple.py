import os
from flask import Flask, request, jsonify
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
    return "The Python Server is ALIVE on Port 5001!"

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
        f"Provide personalized career advice for {name}.\n\n"
        f"Profile Details:\n"
        f"- Current Situation: {situation}\n"
        f"- Education: {studies_text}\n"
        f"- Primary Objective: {goal}\n"
        f"- Favorite Subject: {subject}\n"
        f"- Work Style: {workstyle}\n"
        f"- Problem Solving Approach: {problem_style}\n"
        f"- Preference: {task_pref}\n"
        f"- Self-Description: {personality}\n\n"
        f"Based on these traits, recommend 2 suitable career paths and 3 clear next steps."
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