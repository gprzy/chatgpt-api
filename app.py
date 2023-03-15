import os
import openai
from dotenv import load_dotenv
from src.chatgpt_utils import *
from flask import Flask, request, jsonify


load_dotenv()

app = Flask(__name__)
app.config['GPT_API_KEY'] = os.environ['GPT_API_KEY']
openai.api_key = os.environ['GPT_API_KEY']


@app.route('/chatgpt', methods=['POST'])
def get_first_post():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    
    if not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
        return jsonify({'error': 'Invalid data structure'}), 400
    
    if len(data) == 0:
        return jsonify({'error': 'No posts found'}), 404

    answer = gpt_answer(
        messages=data
    )

    return jsonify({'answer': answer}), 200


@app.route('/health')
def health_check():
    return jsonify({'status': 'Alive!'})


if __name__ == '__main__':
    app.run(debug=True)
