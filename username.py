import streamlit as st
import openai
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key
def get_gpt4_response(question):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response['choices'][0]['message']['content']


def main():
    st.title("AI Prompt Engineer API")
    
    st.write("This API takes a username and a question, then returns a response using GPT-4 Turbo model.")
    
    username = st.text_input("Enter your username")
    question = st.text_area("Enter your question")
    
    if st.button("Get Response"):
        if username and question:
            with st.spinner('Generating response...'):
                response = get_gpt4_response(question)
            st.success("Response received!")
            st.write(f"**Username:** {username}")
            st.write(f"**Response:** {response}")
        else:
            st.error("Please provide both username and question.")

if __name__ == '__main__':
    main()
