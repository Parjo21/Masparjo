import os
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Set this environment variable with your BotFather token


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Respond to /start command."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Halo {user.mention_html()}! 👋\n"
        "Ketik /help untuk melihat perintah."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Respond to /help command with available commands."""
    commands = [
        "/start – salam pembuka",
        "/help – daftar perintah",
        "/echo <teks> – mengulang teks",
    ]
    await update.message.reply_text("\n".join(commands))


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Echo back user-supplied text after /echo command."""
    if context.args:
        await update.message.reply_text(" ".join(context.args))
    else:
        await update.message.reply_text("Kirim /echo <teks>")


def main() -> None:
    """Bot entry point."""
    if not BOT_TOKEN:
        raise RuntimeError("Isi variabel lingkungan BOT_TOKEN dulu.")

    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("echo", echo))

    # Start the bot with polling
    application.run_polling()


if __name__ == "__main__":
    main()