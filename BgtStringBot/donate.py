import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("donate"))
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/942400d144776934cd402.jpg",
        caption=f"""**💥 المطور زين 🙂. كلمني لو عوزت حاجه.🌷**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♕︎ زيـﮯن آلهہ‏‏قر  ♕︎", url=f"https://t.me/devpokemon ")
                ]
                
           ]
        ),
    )
    