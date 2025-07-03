import logging
import os
import requests
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')

class TelegramBot:
    def __init__(self):
        self.application = Application.builder().token(BOT_TOKEN).build()
        self.setup_handlers()
    
    def setup_handlers(self):
        """Setup all command and message handlers"""
        # Command handlers
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(CommandHandler("info", self.info))
        self.application.add_handler(CommandHandler("weather", self.weather))
        self.application.add_handler(CommandHandler("time", self.current_time))
        
        # Callback query handler for inline keyboards
        self.application.add_handler(CallbackQueryHandler(self.button_handler))
        
        # Message handler for regular text messages
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.echo))
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send a message when the command /start is issued."""
        user = update.effective_user
        
        # Create inline keyboard
        keyboard = [
            [InlineKeyboardButton("ℹ️ Info", callback_data='info')],
            [InlineKeyboardButton("🌤️ Cuaca", callback_data='weather')],
            [InlineKeyboardButton("🕒 Waktu", callback_data='time')],
            [InlineKeyboardButton("❓ Bantuan", callback_data='help')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        welcome_text = f"""
🤖 *Selamat datang {user.first_name}!*

Saya adalah bot Telegram yang siap membantu Anda.

*Fitur yang tersedia:*
• Informasi pengguna
• Cek cuaca
• Waktu saat ini
• Echo pesan

Gunakan tombol di bawah atau ketik /help untuk melihat semua perintah.
        """
        
        await update.message.reply_text(
            welcome_text,
            parse_mode='Markdown',
            reply_markup=reply_markup
        )
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send help message with available commands."""
        help_text = """
🤖 *Perintah yang tersedia:*

/start - Mulai bot dan lihat menu utama
/help - Tampilkan pesan bantuan ini
/info - Lihat informasi profil Anda
/weather <kota> - Cek cuaca (contoh: /weather Jakarta)
/time - Lihat waktu saat ini

*Fitur lain:*
• Kirim pesan apapun dan bot akan mengulanginya
• Gunakan tombol inline untuk navigasi cepat

💡 *Tips:* Semua perintah bisa diakses melalui menu utama di /start
        """
        
        await update.message.reply_text(help_text, parse_mode='Markdown')
    
    async def info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send user information."""
        user = update.effective_user
        chat = update.effective_chat
        
        info_text = f"""
👤 *Informasi Profil Anda:*

• *Nama:* {user.first_name}
• *Username:* @{user.username if user.username else 'Tidak ada'}
• *ID User:* `{user.id}`
• *Bahasa:* {user.language_code if user.language_code else 'Tidak diketahui'}
• *ID Chat:* `{chat.id}`
• *Tipe Chat:* {chat.type}

📅 *Waktu:* {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
        """
        
        await update.message.reply_text(info_text, parse_mode='Markdown')
    
    async def weather(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Get weather information for a city."""
        if not context.args:
            await update.message.reply_text(
                "❌ Silakan masukkan nama kota!\n\n"
                "Contoh: /weather Jakarta"
            )
            return
        
        city = ' '.join(context.args)
        
        try:
            # Simple weather API call (you can replace with a real weather API)
            # For demo purposes, this is a mock response
            weather_text = f"""
🌤️ *Cuaca di {city.title()}:*

• *Kondisi:* Cerah berawan
• *Suhu:* 28°C
• *Kelembaban:* 65%
• *Angin:* 10 km/h

📍 *Catatan:* Ini adalah data contoh. Untuk data cuaca real-time, 
integrasikan dengan API seperti OpenWeatherMap.
            """
            
            await update.message.reply_text(weather_text, parse_mode='Markdown')
            
        except Exception as e:
            logger.error(f"Error getting weather: {e}")
            await update.message.reply_text(
                "❌ Maaf, terjadi kesalahan saat mengambil data cuaca."
            )
    
    async def current_time(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send current time."""
        current_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        await update.message.reply_text(
            f"🕒 *Waktu saat ini:*\n{current_time}",
            parse_mode='Markdown'
        )
    
    async def echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Echo the user message."""
        user_message = update.message.text
        
        # Add some fun responses
        if "halo" in user_message.lower() or "hai" in user_message.lower():
            response = f"👋 Halo juga! Anda berkata: '{user_message}'"
        elif "terima kasih" in user_message.lower():
            response = f"🙏 Sama-sama! Pesan Anda: '{user_message}'"
        elif "selamat" in user_message.lower():
            response = f"✨ Selamat juga! Anda berkata: '{user_message}'"
        else:
            response = f"📝 Anda berkata: '{user_message}'"
        
        await update.message.reply_text(response)
    
    async def button_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle inline keyboard button presses."""
        query = update.callback_query
        await query.answer()
        
        if query.data == 'info':
            user = query.from_user
            chat = query.message.chat
            
            info_text = f"""
👤 *Informasi Profil Anda:*

• *Nama:* {user.first_name}
• *Username:* @{user.username if user.username else 'Tidak ada'}
• *ID User:* `{user.id}`
• *Bahasa:* {user.language_code if user.language_code else 'Tidak diketahui'}
• *ID Chat:* `{chat.id}`

📅 *Waktu:* {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
            """
            
            await query.edit_message_text(info_text, parse_mode='Markdown')
            
        elif query.data == 'weather':
            weather_text = """
🌤️ *Informasi Cuaca:*

Untuk cek cuaca, gunakan perintah:
`/weather <nama_kota>`

Contoh: `/weather Jakarta`

📍 *Catatan:* Fitur ini bisa diintegrasikan dengan API cuaca real-time.
            """
            await query.edit_message_text(weather_text, parse_mode='Markdown')
            
        elif query.data == 'time':
            current_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            time_text = f"🕒 *Waktu saat ini:*\n{current_time}"
            await query.edit_message_text(time_text, parse_mode='Markdown')
            
        elif query.data == 'help':
            help_text = """
🤖 *Perintah yang tersedia:*

/start - Mulai bot dan lihat menu utama
/help - Tampilkan pesan bantuan
/info - Lihat informasi profil Anda
/weather <kota> - Cek cuaca
/time - Lihat waktu saat ini

*Fitur lain:*
• Kirim pesan apapun dan bot akan mengulanginya
• Gunakan tombol inline untuk navigasi cepat
            """
            await query.edit_message_text(help_text, parse_mode='Markdown')
    
    def run(self):
        """Start the bot."""
        logger.info("Starting bot...")
        self.application.run_polling()

def main():
    """Main function to run the bot."""
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN tidak ditemukan! Pastikan file .env sudah dibuat.")
        return
    
    bot = TelegramBot()
    
    try:
        bot.run()
    except Exception as e:
        logger.error(f"Error running bot: {e}")

if __name__ == '__main__':
    main()