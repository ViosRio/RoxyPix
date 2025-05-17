#
#-----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
import os
from pyrogram import Client, filters,enums,idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatAction, ParseMode
from pyrogram.types import CallbackQuery
from config import *
import requests

from pyrogram import filters
import os,sys,re,requests
import asyncio,time
from random import choice
from datetime import datetime
import logging

FORMAT = "[LEGEND-MUKESH] %(message)s"
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


StartTime = time.time()
Mukesh = Client(
    "chat-gpt" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)
START = f"""
๏ 𝗠𝗲𝗿𝗵𝗮𝗯𝗮 🌹

MERHABA BEN DEEP SEEK İLE TASARLANAN DOSYA KUYUMCUSU VE FOTOĞRAF EDİTÖRÜYÜM ?
"""
xa = bytearray.fromhex("68 74 74 70 73 3A 2F 2F 67 69 74 68 75 62 2E 63 6F 6D 2F 4E 6F 6F 62 2D 6D 75 6B 65 73 68 2F 43 68 61 74 67 70 74 2D 62 6F 74").decode()
SOURCE = xa
SOURCE_TEXT = f"""
๏ ʜᴇʏ,
"""


x=["❤️","🎉","✨","🪸","🎉","🎈","🎯"]
g=choice(x)
MAIN = [
    [
        InlineKeyboardButton(text="sᴀʜɪᴘ", url=f"https://t.me/{OWNER_USERNAME}")
    ],
    [
        InlineKeyboardButton(
            text="ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="ʏᴀʀᴅıᴍ & ᴋᴏᴍᴜᴛʟᴀʀ ", callback_data="HELP"),
    ],
]
X = [
    [
        InlineKeyboardButton(text=" ᴅᴇsᴛᴇᴋ ", url=f"https://t.me/{SUPPORT_GRP}"),
    ]
    ]
    
PNG_BTN = [
    [
         InlineKeyboardButton(
             text="ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="ᴅᴇsᴛᴇᴋ", 
                              url=f"https://t.me/{SUPPORT_GRP}",
         ),
     ],
]
SOURCE_BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('sᴏᴜʀᴄᴇ', url=f"{SOURCE}")]])
HELP_READ = "**➻ 𝗞𝘂𝗹𝗹𝗮𝗻ı𝗺 :**  \n\n/• /sephia = Fotoğrafa S/Black Efekti Uygular\n\n• /ping = BOTUN SAĞLIK SORUNLARI TEST ET\n\nʙᴏᴛ ᴠᴇʀsɪᴏɴ ᴠ2.1"
HELP_BACK = [
     [
           InlineKeyboardButton(text="ᴋᴀʏɴᴀᴋ ", url=f"https://github.com/ViosRio/RoxyTrans"),
           
     ],
    [
           InlineKeyboardButton(text="⬅️ ", callback_data="HELP_BACK"),
    ],
]

  
#         start
@Mukesh.on_message(filters.command(["start",f"start@{BOT_USERNAME}"]))
async def start(client, m: Message):
    try:
        accha = await m.reply_text(
                        text = f"{g}")
        await asyncio.sleep(0.2)
        await accha.edit("✦ Yᴜ̈ᴋʟᴇɴɪʏᴏʀ..")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(
                  sticker = STKR,
        )
        await asyncio.sleep(0.3)
        await umm.delete()
        await m.reply_photo(
            photo = START_IMG,
            caption=START,
            reply_markup=InlineKeyboardMarkup(MAIN),
        )
    except Exception as y:
        await m.reply(y)
#  callback 
@Mukesh.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
     await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(HELP_BACK),
     )
    elif query.data == "HELP_BACK":
            await query.message.edit(text = START,
                  reply_markup=InlineKeyboardMarkup(MAIN),
        )
    
@Mukesh.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def restart(client, message):
    hmm = await message.reply_photo(START_IMG,
                        caption=HELP_READ,
                        reply_markup= InlineKeyboardMarkup(HELP_BACK),
       )
@Mukesh.on_message(filters.command(['source', 'repo'], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def source(bot, m):
    
    await m.reply_photo(START_IMG, caption=SOURCE_TEXT, reply_markup=SOURCE_BUTTONS)
#  alive
@Mukesh.on_message(filters.command(["ping","alive"], prefixes=["+", "/", "-", "?", "$", "&","."]))
async def ping(client, message: Message):
        start = datetime.now()
        t = "Bekleyiniz.."
        txxt = await message.reply(t)
        await asyncio.sleep(0.25)
        await txxt.edit_text("✦ Yᴜ̈ᴋʟᴇɴɪʏᴏʀ..")
        await asyncio.sleep(0.35)
        await txxt.delete()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await message.reply_photo(
                             photo=START_IMG,
                             caption=f"ʜᴇʏ !!\n**[{BOT_NAME}](t.me/{BOT_USERNAME}) ɪ̇ʟᴇᴛɪşɪᴍ ᴠᴇ öɴᴇʀɪ \n➥ `{ms}` ms\n\n**🌹 || [sᴀʜɪᴘ](https://t.me/{OWNER_USERNAME})||",
                             reply_markup=InlineKeyboardMarkup(PNG_BTN),
       )

# GÖRSEL EDİTOR KODU BURAYA ATALIM KANKİ
  #-----------PHOTO EDITOR & FILE CONVERTER------------
@Mukesh.on_message(filters.command(["sephia", "real", "bw", "enhance"]) & filters.reply)
async def photo_effects(client, message: Message):
    try:
        # Kullanıcının yanıtladığı mesajı kontrol et
        replied = message.reply_to_message
        if not replied.photo:
            await message.reply_text("❌ Lütfen bir fotoğrafı yanıtlayın!")
            return

        # Kullanıcıyı bilgilendirme
        msg = await message.reply_text("✨ Sihrimi uyguluyorum...")
        
        # Fotoğrafı indir
        photo_path = await replied.download()
        
        # Efekte göre işlem yap
        command = message.command[0]
        output_path = f"edited_{command}.jpg"
        
        if command == "sephia":
            await apply_sepia(photo_path, output_path)
        elif command == "bw":
            await apply_blackwhite(photo_path, output_path)
        elif command == "enhance":
            await enhance_photo(photo_path, output_path)
        elif command == "real":
            await apply_real_effect(photo_path, output_path)
        
        # Kullanıcıya gönder
        await message.reply_photo(
            photo=output_path,
            caption=f"🏆 İşte {command} efekti uygulanmış hali!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❤️ Daha Fazla Efekt", callback_data="more_effects")]
            )
        )
        
        # Temizlik
        os.remove(photo_path)
        os.remove(output_path)
        await msg.delete()
        
    except Exception as e:
        await message.reply_text(f"❌ Hata oluştu: {str(e)}")

#-----------FILE CONVERTER------------
@Mukesh.on_message(filters.document)
async def handle_documents(client, message: Message):
    file_type = message.document.file_name.split('.')[-1].lower()
    
    # Butonlar oluştur
    buttons = []
    
    if file_type in ["txt", "csv", "sql"]:
        buttons.append([InlineKeyboardButton("📄 SQL'e Dönüştür", callback_data="convert_sql")])
        buttons.append([InlineKeyboardButton("📊 CSV'ye Dönüştür", callback_data="convert_csv")])
    
    elif file_type in ["jpg", "jpeg", "png"]:
        buttons.append([InlineKeyboardButton("🎨 Sepia Efekti", callback_data="effect_sepia")])
        buttons.append([InlineKeyboardButton("⚫ Siyah-Beyaz", callback_data="effect_bw")])
        buttons.append([InlineKeyboardButton("✨ Netleştir", callback_data="effect_enhance")])
    
    elif file_type in ["mp4", "avi", "mov"]:
        buttons.append([InlineKeyboardButton("🎥 MP4'e Dönüştür", callback_data="convert_mp4")])
        buttons.append([InlineKeyboardButton("🎞️ AVI'ye Dönüştür", callback_data="convert_avi")])
    
    if buttons:
        buttons.append([InlineKeyboardButton("❌ İptal", callback_data="cancel_convert")])
        await message.reply_text(
            "🔮 Bu dosya ile ne yapmak istersin?",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

#-----------CALLBACK HANDLERS------------
@Mukesh.on_callback_query(filters.regex("^convert_|^effect_"))
async def handle_conversion(client, callback: CallbackQuery):
    action = callback.data.split('_')[0]
    target_format = callback.data.split('_')[1]
    
    await callback.answer("⏳ İşleme alındı...")
    original_message = callback.message.reply_to_message
    
    try:
        # Dosyayı indir
        file_path = await original_message.download()
        output_path = f"converted_{target_format}.{target_format}"
        
        # Dönüşüm işlemleri
        if action == "convert":
            if target_format == "sql":
                await convert_to_sql(file_path, output_path)
            elif target_format == "csv":
                await convert_to_csv(file_path, output_path)
            # Diğer dönüşümler...
            
        elif action == "effect":
            if target_format == "sepia":
                await apply_sepia(file_path, output_path)
            elif target_format == "bw":
                await apply_blackwhite(file_path, output_path)
            # Diğer efektler...
        
        # Kullanıcıya gönder
        if action == "convert":
            await callback.message.reply_document(
                document=output_path,
                caption=f"✅ Başarıyla {target_format.upper()} formatına dönüştürüldü!"
            )
        else:
            await callback.message.reply_photo(
                photo=output_path,
                caption=f"✨ {target_format.upper()} efekti uygulandı!"
            )
        
        # Temizlik
        os.remove(file_path)
        os.remove(output_path)
        
    except Exception as e:
        await callback.message.reply_text(f"❌ Dönüşüm hatası: {str(e)}")
    finally:
        await callback.message.delete()

# Yardım mesajını güncelle
HELP_READ = """
**📌 Kullanım Kılavuzu**

✨ **Fotoğraf Efektleri** (Fotoğrafa yanıt vererek):
• `/sephia` - Sepia efekti uygular
• `/bw` - Siyah-beyaz yapar
• `/enhance` - Fotoğrafı netleştirir
• `/real` - Gerçekçi renk efekti

🔄 **Dosya Dönüştürme**:
• Herhangi bir dosya gönderin ve butonlarla seçim yapın
• Desteklenenler: TXT/CSV/SQL, JPG/PNG, MP4/AVI

📊 **Veritabanı Dönüşümleri**:
• SQL ↔ CSV otomatik dönüşüm
• Tablo yapısı sorgulama

**Powered by Deepseek 🌿🍻❤️**
"""
    
        
        


s = bytearray.fromhex("68 74 74 70 73 3A 2F 2F 67 69 74 68 75 62 2E 63 6F 6D 2F 4E 6F 6F 62 2D 6D 75 6B 65 73 68 2F 43 68 61 74 67 70 74 2D 62 6F 74").decode()

if SOURCE != s:
    print("So sad, you have changed source, change it back to ` https://github.com/Noob-mukesh/Chatgpt-bot `  else I won't work")
    sys.exit(1)  


if __name__ == "__main__":
    print(f""" {BOT_NAME} ɪs ᴀʟɪᴠᴇ!
    """)
    try:
        Mukesh.start()
        
        
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    print(f"""JOIN  @MR_SUKKUN
GIVE STAR TO THE REPO 
 {BOT_NAME} ɪs ᴀʟɪᴠᴇ!  
    """)
    idle()
    Mukesh.stop()
    print("Bot stopped. Bye !")
#-----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
