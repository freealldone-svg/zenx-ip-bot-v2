from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
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

    elif data.startswith("buy_"):
        await buy_proxy(query, data.replace("buy_", ""))

    elif data == "balance":
        await show_balance(query)

    elif data == "history":
        await show_orders(query)

    elif data == "support":
        await query.edit_message_text(
            f"📞 Support: @{SUPPORT_USERNAME}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="back")]
            ])
        )

    elif data == "back":
        await query.edit_message_text(
            "👋 Welcome back!",
            reply_markup=MAIN_MENU,
        )

async def show_balance(query):
    users = load_users()

    user_id = str(query.from_user.id)

    if user_id not in users:
        add_user(query.from_user.id)
        users = load_users()

    balance = users[user_id]["balance"]

    await query.edit_message_text(
        f"💰 Your Balance: ৳{balance}",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ])
    )


async def show_proxy_menu(query):
    keyboard = []

    for key, (name, price, filename) in PROXIES.items():
        keyboard.append([
            InlineKeyboardButton(
                f"{name} - ৳{price}",
                callback_data=f"buy_{key}"
            )
        ])

    keyboard.append([
        InlineKeyboardButton("🔙 Back", callback_data="back")
    ])

    await query.edit_message_text(
        "🛒 Choose a proxy:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def buy_proxy(query, proxy_key):
    await query.edit_message_text(
        f"🛒 You selected: {proxy_key}",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Back", callback_data="buy_proxy")]
        ])
    )


async def show_orders(query):
    await query.edit_message_text(
        "📜 You don't have any orders yet.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ])
    )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("🤖 ZENX IP BOT V2 is running...")
app.run_polling()
