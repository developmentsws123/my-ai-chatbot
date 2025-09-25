import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up the page
st.title("🤖 My Smart AI Assistant")
st.write("Now with real ChatGPT power!")

# Get API key from .env file
api_key = os.getenv("OPENAI_API_KEY")

# Debug information
st.write(f"API key found: {api_key is not None}")
if api_key:
    st.write(f"Key starts with: {api_key[:10]}...")

if api_key:
    openai.api_key = api_key
    st.success("✅ API key loaded successfully!")
else:
    st.error("❌ API key not found. Please check your .env file")

# Simple chat
user_input = st.text_input("Ask me anything:")

if user_input and api_key:
    try:
        with st.spinner("AI is thinking..."):
            # Get AI response
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            
            ai_response = response.choices[0].message.content
            st.write(f"**You:** {user_input}")
            st.write(f"**AI:** {ai_response}")
            
    except Exception as e:
        st.error(f"Error: {e}")
elif user_input:
    st.warning("⚠️ Please set up your API key first")

    