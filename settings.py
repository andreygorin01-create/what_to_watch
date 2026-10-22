# what_to_watch/opinions_app/settings.py

import os

from dotenv import load_dotenv

# Читаем переменные из файла .env.
load_dotenv()


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')