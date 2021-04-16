import contextlib
import os

with contextlib.suppress(ImportError):
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())

TELEGRAM_API_TOKEN = os.environ.get('TELEGRAM_API_TOKEN')

FLASK_ADMIN_HOST = os.environ.get('FLASK_ADMIN_HOST')
FLASK_ADMIN_PORT = os.environ.get('FLASK_ADMIN_PORT')
