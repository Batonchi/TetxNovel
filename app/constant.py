import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()

DBNAME = os.environ.get('DBNAME')
HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')
SECRET_KEY = os.environ.get('SECRET_KEY')
ALGORITHM = os.environ.get('ALGORITHM')
PATH = ''
PATH = "C:/Users/gkokg/PycharmProjects/TetxNovel/app/novel.db"