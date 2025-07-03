# 🤖 Telegram Bot Indonesia

Bot Telegram yang dibuat dengan Python menggunakan library `python-telegram-bot`. Bot ini memiliki berbagai fitur menarik dan mudah dikustomisasi.

## ✨ Fitur

- 🎯 **Perintah Dasar**: `/start`, `/help`, `/info`
- 🌤️ **Cuaca**: Cek informasi cuaca kota (template, bisa diintegrasikan dengan API cuaca)
- 🕒 **Waktu**: Lihat waktu saat ini
- 💬 **Echo**: Bot akan mengulangi pesan yang Anda kirim
- ⌨️ **Inline Keyboard**: Menu interaktif dengan tombol
- 📱 **Responsive**: Interface yang user-friendly

## 🚀 Cara Setup

### 1. Buat Bot Telegram

1. Buka Telegram dan cari `@BotFather`
2. Ketik `/newbot` untuk membuat bot baru
3. Ikuti instruksi untuk memberi nama dan username bot
4. Simpan **Bot Token** yang diberikan

### 2. Install Dependencies

```bash
# Masuk ke folder bot
cd telegram-bot

# Install Python dependencies
pip install -r requirements.txt
```

### 3. Konfigurasi Environment

```bash
# Copy file example ke .env
cp .env.example .env

# Edit file .env dan masukkan Bot Token Anda
nano .env
```

Isi file `.env`:
```
BOT_TOKEN=123456789:AAEhBOweik6ad6PsupN9x15zD_CqR1XYZ7w
```

### 4. Jalankan Bot

```bash
python main.py
```

Bot akan mulai berjalan dan menunggu pesan!

## 📱 Cara Menggunakan

### Perintah yang Tersedia:

- `/start` - Mulai bot dan lihat menu utama
- `/help` - Tampilkan daftar perintah
- `/info` - Lihat informasi profil Anda
- `/weather <nama_kota>` - Cek cuaca (contoh: `/weather Jakarta`)
- `/time` - Lihat waktu saat ini

### Menu Interaktif:

Bot dilengkapi dengan inline keyboard yang memudahkan navigasi. Cukup ketik `/start` untuk melihat menu utama.

## 🛠️ Kustomisasi

### Menambah Perintah Baru

1. Buat fungsi baru di class `TelegramBot`:

```python
async def my_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Deskripsi perintah baru."""
    await update.message.reply_text("Respon perintah baru!")
```

2. Tambahkan handler di method `setup_handlers()`:

```python
self.application.add_handler(CommandHandler("mycommand", self.my_command))
```

### Integrasi API Cuaca Real

Untuk menggunakan data cuaca real-time:

1. Daftar di [OpenWeatherMap](https://openweathermap.org/api)
2. Tambahkan API key ke file `.env`:
   ```
   WEATHER_API_KEY=your_api_key_here
   ```
3. Modifikasi fungsi `weather()` untuk menggunakan API

## 📂 Struktur File

```
telegram-bot/
├── main.py              # File utama bot
├── requirements.txt     # Dependencies Python
├── .env.example        # Template konfigurasi
├── .env               # Konfigurasi (tidak di-commit)
└── README.md          # Dokumentasi ini
```

## 🔧 Development

### Logging

Bot sudah dilengkapi dengan logging system. Log akan muncul di console saat bot berjalan.

### Error Handling

Bot memiliki error handling dasar. Untuk production, disarankan menambah:
- Database untuk menyimpan data user
- Rate limiting
- Admin commands
- Monitoring system

## 🚀 Deployment

### Option 1: VPS/Server

1. Upload code ke server
2. Install dependencies
3. Setup environment variables
4. Jalankan dengan `nohup python main.py &`

### Option 2: Heroku

1. Buat `Procfile`:
   ```
   worker: python main.py
   ```
2. Deploy ke Heroku
3. Set environment variables di Heroku dashboard

### Option 3: Railway/Render

1. Connect repository
2. Set environment variables
3. Deploy otomatis

## 📝 Catatan

- Bot ini menggunakan **polling mode** (bukan webhook)
- Cocok untuk development dan bot skala kecil-menengah
- Untuk production besar, pertimbangkan menggunakan webhook mode

## 🤝 Kontribusi

Silakan buat pull request atau issue jika ingin berkontribusi!

## 📄 Lisensi

MIT License - silakan gunakan untuk project pribadi atau komersial.

---

**Happy Coding! 🎉**