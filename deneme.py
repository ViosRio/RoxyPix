# demo
import os
from io import BytesIO  
import random  
from pyrogram import Client, filters, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.types import CallbackQuery
from config import *
import requests
from PIL import Image, ImageDraw, ImageFont
from PIL import ImageEnhance
enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(1.5)  

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
**📌 KLAVUZ**

✨ **FOTO STUDYO**:

• /sephia = Fotoğrafa Sepia Efekti Uygular
• /black = Siyah-Beyaz Yapar
• /real = Gerçekçi Renk efekti

❤️ **Logo Fasarım**
• `/logo` - Logo Tasarım İsim Şenlik

**Powered by Deepseek 🌿🍻❤️**
"""

HELP_BACK = [
    [InlineKeyboardButton("ᴋᴀʏɴᴀᴋ", url=SOURCE)],
    [InlineKeyboardButton("⬅️ Geri", callback_data="HELP_BACK")],
]

# ----------- PHOTO EDITOR FUNCTIONS -----------
# ----------- PHOTO EDITOR FUNCTIONS -----------
async def apply_blackwhite(input_path: str) -> BytesIO:
    """Siyah-Beyaz Efekti Uygular"""
    image = Image.open(input_path)
    image = image.convert("L")  # Grayscale'e çevir
    output = BytesIO()
    image.save(output, format="PNG")
    output.seek(0)
    return output

async def apply_sepia(input_path: str) -> BytesIO:
    """Sepia Efekti Uygular"""
    image = Image.open(input_path)
    width, height = image.size
    pixels = image.load()
    
    for py in range(height):
        for px in range(width):
            r, g, b = image.getpixel((px, py))
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)
            pixels[px, py] = (min(tr, 255), min(tg, 255), min(tb, 255))
    
    output = BytesIO()
    image.save(output, format="PNG")
    output.seek(0)
    return output

# ----------- PHOTO EDITOR FUNCTIONS -----------
async def apply_real_effect(input_path: str) -> BytesIO:
    """Fotoğrafı Netleştirir Ve Çizgi Film Efekti Ekler"""
    from PIL import ImageFilter
    
    image = Image.open(input_path)
    
    # 1. Netleştirme efekti
    sharpened = image.filter(ImageFilter.SHARPEN)
    
    # 2. Çizgi film efekti (edge enhancement + renk canlandırma)
    edges = sharpened.filter(ImageFilter.FIND_EDGES)
    cartoon = Image.blend(sharpened, edges, 0.3)
    
    output = BytesIO()
    cartoon.save(output, format="PNG")
    output.seek(0)
    return output

# ----------- EDITOR HANDLERS -----------
@Mukesh.on_message(filters.command(["real", "enhance"]) & filters.reply)
async def real_effect_handler(client, message: Message):
    try:
        if not message.reply_to_message.photo:
            await message.reply("❌ Lütfen Bir Fotoğrafı Yanıtlayın!")
            return
            
        msg = await message.reply("🎨 Fotoğrafa Profesyonel Efektler Uygulanıyor...")
        
        # Fotoğrafı indir
        photo = await message.reply_to_message.download()
        
        # Efekti uygula
        processed = await apply_real_effect(photo)
        
        # Gönder
        await message.reply_photo(
            photo=processed,
            caption=f"✨ {BOT_NAME} | Profesyonel Efekt\n💫 Netleştirme + Çizgi Film Stili",
            reply_markup=InlineKeyboardMarkup(PNG_BTN)
        
        await msg.delete()
        os.remove(photo)
        
    except Exception as e:
        await message.reply(f"❌ Hata: {str(e)}")


# ----------- EDITOR HANDLERS -----------
@Mukesh.on_message(filters.command(["black", "bw"]) & filters.reply)
async def black_white_handler(client, message: Message):
    try:
        if not message.reply_to_message.photo:
            await message.reply("❌ Lütfen Bir Fotoğrafı Yanıtlayın!")
            return
            
        msg = await message.reply("🔄 Fotoğraf Siyah-Beyaz Yapılıyor...")
        
        # Fotoğrafı indir
        photo = await message.reply_to_message.download()
        
        # Efekti uygula
        processed = await apply_blackwhite(photo)
        
        # Gönder (DÜZELTİLMİŞ KISIM)
        await message.reply_photo(
            photo=processed,
            caption=f"✨ {BOT_NAME} | Siyah-Beyaz Efekti",
            reply_markup=InlineKeyboardMarkup(PNG_BTN)
        )
        
        await msg.delete()
        os.remove(photo)
        
    except Exception as e:
        await message.reply(f"❌ Hata: {str(e)}")
        
    

@Mukesh.on_message(filters.command(["sepia"]) & filters.reply)
async def sepia_handler(client, message: Message):
    try:
        if not message.reply_to_message.photo:
            await message.reply("❌ Lütfen Bir Fotoğrafı Yanıtlayın!")
            return
            
        msg = await message.reply("🔄 Sepia Efekti Uygulanıyor...")
        
        # Fotoğrafı indir
        photo = await message.reply_to_message.download()
        
        # Efekti uygula
        processed = await apply_sepia(photo)
        
        # Gönder
        await message.reply_photo(
            photo=processed,
            caption=f"✨ {BOT_NAME} | Sepia Efekti",
            reply_markup=InlineKeyboardMarkup(PNG_BTN))
        
        await msg.delete()
        os.remove(photo)
        
    except Exception as e:
        await message.reply(f"❌ Hata: {str(e)}")



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

# logos
@Mukesh.on_message(filters.command(["logo", f"logo@{BOT_USERNAME}"]))
async def lego(client, message: Message):
    try:
        # Komut kontrolü
        if len(message.command) < 2:
            await message.reply("❌ Lütfen bir metin belirtin.\nÖrnek: `/logo Ceren`")
            return

        # Logo oluşturma mesajı
        processing_msg = await message.reply("**🔄 Logo oluşturuluyor, lütfen bekleyin...**")

        # Rastgele arkaplan seçimi
        bg_url = random.choice(LOGO_LINKS)
        response = requests.get(bg_url)
        response.raise_for_status()

        # Görsel işleme
        with Image.open(BytesIO(response.content)) as img:
            draw = ImageDraw.Draw(img)
            
            # Font ayarları (3 farklı font denemesi)
            try:
                font = ImageFont.truetype("./fonts/default.ttf", 120)
            except:
                try:
                    font = ImageFont.truetype("./fonts/default.ttf", 120)
                except:
                    font = ImageFont.load_default()

            text = " ".join(message.command[1:])
            
            # Metin boyutları ve konumu
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (img.width - text_width) / 2
            y = (img.height - text_height) / 2
            
            # Metni çiz
            draw.text(
                (x, y), 
                text, 
                font=font, 
                fill="white", 
                stroke_width=2, 
                stroke_fill="black"
            )

            # Geçici dosyaya kaydet
            temp_file = f"logo_{message.from_user.id}.png"
            img.save(temp_file, "PNG")

            # Kullanıcıya gönder
            await message.reply_photo(
                photo=temp_file,
                caption=f"✨ {BOT_NAME} tarafından oluşturuldu\n💖 @{SUPPORT_GRP}",
                reply_markup=InlineKeyboardMarkup(PNG_BTN)
            )

        # İşlem mesajını sil
        await processing_msg.delete()

    except requests.RequestException as e:
        await message.reply(f"❌ Hata: Arkaplan resmi yüklenemedi\n{str(e)}")
    except Exception as e:
        await message.reply(f"❌ Logo oluşturulurken hata:\n{str(e)}")
    finally:
        # Temizlik
        if 'temp_file' in locals() and os.path.exists(temp_file):
            os.remove(temp_file)
        if 'processing_msg' in locals():
            try:
                await processing_msg.delete()
            except:
                pass
        
        
                
                        



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
