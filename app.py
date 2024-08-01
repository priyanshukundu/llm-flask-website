import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables
load_dotenv()

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key='your_api_key',
    api_version="2024-02-01",
    azure_endpoint='https://mbuaiplayground.openai.azure.com/'
)

app = Flask(__name__)

def get_response_from_azure_openai(prompt):
    """
    Gets response from Azure OpenAI based on prompt.
    """
    response = client.chat.completions.create(
        model="gpt-35-turbo",  # Replace with your deployed model name
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = get_response_from_azure_openai(user_input)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
