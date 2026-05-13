from flask import Flask, render_template, request, jsonify
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.text import TextTranslationClient

app = Flask(__name__)

# 🔑 Azure Credentials (REPLACE THESE)
LANGUAGE_KEY = "your language service key"
LANGUAGE_ENDPOINT = "your language service endpoint"

TRANSLATOR_KEY = "your translator service key"
TRANSLATOR_ENDPOINT = "https://api.cognitive.microsofttranslator.com"
TRANSLATOR_REGION = "region"   # e.g., "centralindia"

# 🧠 Language Service Client
text_client = TextAnalyticsClient(
    endpoint=LANGUAGE_ENDPOINT,
    credential=AzureKeyCredential(LANGUAGE_KEY)
)

# 🌍 Translator Client (FIXED)
translator_client = TextTranslationClient(
    endpoint=TRANSLATOR_ENDPOINT,
    credential=AzureKeyCredential(TRANSLATOR_KEY),
    region=TRANSLATOR_REGION
)

# 🏠 Home Route
@app.route('/')
def home():
    return render_template("index.html")

# 🔄 Summarize + Translate API
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data['text']
    language = data['language']

    try:
        # 🧠 Summarization
        poller = text_client.begin_extract_summary([text])
        result = poller.result()

        summary = ""
        for doc in result:
            for sentence in doc.sentences:
                summary += sentence.text + " "

        # 🌍 Translation (FIXED)
        translated = translator_client.translate(
            body=[{"text": summary}],
            to_language=[language]
        )

        final_text = translated[0].translations[0].text

        return jsonify({"summary": final_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ▶️ Run App
if __name__ == '__main__':
    app.run(debug=True)