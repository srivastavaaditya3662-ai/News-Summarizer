# 📰 AI News Summarizer

An intelligent web application that summarizes news articles and translates them into multiple languages using Microsoft Azure Cognitive Services.

---

## 🚀 Features

- 🧠 Extractive summarization using Azure Language Service  
- 🌍 Multi-language translation using Azure Translator  
- 🎨 Modern dark-themed UI  
- ⚡ Fast Flask backend  
- 📋 Copy-to-clipboard functionality  

---

## 🧩 Technologies Used

- Python (Flask)
- HTML, CSS, JavaScript
- Microsoft Azure Language Service
- Microsoft Azure Translator

---

## 📁 Project Structure

news_summarizer/
│
├── app.py
├── requirements.txt
├── README.md
├── templates/
│ └── index.html
├── static/
│ └── style.css

## ⚙️ Setup Instructions

Install dependencies
pip install -r requirements.txt
Add Azure Credentials

Open app.py and replace:

LANGUAGE_KEY = "YOUR_LANGUAGE_KEY"
LANGUAGE_ENDPOINT = "YOUR_LANGUAGE_ENDPOINT"

TRANSLATOR_KEY = "YOUR_TRANSLATOR_KEY"
TRANSLATOR_REGION = "region"

Run the project
python app.py
Open in browser
http://127.0.0.1:5000/

## 🧠 How It Works

1. User enters news article
2. Azure Language Service generates summary
3. Azure Translator converts it into selected language
4. Output is displayed on UI
