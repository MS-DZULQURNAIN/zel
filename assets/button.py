from pyrogram.types import *
from zeldris import BOT_USERNAME

class BUTTON:
    BMANAGE = InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="💁🏻‍♂Perintah Dasar", callback_data="zel_dasar"),
                    InlineKeyboardButton(text="Lanjutan🙋🏻‍♂", callback_data="zel_lanjut"),
                 ],
                 [
                    InlineKeyboardButton(text="🕵🏻Ahli", callback_data="zel_ahli"),
                    InlineKeyboardButton(text="Panduan Pro💆🏻‍♂", callback_data="zel_pro"),
                 ],
                 [
                    InlineKeyboardButton(text="➕ Panduan Lengkap ➕", url=f"http://t.me/{BOT_USERNAME}?start=help"),
                 ],
                 [
                    InlineKeyboardButton(text="🔙 Kembali", callback_data="zel_back"),
                 ]
                ])
