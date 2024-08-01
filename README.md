Flask Chatbot Project

This project is a simple Flask-based chatbot that interacts with users through a web interface. The chatbot utilizes Azure OpenAI to generate responses to user queries. The project includes three main files:

        app.py
        code.py
        index.html
        styles.css

Table of Contents

        Flask Chatbot Project
        Table of Contents
        Installation
        Usage
        Project Structure
        File Descriptions
        app.py
        code.py
        index.html
        styles.css
        Running the Project
        Contributing
        License
        Installation

Clone the repository:

Copy code
git clone https://github.com/priyanshukundu/llm-flask-website.git
cd llm-flask-website
Create a virtual environment and activate it:

Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required dependencies:

Copy code
pip install -r requirements.txt
Set up your environment variables by creating a .env file in the root directory and adding your Azure OpenAI credentials:

makefile
Copy code
API_KEY=your_api_key
AZURE_ENDPOINT=https://your-azure-endpoint.openai.azure.com/
Usage
After setting up the environment and installing the dependencies, you can run the Flask application to start the chatbot.

Project Structure

Copy code
llm-flask-website/
├── static/
│   └── styles.css
├── templates/
│   └── index.html
├── app.py
├── basic.py
├── requirements.txt
└── README.md

File Descriptions

app.py

This is the main Flask application file. It sets up the Flask app, defines routes, and handles communication with the Azure OpenAI service.

python

Copy code
import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables
load_dotenv()

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv('API_KEY'),
    api_version="2024-02-01",
    azure_endpoint=os.getenv('AZURE_ENDPOINT')
)

app = Flask(__name__)

def get_response_from_azure_openai(prompt):
    """
    Gets response from Azure OpenAI based on prompt.
    """
    response = client.chat.completions.create(
        model="gpt-35-turbo",
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
code.py
This file is a simple script for interacting with the chatbot in the console. It demonstrates how to send queries to the Azure OpenAI model and receive responses.

python

Copy code

import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables
load_dotenv()

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv('API_KEY'),
    api_version="2024-02-01",
    azure_endpoint=os.getenv('AZURE_ENDPOINT')
)

def get_response_from_azure_openai(prompt):
    """
    Gets response from Azure OpenAI based on prompt.
    """
    response = client.chat.completions.create(
        model="gpt-35-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def main():
    print("Welcome! Ask me anything or tell me a story, and I'll respond creatively.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "end"]:
            print("Goodbye!")
            break
        response = get_response_from_azure_openai(user_input)
        print(f"Bard: {response}")

if __name__ == "__main__":
    main()
index.html
This is the HTML file for the chatbot's web interface. It includes a simple chat interface with input and output sections.

html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <div class="chat-container">
        <h1>Chatbot</h1>
        <div class="chat-box" id="chat-box"></div>
        <form id="chat-form">
            <input type="text" id="user-input" placeholder="Type your message..." required>
            <button type="submit">Send</button>
        </form>
    </div>
    <script>
        document.getElementById('chat-form').onsubmit = async function(event) {
            event.preventDefault();
            const userInput = document.getElementById('user-input').value;
            document.getElementById('chat-box').innerHTML += `<div class="user-message">You: ${userInput}</div>`;
            document.getElementById('user-input').value = '';

            const response = await fetch('/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({ 'user_input': userInput })
            });

            const data = await response.json();
            document.getElementById('chat-box').innerHTML += `<div class="bot-message">Bot: ${data.response}</div>`;
            document.getElementById('chat-box').scrollTop = document.getElementById('chat-box').scrollHeight; // Scroll to bottom
        };
    </script>
</body>
</html>
styles.css
This file contains the CSS styles for the chat interface.

css
Copy code
/* Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

body {
    font-family: 'Roboto', Arial, sans-serif;
    background-color: #f5f5f5;
    margin: 0;
    padding: 0;
}

.chat-container {
    width: 600px;
    margin: 50px auto;
    background: white;
    border-radius: 12px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
    padding: 30px;
}

h1 {
    text-align: center;
    color: #333;
    margin-bottom: 30px;
}

.chat-box {
    display: flex;
    flex-direction: column;
    height: 400px;
    overflow-y: auto;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
    background-color: #f9f9f9;
}

.user-message, .bot-message {
    padding: 10px 15px;
    border-radius: 20px;
    margin-bottom: 10px;
    max-width: 70%;
    word-wrap: break-word;
    display: flex;
}

.user-message {
    background-color: #007bff;
    color: white;
    justify-content: flex-end;
    align-self: flex-end;
}

.bot-message {
    background-color: #28a745;
    color: white;
    justify-content: flex-start;
    align-self: flex-start;
}

#chat-form {
    display: flex;
    align-items: center;
}

#user-input {
    flex: 1;
    padding: 12px 20px;
    border: 1px solid #ddd;
    border-radius: 20px;
    font-size: 16px;
    background-color: #f9f9f9;
    transition: border-color 0.3s ease;
}

#user-input:focus {
    outline: none;
    border-color: #007bff;
}

button {
    padding: 12px 20px;
    border: none;
    background-color: #007bff;
    color: white;
    border-radius: 20px;
    cursor: pointer;
    font-size: 16px;
    margin-left: 10px;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #0056b3;
}

/* Scrollbar Styles */
.chat-box::-webkit-scrollbar {
    width: 8px;
}

.chat-box::-webkit-scrollbar-track {
    background-color: #f9f9f9;
}

.chat-box::-webkit-scrollbar-thumb {
    background-color: #007bff;
    border-radius: 4px;
}

chat-box::-webkit-scrollbar-thumb:hover {
    background-color: #0056b3;
}


Running the Project
Ensure you are in the project directory.


Activate your virtual environment:
bash
Copy code
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Run the Flask application:
bash
Copy code
python app.py
Open your web browser and go to http://127.0.0.1:5000 to interact with the chatbot.
Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

License
This project is free to use.

This README provides a detailed explanation of the project, including installation steps, usage, and descriptions of the main files. It should help users understand how to set up and run the project effectively.
