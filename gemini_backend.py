from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini API (directly using provided key if .env not set)
API_KEY = os.getenv('GEMINI_API_KEY') or 'AIzaSyCBv8jNE-5K8Ojs0UumdeBL_Zba68b4e18'
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        if not user_message:
            return jsonify({'status': 'error', 'message': 'No message provided'}), 400
        # Generate response from Gemini
        response = model.generate_content(user_message)
        return jsonify({
            'status': 'success',
            'response': response.text
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
