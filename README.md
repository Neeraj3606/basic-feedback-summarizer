# Basic Feedback Summarizer (Generative AI)

A simple FastAPI-based backend service that summarizes customer feedback into
clear insights such as key themes, sentiment breakdown, and action items.

This project demonstrates how Generative AI systems can be integrated into
backend APIs for real-world business use cases like customer feedback analysis.

---

## 🚀 Features

- Accepts raw customer feedback text
- Generates an overall summary
- Extracts common themes (e.g. delivery, pricing, app issues)
- Performs basic sentiment analysis
- Suggests actionable improvements
- Interactive API documentation via Swagger UI

---

## 🛠 Tech Stack

- Python 3
- FastAPI
- Uvicorn
- Pydantic
- REST API

---

## 📂 Project Structure
```text
.
├── main.py
├── README.md
├── .gitignore
└── venv/
 ▶ How to Run Locally

1. Clone the repository
```bash
git clone https://github.com/Neeraj3606/basic-feedback-summarizer.git
## Navigate to the project folder
cd basic-feedback-summarizer
## Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
## Install dependencies
pip install fastapi uvicorn
##  Run the server
uvicorn main:app --reload
##. Open browser and visit
http://127.0.0.1:8000/docs


