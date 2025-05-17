##-----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
import os
from pyrogram import Client, filters, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.types import CallbackQuery
from config import *
import requests
from PIL import Image, ImageDraw, ImageFont
import asyncio, time
from random import choice
from datetime import datetime
import logging
import sys

FORMAT = "[LEGEND-MUKESH] %(message)s"
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

StartTime = time.time()
Mukesh = Client(
    "chat-gpt",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

START = """
๏ 𝗠𝗲𝗿𝗵𝗮𝗯𝗮 🌹

MERHABA BEN DEEPSEEK İLE TASARLANAN DOSYA KUYUMCUSU VE FOTOĞRAF EDİTÖRÜYÜM!

✨ Özelliklerim:
- Fotoğraf Efektleri (Sepia, Siyah-Beyaz)
- LOGO TASARIM

Powered by Deepseek 🌿🍻❤️
"""

SOURCE = "https://github.com/ViosRio/RoxyTrans"
SOURCE_TEXT = "Kaynak Kod: GitHub"

x = ["❤️", "🎉", "✨", "🪸", "🎈", "🎯"]
g = choice(x)

MAIN = [
    [InlineKeyboardButton("sᴀʜɪᴘ", url=f"https://t.me/{OWNER_USERNAME}")],
    [
        InlineKeyboardButton(
            "ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton("ʏᴀʀᴅıᴍ & ᴋᴏᴍᴜᴛʟᴀʀ", callback_data="HELP")],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            "ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton("ᴅᴇsᴛᴇᴋ", url=f"https://t.me/{SUPPORT_GRP}")],
]

HELP_READ = """
**📌 Kullanım Kılavuzu**

✨ **Fotoğraf Efektleri**:
• `/sephia` - Fotoğrafa Sepia efekti uygular
• `/bw` - Siyah-Beyaz yapar
• `/enhance` - Fotoğrafı netleştirir
• `/real` - Gerçekçi renk efekti

❤️ **Logo Fasarım**
• `/logo` - Logo Tasarım İsim Şenlik

**Powered by Deepseek 🌿🍻❤️**
"""

HELP_BACK = [
    [InlineKeyboardButton("ᴋᴀʏɴᴀᴋ", url=SOURCE)],
    [InlineKeyboardButton("⬅️ Geri", callback_data="HELP_BACK")],
]

# ----------- PHOTO EDITOR FUNCTIONS -----------
async def apply_sepia(input_path, output_path):
    # Burada sepia efekti uygulanacak
    pass

async def apply_blackwhite(input_path, output_path):
    # Siyah-beyaz efekti
    pass

async def enhance_photo(input_path, output_path):
    # Netleştirme efekti
    pass

async def apply_real_effect(input_path, output_path):
    # Gerçekçi renk efekti
    pass

# ----------- HANDLERS -----------
@Mukesh.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]))
async def start(client, m: Message):
    try:
        accha = await m.reply_text(text=f"{g}")
        await asyncio.sleep(0.2)
        await accha.edit("✦ Yükleniyor..")
        await asyncio.sleep(0.2)
        await accha.delete()
        
        umm = await m.reply_sticker(sticker=STKR)
        await asyncio.sleep(0.3)
        await umm.delete()
        
        await m.reply_photo(
            photo=START_IMG,
            caption=START,
            reply_markup=InlineKeyboardMarkup(MAIN),
        )
    except Exception as y:
        await m.reply(str(y))

# LOGO

LOGO_LINKS = [
    "https://telegra.ph/file/0859e0104c671bc9b6b7d.jpg",
    "https://telegra.ph/file/b3af2980caf7040702171.jpg",
    "https://telegra.ph/file/14be160df3b84c59e268e.jpg",
    "https://telegra.ph/file/b958155e1e8e9ab9a0416.jpg",
    "https://telegra.ph/file/24fff051c39b815e5078a.jpg",
    "https://telegra.ph/file/258c02c002e89287d5d9b.jpg",
    "https://telegra.ph/file/d2abc99773a9d4954c2ba.jpg",
    "https://telegra.ph/file/9849b3940f063b065f4e3.jpg",
]


@Mukesh.on_message(filters.command(["logo", f"logo@{BOT_USERNAME}"]))
async def lego(event):
    quew = event.pattern_match.group(1)
    if event.sender_id != OWNER_ID and not quew:
        await event.reply(
            "\nKULLANIM : `/logo ceren`"
        )
        return
    pesan = await event.reply("**ᴄʀᴇᴀᴛɪɴɢ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛᴇᴅ ʟᴏɢᴏ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ sᴇᴄ...**")
    try:
        text = event.pattern_match.group(1)
        randc = random.choice(LOGO_LINKS)
        img = Image.open(io.BytesIO(requests.get(randc).content))
        draw = ImageDraw.Draw(img)
        image_widthz, image_heightz = img.size
        fnt = glob.glob("./fonts/fonts*")
        randf = random.choice(fnt)
        font = ImageFont.truetype(randf, 120)
        lw, th, rw, bh = font.getbbox(text)
        w, h = rw - lw, bh - th
        h += int(h * 0.21)
        image_width, image_height = img.size
        draw.text(
            ((image_widthz - w) / 2, (image_heightz - h) / 2),
            text,
            font=font,
            fill=(255, 255, 255),
        )
        x = (image_widthz - w) / 2
        y = (image_heightz - h) / 2 + 6
        draw.text(
            (x, y), text, font=font, fill="white", stroke_width=1, stroke_fill="black"
        )
        fname = "cerenlovely.png"
        img.save(fname, "png")
        await telethn.send_file(
            event.chat_id,
            file=fname,
            caption=f"ʟᴏɢᴏ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ [ CERENS ART ](https://t.me/ViosTeam)",
        )
        await pesan.delete()
        if os.path.exists(fname):
            os.remove(fname)
    except Exception:
        text = event.pattern_match.group(1)
        randc = random.choice(LOGO_LINKS)
        img = Image.open(io.BytesIO(requests.get(randc).content))
        draw = ImageDraw.Draw(img)
        image_widthz, image_heightz = img.size
        fnt = glob.glob("./fonts/fonts*")
        randf = random.choice(fnt)
        font = ImageFont.truetype(randf, 120)
        lw, th, rw, bh = font.getbbox(text)
        w, h = rw - lw, bh - th
        h += int(h * 0.21)
        image_width, image_height = img.size
        draw.text(
            ((image_widthz - w) / 2, (image_heightz - h) / 2),
            text,
            font=font,
            fill=(255, 255, 255),
        )
        x = (image_widthz - w) / 2
        y = (image_heightz - h) / 2 + 6
        draw.text(
            (x, y), text, font=font, fill="white", stroke_width=1, stroke_fill="black"
        )
        fname = "fallen.png"
        img.save(fname, "png")
        await telethn.send_file(
            event.chat_id,
            file=fname,
            caption=f"ʟᴏɢᴏ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ [{BOT_NAME}](https://t.me/{BOT_USERNAME})",
        )
        await pesan.delete()
        if os.path.exists(fname):
            os.remove(fname)



@Mukesh.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
        await query.message.edit_text(
            text=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BACK),
        )
    elif query.data == "HELP_BACK":
        await query.message.edit(
            text=START,
            reply_markup=InlineKeyboardMarkup(MAIN),
        )

# ... (Diğer handler'lar aynı şekilde devam eder)

if __name__ == "__main__":
    print(f"{BOT_NAME} is alive!")
    try:
        Mukesh.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("API_ID/API_HASH geçersiz!")
    except AccessTokenInvalid:
        raise Exception("BOT_TOKEN geçersiz!")
    
    print(f"""
JOIN @{UPDATE_CHNL}
{BOT_NAME} çalışıyor!
""")
    idle()
    Mukesh.stop()
    print("Bot durdu. Görüşürüz!")
