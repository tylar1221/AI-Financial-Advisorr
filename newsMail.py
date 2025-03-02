from flask import Flask, request, render_template, jsonify
import json
import smtplib
import feedparser
import google.generativeai as genai
from deep_translator import GoogleTranslator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
import threading
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load Environment Variables
load_dotenv()
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

# RSS Feed URL for Small Business Schemes
RSS_FEED_URL = "https://news.google.com/rss/search?q=small+business+schemes+by+government&hl=en-IN&gl=IN&ceid=IN:en"
USER_FILE = "users.json"
file_lock = threading.Lock()

# Load users from JSON
def load_users():
    if not os.path.exists(USER_FILE):
        return []
    with open(USER_FILE, "r") as file:
        return json.load(file)

# Save users safely
def save_users(users):
    with file_lock:
        with open(USER_FILE, "w") as file:
            json.dump(users, file, indent=4)

# Summarize text using Gemini API
def summarize_text(text):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(text)
        return response.text if response and hasattr(response, "text") else "Summary not available."
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "Summary not available due to an error."

# Translate text
def translate_text(text, dest_lang):
    try:
        return GoogleTranslator(source="auto", target=dest_lang).translate(text)
    except Exception as e:
        print(f"Translation Error: {e}")
        return text

# Fetch and translate news
def fetch_news(user_lang):
    feed = feedparser.parse(RSS_FEED_URL)
    news_items = []
    for entry in feed.entries[:5]:
        summary = summarize_text(entry.title + " " + getattr(entry, "summary", ""))
        if user_lang != "en":
            summary = translate_text(summary, user_lang)
        news_items.append(f"<b>{entry.title}</b><br>{summary}<br><a href='{entry.link}'>Read more</a><br><br>")
    return "".join(news_items)


# Send email with translated news
def send_email(to_email, language):
    news_content = fetch_news(language)
    if not news_content:
        return

    # Custom message to be added at the end of the email
    footer_message = """
    <hr>
    <p style="color: gray; font-size: 12px;">
        This is an automated email providing daily updates on government schemes for small businesses. 
        Call 1930 for any cyber related issues .
    </p>
    """

    # Append the footer message to the news content
    email_content = news_content + footer_message

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = "Daily Small Business Schemes Update"
    msg.attach(MIMEText(email_content, "html"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()
        print(f"Email sent to {to_email} in {language}.")
    except Exception as e:
        print(f"Error sending email to {to_email}: {str(e)}")


# Schedule emails
def schedule_emails():
    users = load_users()
    schedule.clear()
    for user in users:
        schedule.every().day.at(user["time"]).do(send_email, to_email=user["email"], language=user["language"])
    print("Scheduled emails updated.")

# Run scheduler in background
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)

threading.Thread(target=run_scheduler, daemon=True).start()

# Flask routes
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email, time, language = request.form["email"], request.form["time"], request.form["language"]
        users = load_users()
        for user in users:
            if user["email"] == email:
                user["time"], user["language"] = time, language
                break
        else:
            users.append({"email": email, "time": time, "language": language})
        save_users(users)
        schedule_emails()
        return jsonify({"message": "Email scheduled successfully!"})
    return render_template("index.html")

if __name__ == "__main__":
    schedule_emails()
    app.run(debug=True)
