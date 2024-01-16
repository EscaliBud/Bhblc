from pyrogram import Client, filters

@Client.on_message(filters.command ('start'))
async def cmd_start(Client,message):
  try:
    user_id = str(message.from_user.id)
    chat_type = str(message.chat.type)
    chat_id = str(message.chat.id)
    #PLAN CHECK 
    
    texta = """
sᴛᴀʀᴛɴɢ ɪʜᴋ ᴄᴄ ᴄʜᴇᴄᴋᴇʀ ⚡ ■□□
      """
    edit = await message.reply_text(texta,message.id)
    textb = """
sᴛᴀʀᴛɪɴɢ ɪʜᴋ ᴄᴄ ᴄʜᴇᴄᴋᴇʀ ⚡ ■■□
      """
    edit = await Client.edit_message_text(message.chat.id,edit.id,textb)
    textc = """
sᴛᴀʀᴛɪɴɢ ɪʜᴋ ᴄᴄ ᴄʜᴇᴄᴋᴇʀ ⚡ ■■■
      """
    edit = await Client.edit_message_text(message.chat.id,edit.id,textc)
    textd = f"""
𝗛𝗲𝘆 <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> 

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɪʜᴋ ᴄᴄ ᴄʜᴇᴄᴋᴇʀ ʙᴏᴛ!!

ɴᴏᴛ ᴏɴʟʏ ᴄʜᴇᴄᴋɪɴɢ ᴄᴄ ,ʙᴜᴛ ɪ ᴄᴀɴ ᴀʟsᴏ ᴅᴏ ᴀ ʟᴏᴛ ᴏғ ʜᴀɴᴅғᴜʟ ᴛᴀsᴋs!!

ᴛʏᴘᴇ /register sᴛᴀʀᴛ ᴜsɪɴɢ ᴍᴇ

ɪɴᴄᴀsᴇ ᴏғ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ,ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴅᴇᴠ @EscaliBud

"""
    edit = await Client.edit_message_text(message.chat.id,edit.id,textd)
    await plan_expirychk(user_id)
  except Exception as e:
      print(e)
