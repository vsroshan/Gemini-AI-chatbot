from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure API key
api_key ="AIzaSyDV6Clj8NjObsX_cP0skqwCLpeytkuboKU"
if not api_key:
    raise ValueError("API key not found. Make sure 'GOOGLE_API_KEY' is set in your environment variables.")
genai.configure(api_key=api_key)

# Load Gemini Pro model
model = genai.GenerativeModel("gemini-pro")

# Function to get responses from the Gemini model
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Streamlit app setup
st.set_page_config(page_title="Gemini app ")
st.header("Roshan's AI")

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# When submit is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
