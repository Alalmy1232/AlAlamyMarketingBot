from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    print("Error: BOT_TOKEN not found in environment variables.")
    exit(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 مرحبًا بك في بوت *العالمي للتسويق*!\n"
        "📦 عروض حصرية ومميزة\n"
        "💸 أسعار تنافسية\n"
        "📞 للتواصل معنا:\n"
        "🔗 صفحتنا على التليجرام: @YourPageHere",
        parse_mode="Markdown"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("✅ البوت يعمل الآن...")
app.run_polling()
