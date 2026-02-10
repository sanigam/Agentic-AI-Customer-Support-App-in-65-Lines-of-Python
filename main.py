"""AI Learning Center Support - Streamlit Web Interface

A simple web UI for the multi-agent customer support system that:
- Accepts user questions about policies or general AI topics
- Extracts and displays the final answer from the agent response
"""

# Disable CrewAI telemetry to avoid signal-handler errors in Streamlit threads
import os
os.environ["OTEL_SDK_DISABLED"] = "true"

import streamlit as st # import streamlit for the web interface
from crew import support_crew # Import the crew we just built

st.title("AI Learning Center Support") # set the title of the web interface
query = st.text_input("Ask a question:") # set the input field for the user to enter a question

# If the user clicks the button and has entered a question, run the crew and display the result
if st.button("Get Answer") and query:
    with st.spinner("Processing..."):
        result = support_crew.kickoff(inputs={'user_query': query})
        st.markdown(result)