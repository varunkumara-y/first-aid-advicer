import streamlit as st
import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

# Set up Streamlit UI first
st.set_page_config(
    page_title="🩹 First Aid Advisor",
    layout="centered",
    initial_sidebar_state="collapsed"
)

#backgrouncolor
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #f0f9ff, #cbebff);
    }
    </style>
""", unsafe_allow_html=True)


# Load environment variables
load_dotenv()

# Get API key from environment variable
GEMINI_API_KEY =st.secrets["GEMINI_API_KEY"] 

if not GEMINI_API_KEY:
    st.error("⚠️ Gemini API key not found. Please set up your secrets.toml file with GEMINI_API_KEY=your-key-here")
    st.stop()

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Create the main UI with simple styling
st.title("🩹 First Aid Advisor")
st.markdown("---")
st.markdown("### Describe your situation and get guidance from official medical sources **and** AI.")
st.markdown("---")

# Create a form for input with custom styling
with st.form("first_aid_form"):
    user_input = st.text_area(
        "What's happening?",
        placeholder="e.g., I cut my finger and it's bleeding.",
        height=100,
        help="Describe your medical situation in detail"
    )
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        submit_button = st.form_submit_button("🚑 Get Advice", use_container_width=True)

# Load WHO/Red Cross first aid data
@st.cache_data
def load_guidelines():
    with open("first_aid_data.json", "r") as f:
        return json.load(f)

guidelines = load_guidelines()

# Match user input to guideline keywords
def get_guideline_response(text):
    text_lower = text.lower()
    for condition, data in guidelines.items():
        if any(kw in text_lower for kw in data["keywords"]):
            # Return each step as a separate line with bullet points
            steps = []
            for i, step in enumerate(data["steps"], 1):
                steps.append(f"{i}. {step}")
            return "\n\n".join(steps)
    return "❗ Sorry, I couldn't find specific first aid steps for this situation. Please seek help."

# Get Gemini response
def get_gemini_response(text):
    try:
        # Set up the model
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        # Create the prompt
        prompt = f"""You are a certified first aid assistant providing accurate and concise first aid advice.
        
Someone says: '{text}'. What are the step-by-step first aid instructions?

Please provide clear, numbered steps that are easy to follow in an emergency situation."""
        
        # Generate the response
        response = model.generate_content(prompt)
        
        # Return the text from the response
        return response.text.strip()
    except Exception as e:
        return f"Gemini Error: {e}"

# Handle form submission
if submit_button:
    if not user_input:
        st.warning("Please describe the situation.")
    else:
        # WHO-based response
        st.markdown("---")
        st.subheader("📘 WHO/Red Cross Guidelines")
        with st.spinner("Analyzing..."):
            who_steps = get_guideline_response(user_input)
            st.success(who_steps)

        # Gemini-based response
        st.markdown("---")
        st.subheader("🤖 Gemini Advice")
        with st.spinner("Contacting Gemini..."):
            gemini_steps = get_gemini_response(user_input)
            st.info(gemini_steps)

# Disclaimer
st.markdown("---")
st.markdown("⚠️ *This tool is for informational purposes only. In case of emergency, call your local emergency number.*")