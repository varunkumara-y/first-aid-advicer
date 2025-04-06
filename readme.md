# 🩹 First Aid Advisor
**Compare WHO Guidelines with GPT Suggestions**


First Aid Advisor is a user-friendly medical guidance app built with **Streamlit** and powered by **OpenAI GPT-3.5**. It allows users to describe a first aid situation and get instant, step-by-step advice from both official **WHO/Red Cross guidelines** and **AI-generated suggestions**.

---

## Features

### 🧠 Smart Guidance System
- Compare official first aid steps with AI-powered recommendations
- Uses keyword matching to find the most relevant WHO/Red Cross protocol
- Real-time response from GPT-3.5 for personalized advice

### 🩺 User-Friendly Input
- Natural language input for medical situations
- Clean, minimal UI with simple instructions
- Informative responses with clear formatting

### 📁 Local Data Integration
- Loads structured first aid protocols from a local `first_aid_data.json` file
- Customizable guideline data for flexibility or expansion

---

## Tech Stack

- **Frontend/UI**: Streamlit
- **AI Backend**: OpenAI GPT-3.5 via API
- **Environment Config**: python-dotenv
- **Data**: Local JSON (WHO/Red Cross guidelines)

---

## Getting Started

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/first-aid-advisor.git
cd first-aid-advisor
```

2. **Install Requirements**

```bash
pip install -r requirements.txt
```

3. **Set Your API Key**

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your-openai-api-key
```

4. **Add the First Aid Guidelines**

Ensure `first_aid_data.json` exists with content like:

```json
{
  "burn": {
    "keywords": ["burn", "fire", "scald"],
    "steps": [
      "Cool the burn under running water for at least 10 minutes.",
      "Remove any clothing or jewelry near the burn.",
      "Cover the burn with a clean, non-stick dressing."
    ]
  }
}
```

5. **Run the App**

```bash
streamlit run app.py
```

---

## Contributing

1. Fork the repository  
2. Create your feature branch (`git checkout -b feature/NewFeature`)  
3. Commit your changes (`git commit -m 'Add NewFeature'`)  
4. Push to the branch (`git push origin feature/NewFeature`)  
5. Open a Pull Request  

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- WHO & Red Cross for first aid guidance  
- [OpenAI](https://openai.com/) for GPT models  
- [Streamlit](https://streamlit.io/) for UI framework  

---

## Disclaimer

> ⚠️ This application is for **informational purposes only**.

