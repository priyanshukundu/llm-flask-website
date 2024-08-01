import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import time

# Load environment variables
load_dotenv()

# Initialize Azure OpenAI client (replace with your details)
client = AzureOpenAI(
    api_key='your_api_key',
    api_version="your_api_version",
    azure_endpoint='https://mbuaiplayground.openai.azure.com/'
)

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

def main():
  print("Welcome! Ask me anything or tell me a story, and I'll respond creatively.")
  while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
      break
    
    # Send user input to Azure OpenAI and get response
    response = get_response_from_azure_openai(user_input)
    print("Bard: " + response)
    time.sleep(1)  # Add a slight delay for a more natural flow

if __name__ == "__main__":
  main()

 # type: ignore