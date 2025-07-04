# config.py
# فایل تنظیمات کلی ربات: توکن، اطلاعات ادمین، فایل کاربران مجاز و لاگ

import os

TOKEN = "7826545894:AAFtyOfmcZ8lMajt4lbrV46sTUVde7xnsGQ"  # توکن ربات از BotFather

ADMIN_USER_ID = 6080817675               # آیدی عددی ادمین اصلی (اجباری در لیست مجازها)

ADMIN_PASSWORD = "Sepehrleo1!"           # رمز عبور برای ورود موقت به حالت ادمین

ADMIN_TIMEOUT_SECONDS = 300              # مدت اعتبار حالت ادمین موقت به ثانیه (۵ دقیقه)

MESSAGE_SOURCE_CHAT_ID = -1002865825151  # آیدی گروه/کانال پیام‌ها (با منفی)

LOG_CHAT_ID = -1002657940872             # آیدی کانال یا گروهی که پیام‌های لاگ آنجا فرستاده می‌شوند


# تنظیمات MySQL
MYSQL_CONFIG = {
    "host": "localhost",
    "user": os.getenv("DB_USER", "base_bot_user"),
    "password": os.getenv("DB_PASSWORD", "sepehrleo"),
    "database": "base_bot"
}