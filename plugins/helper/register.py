#Pyrogrm Import
from pyrogram import Client, filters
#Reg Data Import
import time
from datetime import date
from datetime import timedelta
from plugins.func.users_sql import *
@Client.on_message(filters.command ('register'))
async def cmd_register(Client,message):
  try:
    user_id = str(message.from_user.id)
    username = str(message.from_user.username)
    chat_id = str(message.chat.id)
    antispam_time = int(time.time())
    reg_at = str(date.today())
    regdata = fetchinfo(user_id)
    results = str(regdata)
    if results=='None':
      registration = insert_reg_data(user_id,username,antispam_time,reg_at)
      resp = "ʀᴇɢɪsᴛᴇʀᴇᴅ sᴜᴄᴄᴇsɪғᴜʟʟʏ ✅ . ᴛʏᴘᴇ /cmds ᴛᴏ sᴇᴇ ᴍʏ ғᴜʟʟ ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ."
      await message.reply_text(resp,message.id)
  
    else:
      resp = "ᴀʟʀᴇᴀᴅʏ ʀᴇɢɪsᴛᴇʀᴇᴅ ⚠️ .ᴛʏᴘᴇ /cmds ᴛᴏ sᴇᴇ ғᴜʟʟ ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ"
      await message.reply_text(resp,message.id)
      await plan_expirychk(user_id)
    
  except Exception as e:
      print(e)
  
  