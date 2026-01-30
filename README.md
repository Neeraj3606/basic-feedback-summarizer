📊 Basic Feedback Summarizer (Generative AI)
A **FastAPI-based backend service** that uses **Generative AI** to analyze customer feedback and convert it into **clear, actionable business insights**.

This project demonstrates how **Generative AI can be integrated into backend APIs** to solve real-world business problems such as customer feedback analysis—without training any machine learning model.

---

## 🚀 Project Overview

Businesses receive a large volume of customer feedback, but manually analyzing it is time-consuming and inefficient.
This project automates the process by using **Generative AI** to:

* Summarize customer feedback
* Identify key themes and issues
* Analyze overall sentiment
* Suggest actionable improvements

The application exposes a clean **REST API** that can be easily integrated into existing systems.

---

## ✨ Features

* Accepts raw customer feedback text
* Generates a concise overall summary
* Extracts common themes (e.g., delivery, pricing, app issues)
* Performs basic sentiment analysis (Positive / Neutral / Negative)
* Suggests actionable improvement points
* RESTful API design
* Interactive API documentation using **Swagger UI**

---

## 🛠 Tech Stack

* **Python 3**
* **FastAPI** – backend framework
* **Uvicorn** – ASGI server
* **Pydantic** – data validation
* **REST API architecture**

---

## 📂 Project Structure

```text
.
├── main.py        # FastAPI application
├── README.md      # Project documentation
├── .gitignore     # Git ignore rules
└── venv/          # Virtual environment
```

---

## ▶️ How to Run Locally

Follow the steps below to run the project on your local machine.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Neeraj3606/basic-feedback-summarizer.git
cd basic-feedback-summarizer
```

---

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  
```

---

### 3️⃣ Install Dependencies

```bash
pip install fastapi uvicorn
```

---

### 4️⃣ Run the Server

```bash
uvicorn main:app --reload
```

---

### 5️⃣ Open API Documentation

Once the server is running, open your browser and visit:

```
http://127.0.0.1:8000/docs
```

Here you can test all API endpoints using Swagger UI.

---

## 🎯 Why This Project Is Useful

* Demonstrates **real-world Generative AI integration**
* Clean backend API design
* Beginner-friendly yet industry-relevant
* Suitable for:

  * Internships
  * Fresher roles
  * Backend development portfolios
  * AI-assisted systems

---

## 🧠 Learning Outcomes

* Building REST APIs with FastAPI
* Integrating Generative AI into backend services
* API request/response handling
* Clean project structuring
* Using Swagger UI for API testing

---

## 👤 Author

Neeraj Yadav
Backend Developer | Generative AI Enthusiast



