from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

BRAINSHOP_API_URL = "http://api.brainshop.ai/get"

# Replace these values with your BrainShop.ai credentials
BRAINSHOP_API_KEY = "ji1KJlAIZuOEMt07"
BRAINSHOP_UID = "178608"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    if request.method == 'POST':
        user_input = request.form.get('user_input')

        try:
            # Make a request to BrainShop.ai API
            response = requests.get(BRAINSHOP_API_URL, params={
                'bid': BRAINSHOP_UID,
                'key': BRAINSHOP_API_KEY,
                'uid': '1',
                'msg': user_input
            }, verify=False)

            response.raise_for_status()  # Check for request success

            # Extract the chat response from the API
            chat_response = response.json().get('cnt')

            return render_template('index.html', user_input=user_input, chat_response=chat_response)

        except requests.exceptions.RequestException as e:
            # Handle any request exceptions (e.g., network issues, timeouts)
            error_message = f"Error communicating with BrainShop.ai: {str(e)}"
            return render_template('index.html', user_input=user_input, chat_response=error_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
