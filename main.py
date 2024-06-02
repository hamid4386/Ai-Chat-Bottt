import os
import google.generativeai as genai
import streamlit as st

# Configure the Gemini AI API key
genai.configure(api_key='AIzaSyDTxcE6_Z6W-U9_NnACOd81KqHM8dcLV84')

# Create the Gemini AI model
generation_config = {
  "temperature": 0.5,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

# Create the Streamlit UI
st.title("Gemini AI Chatbot")

# User input
user_input = st.text_area("Type your message here:", height=200)

# Button to send the message
if st.button("Send"):
    if user_input:
        # Create a new chat session
        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [user_input],
                }
            ]
        )
        
        # Get the response from the Gemini AI chatbot
        response = chat_session.send_message(user_input)
        
        # Display the response in the Streamlit UI
        st.write(f"Hamid AI Chatbot: {response.text}")