from flask import Flask, request, jsonify
from flask_cors import CORS

import openai

app = Flask(__name__)
CORS(app)

openai.api_key = ''

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        prompt = data.get('prompt')

        response = openai.ChatCompletion.create(
            model='gpt-4-turbo',  
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=100  
        )
        reply = response.choices[0].message['content']
        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
