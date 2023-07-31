#-----------CREDITS -----------
# telegram : @ME_BLACKMAMBA
# github : FANTASTICSUKHI
from pyrogram import Client, filters,enums,idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatAction, ParseMode
import openai
from pyrogram.types import CallbackQuery
from config import *
import os,sys,re,requests
import asyncio,time
from random import choice
from database import *

from datetime import datetime
import logging

FORMAT = "[GODFATHER] %(message)s"
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


StartTime = time.time()
worker = Client(
    "chat-gpt" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)
START = f"""
๏ ʜᴇʏ, ɪ ᴀᴍ {BOT_NAME}
➻ ᴀɴ ᴏɴʟɪɴᴇ ꜱᴛᴜᴅʏ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ.
──────────────────
➻ ᴜsᴀɢᴇ:\n\n `/course` : CourseName.
    example: `/course ` python

๏ ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ ᴜsᴇ /help
"""
xa = bytearray.fromhex("68 74 74 70 73 3a 2f 2f 67 69 74 68 75 62 2e 63 6f 6d 2f 46 61 6e 74 61 73 74 69 63 53 75 6b 68 69 2f 53 74 75 64 79 42 6f 74").decode()
axx = bytearray.fromhex("4d 41 4d 42 41 5f 52 45 54 55 52 4e 53").decode()
xxc = bytearray.fromhex("4d 41 4d 42 41 20 54 48 4f 55 47 48 54 53").decode()
SOURCE = xa
UPDATE_CHNL = xxc
DEVELOPER = axx
SOURCE_TEXT = f"""
๏ ʜᴇʏ, ɪ ᴀᴍ [{BOT_NAME}]
➻ ᴀɴ ᴏɴʟɪɴᴇ ꜱᴛᴜᴅʏ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ.
──────────────────
ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ
"""


x=["❤️","🎉","✨","🪸","🎉","🎈","🎯"]
g=choice(x)
MAIN = [
    [
        InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/MAMBA_RETURNS"),
        InlineKeyboardButton(text=" ɴᴇᴛᴡᴏʀᴋ ", url=f"https://t.me/THE_THIRD_EYE_NETWORK"),
    ],
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴍᴅs ", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="Firstly Pay then get this source code"),
        InlineKeyboardButton(text=" ᴜᴘᴅᴀᴛᴇs ", url=f"https://t.me/THE_THIRD_EYE_NETWORK"),
    ],
]
X = [
    [
        InlineKeyboardButton(text="ᴘʀᴇᴍɪᴜᴍ", url=f"https://te.legra.ph/file/e7eabfded83d9fe157397.jpg"),
        
        InlineKeyboardButton(text=" ꜰʀᴇᴇ ", url=f"https://t.me/FREE_EDUCATION_MATERIAL"),
    ]
    ]
    
PNG_BTN = [
    [
         InlineKeyboardButton(
             text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", 
                              url=f"https://t.me/TELE_WALI_FRIENDSHIP",
         ),
     ],
]
SOURCE_BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('sᴏᴜʀᴄᴇ', url="https://github.com/FantasticSukhi/StudyBot")]])
HELP_READ = "➻ ᴜsᴇ /course write a simple flask app in python.  \n\n **➻ ᴜsᴇ /ping ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴘɪɴɢ ᴏғ ᴛʜᴇ ʙᴏᴛ.**\n\n©️ @MAMBA_RETURNS**"
HELP_BACK = [
     [
           InlineKeyboardButton(text=" ɪɴꜱᴛʀᴜᴄᴛɪᴏɴꜱ ", url=f"https://t.me/THE_THIRD_EYE_NETWORK/31"),
           
     ],
    [
           InlineKeyboardButton(text="ʙᴀᴄᴋ ", callback_data="HELP_BACK"),
    ],
]

  
#         start
@worker.on_message(filters.command(["start",f"start@{BOT_USERNAME}"]))
async def restart(client, m: Message):
        accha = await m.reply_text(
                        text = f"{g}")
        await asyncio.sleep(0.2)
        await accha.edit("ᴘɪɴɢ ᴘᴏɴɢ ꜱᴛᴀʀᴛɪɴɢ..")
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
#  callback 
@worker.on_callback_query()
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
    
@worker.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def restart(client, message):
    hmm = await message.reply_text(
                        text = HELP_READ,
                        reply_markup= InlineKeyboardMarkup(HELP_BACK),
       )
@worker.on_message(filters.command(['source', 'repo'], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def source(bot, m):
    
    await m.reply_photo(START_IMG, caption=SOURCE_TEXT, reply_markup=SOURCE_BUTTONS)
#  alive
@worker.on_message(filters.command(["ping","alive"], prefixes=["","+", "/", "-", "?", "$", "&","."]))
async def ping(client, message: Message):
        start = datetime.now()
        t = "ριиgιиg..."
        txxt = await message.reply(t)
        await asyncio.sleep(0.25)
        await txxt.edit_text("ριиgιиg.....")
        await asyncio.sleep(0.35)
        await txxt.delete()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await message.reply_photo(
                             photo=START_IMG,
                             caption=f"ʜᴇʏ ʙᴀʙʏ!!\n**[{BOT_NAME}](t.me/{BOT_USERNAME}) ɪꜱ ᴀʟɪᴠᴇ 🥀 ᴀɴᴅ ᴡᴏʀᴋɪɴɢ ꜰɪɴᴇ ᴡɪᴛʜ ᴘᴏɴɢ ᴏꜰ \n➥ `{ms}` ms\n\n**ᴍᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ || [MAMBA](https://t.me/MAMBA_RETURNS)||",
                             reply_markup=InlineKeyboardMarkup(PNG_BTN),
       )

#  main   
bot.api_key = OPENAI_KEY
@worker.on_message(filters.command(["course","edu","pdf"],  prefixes=["","+", ".", "/", "-", "?", "$","#","&"]))
async def chat(bot, message):
    
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/course python`")
        else:

            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2,
)

            x=resp['choices'][0]["message"]["content"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"{message.from_user.first_name} ᴀꜱᴋᴇᴅ:\n\n {a} \n\n {BOT_NAME} ᴀɴꜱᴡᴇʀᴇᴅ:-\n\n {x}\n\n✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ  {telegram_ping} \n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{BOT_USERNAME} ", parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(X))     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ:    {e} ")

@worker.on_message(filters.command(["image","photo","img","generate"],  prefixes=["","+", ".", "/", "-", "?", "$","#","&"] ))

async def chat(bot, message):

    try:



        start_time = time.time()

        await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)

        if len(message.command) < 2:

            await message.reply_text(

            "**Example:**\n\n`/generate a white siamese cat`")

        else:

            a = message.text.split(' ', 1)[1]

            response= bot.Image.create(prompt=a ,n=1,size="1024x1024")

            image_url = response['data'][0]['url']

            end_time = time.time()

            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"

            await message.reply_photo(image_url,caption=f"✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ {telegram_ping} ",parse_mode=ParseMode.DISABLED,reply_markup=InlineKeyboardMarkup(X)) 

    except Exception as e:

            await message.reply_text(f"**ᴇʀʀᴏʀ: **  ` {e} `")

    

    
s = bytearray.fromhex("68 74 74 70 73 3a 2f 2f 67 69 74 68 75 62 2e 63 6f 6d 2f 46 61 6e 74 61 73 74 69 63 53 75 6b 68 69 2f 43 48 41 54 47 50 54").decode()
u = bytearray.fromhex("4d 45 5f 42 4c 41 43 4b 4d 41 4d 42 41").decode()
d= bytearray.fromhex("4d 41 4d 42 41 20 54 48 4f 55 47 48 54 53").decode()
if SOURCE != s:
    print("So sad, you have changed source, change it back to ` https://github.com/FantasticSukhi/StudyBot `  else I won't work")
    sys.exit(1)  
if DEVELOPER!=u:
    print("So sad, you have changed Updates, change it back to `INCRICIBLE ` else I won't work")
    sys.exit(1)
if UPDATE_CHNL!=d:
    print("So sad, you have change developer, change it back to `MAMBA_RETURNS` else I won't work")
    sys.exit(1)


if __name__ == "__main__":
    print(f""" {BOT_NAME} ɪs ᴀʟɪᴠᴇ!
    """)
    try:
        worker.start()
        
        
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    print(f"""JOIN  @TELE_WALI_FRIENDSHIP
GIVE STAR TO THE REPO 
 {BOT_NAME} ɪs ᴀʟɪᴠᴇ!  
    """)
    idle()
    worker.stop()
    print("Bot stopped. Bye !")
#-----------CREDITS -----------
# telegram : @ME_BLACKMAMBA
# github : FantasticSukhi
