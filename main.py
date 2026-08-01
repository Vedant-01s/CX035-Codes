from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
from google import genai

# Initialize the API
app = FastAPI(title="Supermarket AI Backend")

# Allow your teammate's frontend to bypass security blocks (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the dataset once when the server starts
df = pd.read_csv('Supermarket_Dashboard_ML_Dataset.csv')

# Define what the frontend will send to the AI
class AIRequest(BaseModel):
    user_query: str

# ---------------- ENDPOINTS ----------------

@app.get("/api/kpis")
def get_kpis():
    """Sends the basic numbers to the frontend."""
    return {
        "total_revenue": float(df['Revenue'].sum()),
        "total_profit": float(df['Profit'].sum()),
        "total_items_sold": int(df['Quantity_Sold'].sum())
    }

@app.post("/api/consultant")
def ask_ai(request: AIRequest):
    """Takes a question from the frontend, asks Gemini, and returns the answer."""
    # IMPORTANT: Put your actual Gemini API key inside these quotes
    api_key = "AQ.Ab8RN6LUm1IBNVefocAgef9yzoWYpu8eHTwZ54Yv7sz3ZXjqTg" 
    
    client = genai.Client(api_key=api_key)
    
    prompt = f"""
    You are a retail consultant advising an Indian supermarket. 
    Total Store Revenue: ₹{df['Revenue'].sum()}
    The shop owner asks: "{request.user_query}"
    Provide a highly actionable, 3-bullet point strategy. Use Indian Rupees (₹).
    """
    
    response = client.models.generate_content(
        model='gemini-3.5-flash',
        contents=prompt
    )
    
    return {"ai_response": response.text}