# Create virtual environment
python -m venv venv

# Activate environment (Windows)
.\venv\Scripts\activate

# Activate environment (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install streamlit openai

# Save installed packages
pip freeze > requirements.txt

# Run Streamlit
streamlit run app.py
