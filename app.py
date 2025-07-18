from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai

# ✅ Replace with your actual Gemini API key
genai.configure(api_key="AIzaSyCV_lpGMDIaShXM5i0ODC29H_zvXKmbhy0")

# ✅ Use Gemini Pro model
model = genai.GenerativeModel("gemini-2.5-pro")

app = FastAPI()

# ✅ Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Schema for request
class ChatRequest(BaseModel):
    messages: list

# ✅ Route to handle chat
@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        user_input = request.messages[-1]["content"]
        response = model.generate_content(user_input)
        return {"reply": response.text}
    except Exception as e:
        return {"reply": f"❌ Error from Gemini: {str(e)}"}
