from random import randint as ran
import re

from bot import my_bot
from Message import Message as M

from services import RollEngine

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
    
    regex = r"((?P<qtd>\d+)d(?P<lados>\d+) *)((?P<modificador>[+-]\d+) *)?"
    match = re.match(regex, m.text.lower())
    
    qtd = match and int(match.group("qtd")) or 1
    sides = match and int(match.group("lados")) or 20
    modificador = match and int(match.group("modificador")) or 0


    dados = [ran(1, sides) for _ in range(qtd)]

    message = f"Dados: {dados}\nmodificador: {modificador}\ntotal: {sum(dados)+modificador}"
    send_message(m.chat_id, message)



