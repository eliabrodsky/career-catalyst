import streamlit as st
import google.generativeai as genai
import json

with st.sidebar:
    openai_api_key = st.text_input("Gemini API Key", key="chatbot_api_key", type="password")

st.title("💬 Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your Gemini API key to continue.")
        st.stop()
    genai.configure(api_key=openai_api_key)

    model = genai.GenerativeModel('gemini-pro')
    
    response = model.generate_content(st.session_state.messages).text
    st.session_state.messages.append(response)
    st.chat_message("assistant").write(response['content'])