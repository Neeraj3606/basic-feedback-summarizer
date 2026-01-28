from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class FeedbackIn(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "ok", "message": "Feedback Summarizer API running"}

@app.post("/summarize")
def summarize(data: FeedbackIn):
    text = data.text.strip()
    if not text:
        return {"error": "Empty feedback"}

    # Abhi demo response (AI connect baad me)
    return {
        "overall_summary": "Demo summary: customers are talking about delivery, pricing, and app issues.",
        "themes": ["Delivery", "Pricing", "App Bugs"],
        "sentiment": {"positive": 2, "neutral": 1, "negative": 2},
        "action_items": [
            "Improve delivery ETA accuracy",
            "Review pricing complaints",
            "Fix checkout / login bugs"
        ]
    }


