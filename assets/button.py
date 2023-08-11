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
    BBMANAGE = InlineKeyboardMarkup(
                 [
                    InlineKeyboardButton(text="🔙 Kembali", callback_data="zel_manage"),
                 ]
                ])
    BMUSIC = InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="ᴘᴇʀɪɴᴛᴀʜ ᴀᴅᴍɪɴ", callback_data="zel_admin"),
                    InlineKeyboardButton(text="ᴘᴇʀɪɴᴛᴀʜ ʙᴏᴛ", callback_data="zel_bot"),
                 ],
                 [
                    InlineKeyboardButton(text="ᴘᴇʀɪɴᴛᴀʜ ᴘʟᴀʏ", callback_data="zel_play"),
                    InlineKeyboardButton(text="ᴘᴇʀɪɴᴛᴀʜ ᴇxsᴛʀᴀ", callback_data="zel_extra"),
                 ],
                 [
                    InlineKeyboardButton(text="«", callback_data="zel_back"),
                 ]
                ])
    BBMUSIC = InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="🔙 Kembali", callback_data="zel_music"),
                 ]
                ])
    BJASA = InlineKeyboardMarkup(
              [
                 [
                     InlineKeyboardButton("Admin", url="https://t.me/msdqqq")
                 ],
                 [
                    InlineKeyboardButton(text="«", callback_data="zel_back"),
                 ]
              ])
