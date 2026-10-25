from random import randint as ran
import re

from bot import my_bot
from Message import Message as M

from services import Manager

send_message = my_bot.sendMessage
send_sticker = my_bot.sendSticker
send_audio = my_bot.sendVoice
send_music = my_bot.sendAudio
send_video_note = my_bot.sendVideoNote

handlers = []


@handlers.append
def roll(m: M):
    if m.command not in ["/roll", "/r"]:
        return
    
    manager = Manager()
    message = manager.execute_roll(m.text, m.user_id)

    send_message(m.chat_id, message)



