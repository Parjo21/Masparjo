#!/bin/bash

# Script untuk menjalankan bot Telegram
echo "🤖 Memulai Bot Telegram..."

# Aktivasi virtual environment
source venv/bin/activate

# Cek apakah file .env ada
if [ ! -f .env ]; then
    echo "❌ File .env tidak ditemukan!"
    echo "📝 Silakan copy .env.example ke .env dan isi BOT_TOKEN Anda"
    echo "   cp .env.example .env"
    echo "   nano .env"
    exit 1
fi

# Jalankan bot
echo "🚀 Bot sedang berjalan..."
python main.py