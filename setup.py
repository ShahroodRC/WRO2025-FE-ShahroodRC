#setup.py
from setuptools import setup, find_packages

setup(
    name="telegram-base-bot",
    version="1.3.0",  # ← نسخه بروز شد
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "python-telegram-bot==20.0",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "run-bot=telegram_base_bot.start_bot:main",
        ],
    },
    author="Sepehr Yavarzadeh",
    description="A Telegram base bot with access control and message handler",
    url="https://github.com/yourusername/telegram-base-bot ",
)