import sqlite3
import os
import app.constant

from app.constant import *


def get_connection(name):  # подключение к БД
    if app.constant.PATH == '':
        with open('constant.py', 'a') as file:
            el = os.path.abspath(name)
            el = el.replace('\\', '/')
            file.write('\n' + f'PATH = "{el}"')
    con = sqlite3.connect(name)
    return con

# фунция иницилизации БД


def create_database():
    with get_connection('novel.db') as conn:
        conn.cursor().execute('''
                CREATE TABLE IF NOT EXISTS heroes(
                    id INTEGER PRIMARY KEY,
                    hero_name VARCHAR(255) NOT NULL,
                    history text DEFAULT NULL,
                    friendly_degree INTEGER DEFAULT 0,
                    items text[] NOT NULL,
                    xp INTEGER DEFAULT 1000,
                    atk INTEGER DEFAULT 20
                );
                ''')
        conn.cursor().execute('''
                    CREATE TABLE IF NOT EXISTS players(
                    id INTEGER PRIMARY KEY,
                    nick_name VARCHAR(255) NOT NULL UNIQUE,
                    hero_id INTEGER REFERENCES heroes(id) DEFAULT 1,
                    feedback text DEFAULT NULL
                );
                ''')
        conn.cursor().execute('''
                    CREATE TABLE IF NOT EXISTS dices(
                    id INTEGER PRIMARY KEY,
                    name_of_dice VARCHAR(255) UNIQUE NOT NULL,
                    num_of_faces text,
                    description text DEFAULT NULL,
                    faces text[]
                );
                ''')
        conn.cursor().execute('''
                    CREATE TABLE IF NOT EXISTS items(
                    id INTEGER PRIMARY KEY,
                    item_name VARCHAR(255) NOT NULL,
                    description text DEFAULT NULL,
                    type_of_item VARCHAR(255) DEFAULT 'strange item'
                );
                ''')
        conn.cursor().execute('''
                    CREATE TABLE IF NOT EXISTS regions(
                    id INTEGER PRIMARY KEY,
                    region_name VARCHAR(255),
                    heroes_placed text[],
                    neighbourhood text[] DEFAULT NULL,
                    maybe_items text[] DEFAULT NULL
                );
                ''')
        conn.cursor().execute('''
                    CREATE TABLE IF NOT EXISTS texts(
                    id INTEGER PRIMARY KEY,
                    content text NOT NULL,
                    degree_of_friendly INTEGER DEFAULT 0,
                    region_id INTEGER REFERENCES regions(id),
                    who_says text REFERENCES heroes(hero_name)
                );
                ''')
        conn.cursor().execute('''
                    CREATE TABLE IF NOT EXISTS faces(
                    id INTEGER PRIMARY KEY,
                    face_name VARCHAR(255) NOT NULL,
                    description text NOT NULL
                );
                ''')
        conn.cursor().execute('''
                    CREATE TABLE IF NOT EXISTS answer_texts(
                    id INTEGER PRIMARY KEY,
                    content text NOT NULL,
                    degree_of_friendly INTEGER DEFAULT 0,
                    region_id INTEGER REFERENCES regions(id)
                );
                ''')
        conn.cursor().execute('''
                    CREATE TABLE IF NOT EXISTS sessions(
                    id INTEGER PRIMARY KEY,
                    player_id INTEGER REFERENCES players(id),
                    checkpoint int REFERENCES regions(id),
                    player_puppet text[]
                    );
                ''')
        conn.commit()