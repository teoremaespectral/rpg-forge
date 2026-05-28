from bot import my_bot
from Message import Message as M

send_message = my_bot.sendMessage
send_sticker = my_bot.sendSticker
send_audio = my_bot.sendVoice
send_music = my_bot.sendAudio
send_video_note = my_bot.sendVideoNote

handlers = []

@handlers.append
def hello(m: M):
    
    if m.text.lower() == "olá!":
        pessoa = m.user_name
        send_message(m.chat_id, f'Olá, {pessoa} ☺️')
