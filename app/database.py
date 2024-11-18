import sqlite3

import app.constant
from app.constant import *
import os
import dotenv


def get_connection(name):
    if app.constant.PATH == '':
        with open('constant.py', 'a') as file:
            el = os.path.abspath(name)
            el = el.replace('\\', '/')
            file.write('\n' + f'PATH = "{el}"')
    con = sqlite3.connect(name)
    return con


def create_database():
    with get_connection('novel.db') as conn:
        conn.cursor().execute('''
                CREATE TABLE IF NOT EXISTS heroes(
                    id SERIAL PRIMARY KEY,
                    hero_name VARCHAR(255) NOT NULL,
                    history text DEFAULT NULL,
                    friendly_degree INTEGER DEFAULT 0,
                    items text[] NOT NULL,
                    skills text[] DEFAULT NULL
                );
                ''')
        conn.cursor().execute('''
                    CREATE TABLE IF NOT EXISTS players(
                    id SERIAL PRIMARY KEY,
                    nick_name VARCHAR(255) NOT NULL,
                    hero_id INTEGER REFERENCES heroes(id) DEFAULT 1,
                    feedback text DEFAULT NULL
                );
                ''')
        conn.cursor().execute('''
                    CREATE TABLE IF NOT EXISTS dices(
                    id SERIAL PRIMARY KEY,
                    name_of_dice VARCHAR(255) UNIQUE NOT NULL,
                    num_of_faces INTEGER DEFAULT 1,
                    description text DEFAULT NULL,
                    faces text[]
                );
                ''')
        conn.cursor().execute('''
                    CREATE TABLE IF NOT EXISTS items(
                    id SERIAL PRIMARY KEY,
                    item_name VARCHAR(255) NOT NULL,
                    description text DEFAULT NULL,
                    type_of_item VARCHAR(255) DEFAULT 'strange item'
                );
                ''')
        conn.cursor().execute('''
                    CREATE TABLE IF NOT EXISTS regions(
                    id SERIAL PRIMARY KEY,
                    region_name VARCHAR(255),
                    description text DEFAULT NULL,
                    heroes_placed text[],
                    neighbourhood text[],
                    maybe_items text[]
                );
                ''')
        conn.cursor().execute('''
                    CREATE TABLE IF NOT EXISTS skills(
                    id SERIAL PRIMARY KEY,
                    skill_name VARCHAR(255) NOT NULL,
                    type_of_skills VARCHAR(255) DEFAULT 'strange skill',
                    description text DEFAULT NULL
                );
                ''')
        conn.cursor().execute('''
                    CREATE TABLE IF NOT EXISTS texts(
                    id SERIAL PRIMARY KEY,
                    content text NOT NULL,
                    degree_of_friendly INTEGER DEFAULT 0,
                    region_id INTEGER REFERENCES regions(id)
                );
                ''')
        conn.cursor().execute('''
                    CREATE TABLE IF NOT EXISTS faces(
                    id SERIAL PRIMARY KEY,
                    face_name VARCHAR(255) NOT NULL,
                    description text NOT NULL
                );
                ''')
        conn.cursor().execute('''
                    CREATE TABLE IF NOT EXISTS answer_words(
                    id SERIAL PRIMARY KEY,
                    content text NOT NULL,
                    degree_of_friendly INTEGER DEFAULT 0,
                    region_id INTEGER REFERENCES regions(id)
                );
                ''')
        conn.cursor().execute('''
                    CREATE TABLE IF NOT EXISTS sessions(
                    id SERIAL PRIMARY KEY,
                    player_id INTEGER REFERENCES players(id),
                    world_map text[],
                    placement VARCHAR(255) NOT NULL,
                    checkpoint int REFERENCES dices(id),
                    items text[],
                    the_player_puppet text[]
                    );
                ''')
        conn.cursor().execute('''
                    CREATE TABLE IF NOT EXISTS checkpoints(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    region_id INTEGER REFERENCES regions(id)
            )
        ''')
        conn.commit()


def update_info(file_name: str):
    with get_connection(PATH) as conn:
        with open(os.path.abspath(file_name)) as file:
            lines = file.read()