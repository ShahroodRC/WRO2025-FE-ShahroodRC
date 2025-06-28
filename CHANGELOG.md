# Changelog

All notable changes to this project will be documented in this file.

## [1.1.0] - 2025-06-29

### Added
- قابلیت ذخیره و به‌روزرسانی آمار پیام‌های کاربران در MySQL
- پشتیبانی از انواع خروجی‌های رسانه‌ای: عکس، ویدیو، گیف، صوت، استیکر و ...
- بهبود مدیریت دسترسی کاربران با استفاده از MySQL
- ثبت اطلاعات کاربران (پروفایل و عکس) در فولدر `logs/`
- بهبود ساختار داخلی برای توسعه آینده

### Changed
- تغییر نحوه ذخیره شمارش پیام‌ها از JSON به MySQL
- به‌روزرسانی دستورات دینامیکی ربات براساس وضعیت ادمین/کاربر
- بهبود خوانایی لاگ‌ها و مدیریت خطاهای دیتابیس

### Fixed
- اصلاح مشکل حذف و اضافه کاربران در لیست مجاز
- بهبود مدیریت اتصالات MySQL
- رفع مشکل ذخیره‌ی اطلاعات کاربر در صورت وجود اشکال در دیتابیس

---

## [1.0.0] - 2025-06-27 - Initial Release

### Added
- Initial release of the Telegram base bot
- User access control
- Admin login/logout
- Message handling
- Logging to group
- Versioning support