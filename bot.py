from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import *
from database import *
from admin import *
from proxy import *

import json
import os

PROXIES = {
    "owl": ("🦉 Owl IP", 9, "owl.txt"),
    "abc": ("🔵 ABC IP", 255, "abc.txt"),
    "rocket": ("🚀 Rocket IP", 160, "rocket.txt"),
    "rapid": ("⚡ Rapid IP", 127, "rapid.txt"),
    "datamplus": ("🌐 Datamplus", 150, "datamplus.txt"),
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    add_user(update.effective_user.id)

    keyboard = [
        [
            InlineKeyboardButton("💰 My Balance", callback_data="balance"),
            InlineKeyboardButton("🛒 Buy Proxy", callback_data="buy"),
        ],
        [
            InlineKeyboardButton("💳 Deposit", callback_data="deposit"),
            InlineKeyboardButton("📜 Order History", callback_data="history"),
        ],
        [
            InlineKeyboardButton("📞 Support", callback_data="support"),
        ],
    ]

    await update.message.reply_text(
        "👋 Welcome to ZENX IP BOT V2\n\n"
        "Select an option below:",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

MAIN_MENU = InlineKeyboardMarkup([
    [InlineKeyboardButton("💳 Deposit", callback_data="deposit")],
    [InlineKeyboardButton("🛒 Buy Proxy", callback_data="buy_proxy")],
    [InlineKeyboardButton("💰 My Balance", callback_data="balance")],
    [InlineKeyboardButton("📜 Order History", callback_data="history")],
    [InlineKeyboardButton("📞 Support", callback_data="support")],
])
