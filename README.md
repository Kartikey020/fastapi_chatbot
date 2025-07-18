# 🤖 Gemini Chatbot API (FastAPI)

A simple backend API using **FastAPI** and **Google Gemini Pro (gemini-2.5-pro)** to generate AI-powered responses for chatbot applications.

---

## 🚀 Features

- ✨ Uses Google's **Generative AI** (Gemini 2.5 Pro)
- ⚡ Built with **FastAPI** for high performance
- 🌐 **CORS-enabled** for frontend integration (e.g., React, Streamlit)
- 🧩 JSON-based input and output for easy integration

---

## 📁 Project Structure


---

## 📦 Installation

1. **Clone the repository**:

git clone https://github.com/yourusername/gemini-chatbot-fastapi.git
cd gemini-chatbot-fastapi
2.Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3.Install dependencies:
pip install -r requirements.txt
4.Set up your Gemini API key:
GEMINI_API_KEY=your_actual_gemini_api_key
5.Run the FastAPI server:
uvicorn main:app --reload

---

🛡️ CORS Note
CORS is currently set to allow all origins (allow_origins=["*"]) for development purposes. Update it for production use.

---

🧠 Credits
FastAPI

Google Generative AI (Gemini)
