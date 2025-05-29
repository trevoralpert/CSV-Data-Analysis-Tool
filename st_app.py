import streamlit as st
from dotenv import load_dotenv
from utils import query_agent

load_dotenv()

st.title("Let's do some analysis on your CSV")
st.header("Please upload your CSV file here:")

data = st.file_uploader("Uploader CSV file", type="csv")

# Initialize conversation history in session state
if "history" not in st.session_state:
    st.session_state.history = []

# Chat input
user_input = st.text_input("You:", key="user_input")

if st.button("Send") and data is not None and user_input.strip() != "":
    # Add user message to history
    st.session_state.history.append({"role": "user", "content": user_input})

    # Build conversation context from last 5 exchanges
    context = ""
    for turn in st.session_state.history[-10:]:
        context += f"{turn['role'].capitalize()}: {turn['content']}\n"
    context += "Assistant:"

    # Get assistant response
    response = query_agent(data, context)
    st.session_state.history.append({"role": "assistant", "content": response})

# Display conversation
st.subheader("Conversation:")
for turn in st.session_state.history:
    if turn["role"] == "user":
        st.markdown(f"**You:** {turn['content']}")
    else:
        st.markdown(f"**Assistant:** {turn['content']}")
