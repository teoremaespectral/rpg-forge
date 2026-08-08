from typing import Callable

from Message import Message

handlers = []

def dispatch(update: dict):
    print(update)
    _message = update["message"]
    m = Message(_message)
    print(m)
    #print("------------------------------------------------------------------------------------------")

    for handler in handlers:
        handler(m)

def register_handler(handler: Callable):
    handlers.append(handler)