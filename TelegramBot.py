import os
import logging
import fitz  # PyMuPDF for extracting text from PDFs
import httpx
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from google.generativeai import configure, GenerativeModel

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Google Gemini AI
configure(api_key=GEMINI_API_KEY)
gemini_model = GenerativeModel("gemini-1.5-flash")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Store user language preferences
user_languages = {}


# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = "\n".join([page.get_text("text") for page in doc])
        return text
    except Exception as e:
        logger.error(f"Error extracting text from PDF: {e}")
        return ""


# Function to split long messages into multiple parts
def split_text(text, chunk_size=4000):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


# Start command - Asks user to choose a language
async def start(update: Update, context: CallbackContext):
    keyboard = [["English", "Hindi"], ["Marathi", "Bengali"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text("🌍 Choose your preferred language:", reply_markup=reply_markup)


# Handle language selection
async def set_language(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    selected_language = update.message.text.strip()

    if selected_language in ["English", "Hindi", "Marathi", "Bengali"]:
        user_languages[chat_id] = selected_language
        await update.message.reply_text(f"✅ Language set to {selected_language}!")
    else:
        await update.message.reply_text("❌ Please choose a valid language from the options.")


# Handle PDF document upload
async def handle_document(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    file = await update.message.document.get_file()
    file_path = f"{file.file_id}.pdf"

    # Download file
    await file.download_to_drive(file_path)

    text = extract_text_from_pdf(file_path)
    os.remove(file_path)  # Cleanup after processing

    if text.strip():
        language = user_languages.get(chat_id, "English")  # Default to English
        response = gemini_model.generate_content(f"Respond in {language}. {text[:2000]}")

        # Send message in chunks
        response_texts = split_text(response.text)
        for part in response_texts:
            await update.message.reply_text(f"📄 PDF Analysis ({language}):\n\n{part}")
    else:
        await update.message.reply_text("❌ Could not extract text from the PDF.")


# Main function to run the bot
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, set_language))  # Handle language selection
    app.add_handler(MessageHandler(filters.Document.MimeType("application/pdf"), handle_document))

    logger.info("Bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()
