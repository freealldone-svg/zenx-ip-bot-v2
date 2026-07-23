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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    add_user(update.effective_user.id)

    await update.message.reply_text(
        "👋 Welcome to ZENX IP BOT V2\n\n"
        "Select an option below:",
        reply_markup=MAIN_MENU,
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "deposit":
        await query.edit_message_text(
            "💳 Choose your deposit method:",
            reply_markup=DEPOSIT_MENU,
        )

    elif data == "buy_proxy":
        await show_proxy_menu(query)

    elif data == "balance":
        await show_balance(query)

    elif data == "orders":
        await show_orders(query)

    elif data == "support":
        await query.edit_message_text(
            f"📞 Support: @{SUPPORT_USERNAME}"
        )

    elif data == "back":
        await query.edit_message_text(
            "👋 Welcome back!",
            reply_markup=MAIN_MENU,
        )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("🤖 ZENX IP BOT is running...")
app.run_polling()
