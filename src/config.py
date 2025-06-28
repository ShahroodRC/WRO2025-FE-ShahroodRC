# config.py
# فایل تنظیمات کلی ربات: توکن، اطلاعات ادمین، فایل کاربران مجاز و لاگ

import os
from dotenv import load_dotenv

load_dotenv()  # بارگذاری متغیرهای محیطی از فایل .env

TOKEN = "7826545894:AAFtyOfmcZ8lMajt4lbrV46sTUVde7xnsGQ"  # توکن ربات از BotFather

USERS_FILE = "allowed_users.json"  # مسیر فایل لیست کاربران مجاز

ALL_USERS_FILE = "all_users.json"

ADMIN_USER_ID = 6080817675         # آیدی عددی ادمین اصلی (اجباری در لیست مجازها)

ADMIN_PASSWORD = "Sepehrleo1!"     # رمز عبور برای ورود موقت به حالت ادمین

ADMIN_TIMEOUT_SECONDS = 300        # مدت اعتبار حالت ادمین موقت به ثانیه (۵ دقیقه)

LOG_CHAT_ID = -1002657940872       # آیدی کانال یا گروهی که پیام‌های لاگ آنجا فرستاده می‌شوند