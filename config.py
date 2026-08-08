'''
Arquivo de importação do .env
'''

import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
WEBHOOK: str = os.getenv("WEBHOOK", "/")
ROUTE: str = os.getenv("ROUTE", "/")