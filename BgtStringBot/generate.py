from data import Data
from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from pyrogram1 import Client as Client1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from pyrogram1.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)


ask_ques = "**» • ذا كنـت تـريد تنـصيـب سـورس مـيوزك فـأختـار بـايـروجـرام\n• واذا تـريـد تنـصـيب التليثون فـأخـتار تيرمكـس\n• اذا كنـت سـورسـك مـتحـدث مـع اخـر تحديثات الـباروجـرام فا اخـتار بـايـروجـرام [New] \n• يوحد استخرجات جـلسـات لـي البـوتات :**"

buttons_ques = [
    [
        InlineKeyboardButton("🎙 بـايـࢪوجـࢪام 🎙", callback_data="pyrogram1"),
        InlineKeyboardButton("🎙 بـايـࢪوجـࢪام ᴠ2🎙", callback_data="pyrogram"),
    ],
    [
        InlineKeyboardButton("🎛 تـلـيـثـونـ 🎛", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("📟  بـايـࢪوجـࢪام بـوتـ  📟", callback_data="pyrogram_bot"),
        InlineKeyboardButton("🕹 تـلـيـثـونـ بـوتـ 🕹", callback_data="telethon_bot"),
    ],
]


@Client.on_message(filters.private & ~filters.forwarded & filters.command('generate'))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "Telethon"
    else:
        ty = "Pyrogram"
        if not old_pyro:
            ty += " v2"
    if is_bot:
        ty += " Bot"
    await msg.reply(f"⚡ ¦ بـدء إنـشـاء جـلسـة **{ty}**...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, '🎮حسنـا قم بأرسال الـ API_ID', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply('ال انت بعته غلط ♻️.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    api_hash_msg = await bot.ask(user_id, '» 🎮حسنـا قم بأرسال الـ API_HASH', filters=filters.text)
    if await cancelled(api_hash_msg):
        return
    api_hash = api_hash_msg.text
    if not is_bot:
        t = "» ✔️الان ارسل رقمك مع رمز دولتك , مثال :+201287585064 💥'"
    else:
        t = "sᴇɴᴅ ʏᴏᴜʀ `BOT_TOKEN` 🤖 \nʟɪᴋᴇ : `12345:bikashhalder` 🌷'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("»⬇️انتـظر لـحظـه سـوف نـرسـل كـود لحسابـك بالتليجـرام...")
    else:
        await msg.reply("ʟᴏɢɢɪɴɢ ᴀs ʙᴏᴛ ᴜsᴇʀ...")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        await msg.reply('`API_ID` ᴀɴᴅ `API_HASH` ᴄᴏᴍʙɪɴᴀᴛɪᴏɴ ɪs ɪɴᴠᴀʟɪᴅ🙂. ᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴛʀɪɴɢ ᴀɢᴀɪɴ⬅️.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply('`PHONE_NUMBER` ɪs ɪɴᴠᴀʟɪᴅ🙂. ᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴛʀɪɴɢ ᴀɢᴀɪɴ⬅️.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "https://telegra.ph/file/da1af082c6b754959ab47.jpg» 🔍من فضلك افحص حسابك بالتليجرام وتفقد الكود من حساب اشعارات التليجرام. إذا كان\n  هناك تحقق بخطوتين( المرور ) ، أرسل كلمة المرور هنا بعد ارسال كود الدخول بالتنسيق أدناه.- اذا كانت كلمة المرور او الكود  هي\n 12345 يرجى ارسالها بالشكل التالي 1 2 3 4 5 مع وجود مسـافـات بين الارقام اذا احتجت مساعدة @iiqllll.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply('تخطـيـﮯت آلمـدهہ‏‏ آلمـحددهہ‏‏🤣. حآول ♻️.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply('آلگود آلذيـﮯ آرسـلتهہ‏‏ خطـآ🙂. حآول مـجددآ♻️.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply('آلگود مـدهہ‏‏ آنتهہ‏‏ت🙂. حآول مـجددآ♻️.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = await bot.ask(user_id, 'حطـ آلبآسـورد بتآعگ💥. وبعديـﮯن يـﮯفضـل 🙂.', filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply('حآول بعد شـويـﮯهہ‏‏🙂. آعمـل آسـترت تنيـﮯ🥀.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                await two_step_msg.reply('آلبآسـورد غلطـ هہ‏‏نبدآ ننصـب حطـ آلبآسـ مـتخفشـ🙂.\n🥀 \nحآول تنيـﮯ🌻.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**{ty.upper()} آلجلسـهہ‏‏ 🥀** \n\n`{string_session}` \n\nبوت آلآسـتخرآج @str_12bot 🥀\n\n قنآ‏‏هہ آلسـورسـ @S_EG_P 🥀\n\nآلمـطـور زيـﮯن @devpokemon 🌺"
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "تمـ آسـتخرآج آلجلسـهہ‏‏ {} 💥. \n\nهہ‏‏تلآقيـﮯهہ‏‏آ فيـﮯ آلمـحفوظـآت👉! \n\nآلقآمـد [زيـﮯن آلهہ‏‏قر](https://t.me/devpokemon)  @S_EG_P 🌷".format("telethon" if telethon else "pyrogram"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("آلعمـليـﮯهہ‏‏ آنتهہ‏‏ت❎!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("تمـ آعآدهہ‏‏ تشـغيـﮯل آلبوت♻️!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("تمـت آنتهہ‏‏آء آلعمـليـﮯهہ‏‏❎!", quote=True)
        return True
    else:
        return False
