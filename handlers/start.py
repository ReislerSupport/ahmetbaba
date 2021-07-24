from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Merhaba👋 Telegram Gruplarının sesli sohbetlerinde müzik çalabiliyorum.
        Telegram gruplarının sesli sohbetlerinde müzik çalmamı ister misin?
        Beni nasıl kullanabileceğinizi öğrenmek için lütfen aşağıdaki
        '📜 Kullanım Kılavuzu 📜' düğmesini tıklayın.
        Grubunuzun sesli sohbetinde müzik çalabilmek için Asistanın grubunuzda olması gerekir.""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 Kullanım Kılavuzu 📜", url="https://t.me/avcilarbot")
                  ],[
                    InlineKeyboardButton(
                        "👨‍💻 Güncellemeler 👨‍💻", url="https://t.me/avcilarsupport"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Destek Grubu 🎙️", url="https://t.me/avcilarsupport"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("test") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🔴 Müzik Oynatıcı Aktif**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎙️ Destek Grubu 🎙️", url="https://t.me/avcilarsupport")
                ]
            ]
        )
   )
