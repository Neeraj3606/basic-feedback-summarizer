from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import os
import json

from sqlalchemy import create_engine, Column, Integer, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

from google import genai
from google.genai import types

# Load environment variables
load_dotenv()

# ---------- Database (SQLite) ----------
DB_URL = "sqlite:///./feedback.db"
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class FeedbackLog(Base):
    __tablename__ = "feedback_logs"
    id = Column(Integer, primary_key=True, index=True)
    feedback = Column(Text, nullable=False)
    result_json = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# ---------- FastAPI ----------
app = FastAPI(title="Customer Feedback Summarizer (Gemini)")

# CORS (frontend file:/// se bhi call ho sake)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Gemini Client ----------
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# ---------- Request Schema ----------
class FeedbackRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "ok", "message": "Feedback Summarizer API (Gemini) running"}

@app.post("/summarize")
def summarize_feedback(data: FeedbackRequest):
    prompt = f"""
You are a business analyst.
Analyze the customer feedback and return JSON with:
- summary (string)
- key_issues (array of strings)
- sentiment (one of: Positive, Neutral, Negative)
- actionable_suggestions (array of strings)

Customer feedback:
{data.text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            response_mime_type="application/json",
        ),
    )

    # response.text is JSON string
    try:
        result = json.loads(response.text)
    except Exception:
        result = {"raw": response.text}

    # Save to DB (ALWAYS)
    db = SessionLocal()
    try:
        db.add(
            FeedbackLog(
                feedback=data.text,
                result_json=json.dumps(result, ensure_ascii=False),
            )
        )
        db.commit()
    finally:
        db.close()

    return {"result": result}
@app.get("/history")
def history(limit: int = 20):
    db = SessionLocal()
    try:
        rows = db.query(FeedbackLog).order_by(FeedbackLog.id.desc()).limit(limit).all()
        return [
            {
                "id": r.id,
                "feedback": r.feedback,
                "result": json.loads(r.result_json),
                "created_at": r.created_at.isoformat()
            }
            for r in rows
        ]
    finally:
        db.close()
