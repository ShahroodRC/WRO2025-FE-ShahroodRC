# bot_core.py
import os
import functools
import asyncio
import threading
import time
import hashlib
import logging
from datetime import datetime
from pathlib import Path

from telegram import Update, BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)
import main
import config
import mysql.connector
from mysql.connector import Error


# ساخت پوشه logs اگر وجود نداشته باشه
log_folder = Path("logs")
log_folder.mkdir(exist_ok=True)

# تنظیمات لاگ
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_folder / "app.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# غیرفعال کردن لاگ‌های بی‌دلیل httpx
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


def get_db_connection():
    try:
        conn = mysql.connector.connect(**config.MYSQL_CONFIG)
        return conn
    except Error as e:
        print(f"خطا در اتصال به MySQL: {e}")
        return None

allowed_users = []
temp_admins = {}  # user_id: last_active_timestamp


def save_message_counts(counts):
    conn = get_db_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        for user_id, count in counts.items():
            cursor.execute("""
                INSERT INTO message_counts (user_id, count)
                VALUES (%s, %s)
                ON DUPLICATE KEY UPDATE count = %s
            """, (user_id, count, count))
        conn.commit()
    except Error as e:
        print(f"خطا در ذخیره شمارش پیام‌ها: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

user_message_counts = {}

def load_message_counts():
    conn = get_db_connection()
    if not conn:
        return {}
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, count FROM message_counts")
        return {str(row[0]): row[1] for row in cursor.fetchall()}
    except Error as e:
        print(f"خطا در بارگذاری شمارش پیام‌ها: {e}")
        return {}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
user_message_counts = load_message_counts()

def save_allowed_users(user_list):
    conn = get_db_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        # حذف همه کاربران قبلی
        cursor.execute("DELETE FROM allowed_users")
        # اضافه کردن کاربران جدید
        for user_id in user_list:
            cursor.execute("INSERT IGNORE INTO allowed_users (user_id) VALUES (%s)", (user_id,))
        conn.commit()
    except Error as e:
        print(f"خطا در ذخیره کاربران مجاز: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def load_allowed_users():
    conn = get_db_connection()
    if not conn:
        print("اتصال به MySQL برقرار نشد. ادمین اصلی به صورت پیش‌فرض اضافه شد.")
        return [config.ADMIN_USER_ID]
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM allowed_users")
        users = [row[0] for row in cursor.fetchall()]
        if config.ADMIN_USER_ID not in users:
            users.append(config.ADMIN_USER_ID)
            save_allowed_users(users)
        return users
    except Error as e:
        print(f"خطا در بارگذاری کاربران مجاز: {e}")
        return [config.ADMIN_USER_ID]
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def check_all_users(user_id):
    conn = get_db_connection()
    if not conn:
        return False
    try:
        cursor = conn.cursor()

        # بررسی اینکه آیا کاربر وجود داره
        cursor.execute("SELECT user_id FROM all_users WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()

        is_new = result is None

        if is_new:
            # اگر کاربر جدید باشه، اضافه کن
            cursor.execute("INSERT IGNORE INTO all_users (user_id) VALUES (%s)", (user_id,))
            conn.commit()

        return is_new
    except Error as e:
        print(f"خطا در ثبت کاربر: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def is_admin(user_id):
    last_active = temp_admins.get(user_id)
    if user_id == config.ADMIN_USER_ID:
        return True
    if last_active and (time.time() - last_active < config.ADMIN_TIMEOUT_SECONDS):
        return True
    return False


ADMIN_COMMANDS = [
    BotCommand("start", "🟢 شروع کار با ربات"),
    BotCommand("help", "📘 راهنما"),
    BotCommand("adminlogin", "🔐 ورود به حالت ادمین موقت"),
    BotCommand("adminlogout", "🔓 خروج از حالت ادمین موقت"),
    BotCommand("add_user", "➕ اضافه کردن کاربر"),
    BotCommand("remove_user", "➖ حذف کاربر"),
    BotCommand("panel", "مشاهده لیست کاربران")
]

USER_COMMANDS = [
    BotCommand("start", "شروع کار با ربات"),
    BotCommand("help", "راهنما"),
    BotCommand("adminlogin", "ورود به حالت ادمین موقت"),
]


async def set_commands_for_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if is_admin(update.effective_user.id):
        await context.bot.set_my_commands(ADMIN_COMMANDS)
    else:
        await context.bot.set_my_commands(USER_COMMANDS)


def check_access(func):
    @functools.wraps(func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
        user_id = update.effective_user.id
        user_input = update.message.text if update.message else ''
        logger.info(f"پیام دریافت شد از کاربر {user_id}: {user_input}")

        user_id_str = str(user_id)
        user_message_counts[user_id_str] = user_message_counts.get(user_id_str, 0) + 1
        save_message_counts(user_message_counts)
        phone_number = "N/A"
        if update.message and update.message.contact:
            phone_number = update.message.contact.phone_number or "N/A"
        await save_user_info_and_photo(context, update.effective_user, phone_number=phone_number)

        if user_id in temp_admins:
            temp_admins[user_id] = time.time()

        if func.__name__ in ["add_user", "remove_user", "panel"]:
            if not is_admin(user_id):
                await log_message(update, context, 13)
                return

        else:
            if user_id not in allowed_users and not is_admin(user_id):
                await log_message(update, context, 42)
                return

        return await func(update, context, *args, **kwargs)

    return wrapper


async def save_user_info_and_photo(context: ContextTypes.DEFAULT_TYPE, user, phone_number="N/A"):
    try:
        user_id = user.id
        folder_path = Path("logs/users") / str(user_id)
        folder_path.mkdir(parents=True, exist_ok=True)

        info_path = folder_path / "info.txt"
        photos = await context.bot.get_user_profile_photos(user.id)

        with open(info_path, "w", encoding="utf-8") as f:
            f.write(f"ID: {user.id}\n")
            f.write(f"Name: {user.first_name} {user.last_name or ''}\n")
            f.write(f"Username: @{user.username or ''}\n")
            f.write(f"Language: {user.language_code or 'N/A'}\n")
            f.write(f"Is Bot: {'Yes' if user.is_bot else 'No'}\n")
            f.write(f"Phone Number: {phone_number}\n")
            f.write(f"Profile Photos Count: {photos.total_count}\n")

        # پوشه ذخیره عکس‌ها
        photos_folder = folder_path / "profile_photos"
        photos_folder.mkdir(exist_ok=True)

        # لیست فایل‌های موجود برای تشخیص شماره بعدی
        existing_files = [f for f in os.listdir(photos_folder) if f.startswith("profile_") and f.endswith(".jpg")]
        existing_numbers = [int(f.split("_")[1].split(".")[0]) for f in existing_files]
        next_number = max(existing_numbers, default=0) + 1

        # لیست hash‌های قدیمی برای مقایسه
        hashes_log = photos_folder / "photo_hashes.txt"

        # ذخیره فقط بزرگترین سایز از هر عکس
        if photos.total_count > 0:
            for photo_list in photos.photos:  # photo_list = یک ردیف از سایزهای مختلف
                largest_photo = photo_list[-1]  # آخرین عکس در ردیف = بزرگترین سایز

                photo_file = await context.bot.get_file(largest_photo.file_id)
                photo_path = photos_folder / f"profile_{next_number}.jpg"
                next_number += 1

                # محاسبه hash عکس برای جلوگیری از دانلود تکراری
                temp_path = photos_folder / f"temp_download.jpg"
                await photo_file.download_to_drive(str(temp_path))

                hash_sha256 = hashlib.sha256()
                with open(temp_path, "rb") as f:
                    for chunk in iter(lambda: f.read(4096), b""):
                        hash_sha256.update(chunk)
                file_hash = hash_sha256.hexdigest()

                # بررسی hash قبلی
                if hashes_log.exists():
                    with open(hashes_log, "r") as f:
                        existing_hashes = f.read().splitlines()
                    if file_hash in existing_hashes:
                        os.remove(temp_path)  # حذف عکس تکراری
                        continue

                # ذخیره hash جدید
                with open(hashes_log, "a") as f:
                    f.write(file_hash + "\n")

                # تغییر نام فایل به نام نهایی
                os.rename(temp_path, photo_path)

    except Exception as e:
        logger.error(f"خطا در ذخیره اطلاعات کاربر {user_id}: {e}", exc_info=True)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    if not is_admin(user_id):
        await query.edit_message_text("❌ شما اجازه دسترسی به این قسمت را ندارید.")
        return

    data = query.data
    allowed_users = context.bot_data.get('allowed_users', [])
    
    # گرفتن تمام کاربران از پوشه logs/users/
    all_user_dirs = [d for d in os.listdir("logs/users") if os.path.isdir(os.path.join("logs/users", d))]
    all_users_list = [int(uid) for uid in all_user_dirs]

    if data == "all_users":
        text = "👥 همه کاربران:\n\n"
        users = all_users_list
    elif data == "allowed_users":
        text = "✅ کاربران مجاز:\n\n"
        users = allowed_users
    else:
        text = "❓ نوع لیست ناشناخته است."
        users = []

    if not users:
        text += "کاربری یافت نشد."
    else:
        for idx, user_id in enumerate(users, start=1):
            try:
                info_path = Path("logs/users") / str(user_id) / "info.txt"
                if info_path.exists():
                    with open(info_path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        username_line = next((line for line in lines if line.startswith("Username:")), None)
                        username = username_line.split(": ")[1].strip() if username_line else ""
                    name_line = next((line for line in lines if line.startswith("Name:")), None)
                    name = name_line.split(": ")[1].strip() if name_line else ""

                    line = f"{idx}. {name}"
                    if username:
                        line += f" ({username})"
                    line += f" (ID: {user_id})\n"
                    text += line
                else:
                    text += f"{idx}. ID: {user_id}\n"
            except Exception as e:
                text += f"{idx}. ID: {user_id} (خطا: {e})\n"

    await query.edit_message_text(text.strip(), parse_mode='Markdown')
        

LOG_CHAT_ID = config.LOG_CHAT_ID

async def forward_message_to_log_group(context: ContextTypes.DEFAULT_TYPE, update: Update):
    forwarded_message = await context.bot.forward_message(
        chat_id=LOG_CHAT_ID,
        from_chat_id=update.effective_chat.id,
        message_id=update.message.message_id
    )
    return forwarded_message.message_id


@check_access
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    try:
        output = main.run_code(user_input)
    except Exception as e:
        output = f"خطا در اجرای کد: {e}"

    await log_message(update, context, output)

async def handle_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_message(update, context, 21)


async def log_message(update: Update, context: ContextTypes.DEFAULT_TYPE, output):
    user = update.effective_user
    user_id_str = str(user.id)
    user_msg_num = user_message_counts.get(user_id_str, 0)

    await handle_response(update, context, output)

    # ارسال به گروه لاگ
    forwarded_message_id = await forward_message_to_log_group(context, update)

    # جمع‌آوری اطلاعات
    first_name = user.first_name or ""
    last_name = user.last_name or ""
    username = f"@{user.username}" if user.username else ""
    phone_number = ""
    if update.message and update.message.contact:
        phone_number = update.message.contact.phone_number or ""

    log_text = f"""{output}

{'-' * 60}

کد کاربر: {user.id}
نام و نام خانوادگی: {first_name} {last_name}
یوزرنیم: {username}
شماره تلفن: {phone_number}
شماره پیام کاربر: {user_msg_num}
"""

    # ارسال به گروه لاگ
    try:
        await context.bot.send_message(
            chat_id=LOG_CHAT_ID,
            text=log_text,
            reply_to_message_id=forwarded_message_id
        )
    except Exception as e:
        logger.warning(f"خطا در ارسال لاگ به گروه: {e}")

    # ارسال به کنسول و فایل
    if isinstance(output, dict):
        logger.info(f"پاسخ داده شد: {output}")
    elif isinstance(output, str) and output.startswith("❌"):
        logger.warning(output)
    else:
        logger.info(output)

#async def handle_forward(context, chat_id, from_chat_id, message_ids):
#    for msg_id in message_ids:
#        await context.bot.copy_message(chat_id=chat_id, from_chat_id=from_chat_id, message_id=msg_id)


async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE, output):
    if not output:
        await log_message(update, context, 6)
        return None

    if isinstance(output, str):
        await update.message.reply_text(output)
        
    elif isinstance(output, dict):
        typee = output.get('type')
        data = output.get('data')

        if typee == 'forward':
            from_chat_id = output.get('from_chat_id')
            message_ids = output.get('message_ids', [])
            forward_type = output.get('forward_type', 'forward')

            for msg_id in message_ids:
                if forward_type == 'forward':
                    forwarded_message = await context.bot.forward_message(
                        chat_id=update.effective_chat.id,
                        from_chat_id=from_chat_id,
                        message_id=msg_id
                    )
                    return forwarded_message  # یا متنش رو برگردون

                elif forward_type == 'copy':
                    copied_message = await context.bot.copy_message(
                        chat_id=update.effective_chat.id,
                        from_chat_id=config.MESSAGE_SOURCE_CHAT_ID,
                        message_id=msg_id
                    )
                    return copied_message  # یا متنش رو برگردون

        elif typee == 'photo':
            if data:
                await update.message.reply_photo(data)
            else:
                await log_message(update, context, 34)

        elif typee == 'video':
            if data:
                await update.message.reply_video(data)
            else:
                await log_message(update, context, 33)

        elif typee == 'gif':
            if data:
                await update.message.reply_animation(data)
            else:
                await log_message(update, context, 32)

        elif typee == 'audio':
            if data:
                await update.message.reply_audio(data)
            else:
                await log_message(update, context, 31)
        
        elif typee == 'voice':
            if data:
                await update.message.reply_voice(data)
            else:
                await log_message(update, context, 30)
        
        elif typee == 'document':
            if data:
                await update.message.reply_document(data)
            else:
                await log_message(update, context, 29)
        
        elif typee == 'location':
            lat = output.get('latitude')
            lon = output.get('longitude')
            if lat is not None and lon is not None:
                await update.message.reply_location(latitude=lat, longitude=lon)
            else:
                await log_message(update, context, 28)
        
        elif typee == 'sticker':
            if data:
                await update.message.reply_sticker(data)
            else:
                await log_message(update, context, 27)
        
        elif typee == 'contact':
            phone = output.get('phone_number')
            first_name = output.get('first_name', '')
            last_name = output.get('last_name', '')
            if phone:
                await update.message.reply_contact(phone_number=phone, first_name=first_name, last_name=last_name)
            else:
                await log_message(update, context, 23)
        
        else:
            await log_message(update, context, 22)
    
    elif isinstance(output, int):
        await context.bot.copy_message(
                        chat_id=update.effective_chat.id,
                        from_chat_id=config.MESSAGE_SOURCE_CHAT_ID,
                        message_id=output
                    )
    else:
        await update.message.reply_text(str(output))


@check_access
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await set_commands_for_user(update, context)
    user = update.effective_user
    user_id = user.id

    # بررسی اینکه آیا کاربر قبلاً وجود دارد؟
    is_new_user = check_all_users(user_id)  # این تابع باید True/False برگردونه که کاربر جدید بوده

    try:
        if is_admin(user_id):
            await log_message(update, context, 7)
        else:
            if is_new_user:
                allowed_users.append(user_id)
                save_allowed_users(allowed_users)
                await log_message(update, context, 9)
            else:
                await log_message(update, context, 10)

    except Exception as e:
        await log_message(update, context, f"خطا در ارسال پیام شروع: {e}")


@check_access
async def add_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args or not args[0].isdigit():
        await log_message(update, context, 43)
        return

    new_user_id = int(args[0])
    if new_user_id in allowed_users:
        await log_message(update, context, f"کاربر با شناسه {new_user_id} قبلاً دسترسی دارد.")
    else:
        allowed_users.append(new_user_id)
        save_allowed_users(allowed_users)
        await log_message(update, context, f"کاربر با شناسه {new_user_id} به لیست مجازها اضافه شد.")


@check_access
async def remove_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args or not args[0].isdigit():
        await log_message(update, context, 44)
        return

    rem_user_id = int(args[0])
    if rem_user_id not in allowed_users:
        await log_message(update, context, f"کاربر با شناسه {rem_user_id} در لیست مجازها نیست.")
    else:
        allowed_users.remove(rem_user_id)
        save_allowed_users(allowed_users)
        await log_message(update, context, f"کاربر با شناسه {rem_user_id} از لیست مجازها حذف شد.")


@check_access
async def panel(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("همه کاربران", callback_data="all_users")],
        [InlineKeyboardButton("کاربران مجاز", callback_data="allowed_users")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("🔐 منو مدیریت:", reply_markup=reply_markup)


async def admin_login(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    args = context.args
    if not args:
        await log_message(update, context, 37)
        return
    password = args[0]
    if password == config.ADMIN_PASSWORD:
        temp_admins[user_id] = time.time()
        await log_message(update, context, 38)
        await set_commands_for_user(update, context)
    else:
        await log_message(update, context, 39)


async def admin_logout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in temp_admins:
        temp_admins.pop(user_id)
        await log_message(update, context, 40)
        await set_commands_for_user(update, context)
    else:
        await log_message(update, context, 41)


async def admin_timeout_task_loop():
    while True:
        now = time.time()
        to_remove = [uid for uid, last_active in temp_admins.items() if now - last_active > config.ADMIN_TIMEOUT_SECONDS]
        for uid in to_remove:
            temp_admins.pop(uid, None)
            print(f"ادمین موقت {uid} حذف شد به دلیل عدم فعالیت")
        await asyncio.sleep(60)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if is_admin(update.effective_user.id):
        await log_message(update, context, 11)
    else:
        await log_message(update, context, 12)



def start_background_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def run_bot(token):
    global allowed_users
    allowed_users = load_allowed_users()
    logger.info("ربات در حال اجراست...")

    app = ApplicationBuilder().token(token).build()

    # تنظیمات اولیه
    app.bot_data['allowed_users'] = load_allowed_users()
    app.bot_data['temp_admins'] = {}
    private_chat_filter = filters.ChatType.PRIVATE

    # ثبت دستورات
    app.add_handler(CommandHandler("start", start, filters=private_chat_filter))
    app.add_handler(CommandHandler("add_user", add_user, filters=private_chat_filter))
    app.add_handler(CommandHandler("remove_user", remove_user, filters=private_chat_filter))
    app.add_handler(CommandHandler("adminlogin", admin_login, filters=private_chat_filter))
    app.add_handler(CommandHandler("adminlogout", admin_logout, filters=private_chat_filter))
    app.add_handler(CommandHandler("help", help, filters=private_chat_filter))
    app.add_handler(CommandHandler("panel", panel, filters=private_chat_filter))

    app.add_handler(CallbackQueryHandler(button_handler))
    
    app.add_handler(MessageHandler(filters.Document.ALL | filters.VIDEO | filters.AUDIO | filters.PHOTO, handle_media))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND & private_chat_filter, handle_message))

    # راه‌اندازی async
    asyncio.run(app.run_polling())
