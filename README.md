Flask Chatbot Project 
This project is a web-based chatbot built using Flask, designed to interact with users through a simple and intuitive interface. The chatbot utilizes Azure OpenAI for generating intelligent responses to user queries....

Project Overview
The project consists of the following files:

app.py: The core Flask application that sets up routes and handles interactions with Azure OpenAI.
code.py: A standalone script for interacting with the chatbot via the console.
index.html: The HTML file defining the web interface for the chatbot.
styles.css: The CSS file used to style the chatbot’s web interface.
Installation
To set up the project on your local machine, follow these steps:

Clone the Repository:

bash
Copy code
git clone https://github.com/priyanshukundu/llm-flask-website.git
cd llm-flask-website
Create and Activate a Virtual Environment:
This helps manage project dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Required Dependencies:
Ensure you have all necessary Python packages:

bash
Copy code
pip install -r requirements.txt
Configure Environment Variables:

Create a .env file in the root directory.
Add your Azure OpenAI credentials:
env
Copy code
API_KEY=your_api_key
AZURE_ENDPOINT=https://your-azure-endpoint.openai.azure.com/
Running the Project
To run the Flask application and interact with the chatbot:

Activate the Virtual Environment:

bash
Copy code
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Start the Flask Application:

bash 
Copy code
python app.py
Access the Chatbot:
Open your web browser and navigate to http://127.0.0.1:5000 to start interacting with the chatbot.

Project Structure
Here's a brief overview of the project structure:

..
Copy code
llm-flask-website/
├── static/
│   └── styles.css
├── templates/
│   └── index.html
├── app.py
├── code.py
├── requirements.txt
└── README.md
File Descriptions .
app.py: This file contains the Flask application setup, including route definitions and communication with the Azure OpenAI service. It handles user requests and sends them to Azure OpenAI for generating responses.

code.py: This script provides a command-line interface for interacting with the chatbot. It demonstrates how to send user queries to Azure OpenAI and display the responses.

index.html: This HTML file defines the structure and content of the chatbot’s web interface, including input and output sections.

styles.css: This CSS file styles the chatbot’s web interface, providing a user-friendly and visually appealing layout.

Contributing .
We welcome contributions to improve the project. If you have suggestions or enhancements, please fork the repository and create a pull request with your changes. Ensure that your changes are well-documented and tested.

License .
FREE TO USE : )       . . 

