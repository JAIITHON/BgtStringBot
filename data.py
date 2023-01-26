from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("💥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ 💥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 آرجع 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("🌷 قنآ‏‏هہ آلسـورسـ 🌷", url="https://t.me/S_EG_P")],
        [
            InlineKeyboardButton("🌸 مـسـآعد‏‏هہ 🌸", callback_data="help"),
            InlineKeyboardButton("🎪 حول آلبوت 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("💥 بآر  💥", url="https://t.me/GRO_UP_1")],
    ]

    START = """
مـنور يـﮯزمـگسـ {}

📟¦اهلا بـك عزيـزي 📬
⚡¦يـمكنك استـخـراج الـتـالـي
♻️¦تيرمـكـس تليثون للحسـابـات🏂
♻️¦تيرمـكـس تليثون للبوتــات🤖
🎧¦بايـروجـرام مـيوزك للحسابات🙋🏼‍♂️
🗽¦بايـروجـرام مـيوزك احدث اصدار🎊
🎧¦بايـروجـرام مـيوزك للبوتات🤖
- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل سـورس اغــاني تم انشـاء هـذا البـوت بواسطـة
    """

    HELP = """
💥 **ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs** 💥

/about -  حول بوت جلسـآت گرسـتيـﮯن...      🌷
/cancel - لآغلآق آلنآفذ‏‏هہ آلحآليـﮯهہ‏‏ 🌷
/donate - لمـعرف‏‏هہ مـطـور آلسـورسـ 🌷
/help -   لمـعرف‏‏هہ آلمـزيـﮯد مـن آلآوآمـر.....    🌷 
/generate - لآسـتخرآج جلسـ‏‏هہ....   🌷
/restart - لآعآد‏‏هہ تشـغيـﮯل آلبوت. 🌷
/start - لعمـل آسـترت للبوت....    🌷
"""

    ABOUT = """
**حول بوت جلسـآت سـورسـ گرسـتيـﮯن** 

آلبوت دهہ‏‏ لآسـتخرآج جلسـآت . @S_EG_P 🌷 آلمـطـوريـﮯن @devpokemon @cr_criss

جروب الدعم : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/GRO_UP_1)

المطور زين : [dev pⓞкє๓๏ภ](https://t.me/devpokemon)

المطور بارلو : [ȡέν ВάŕĻό](https://t.me/bar_lo0o0)


    """
