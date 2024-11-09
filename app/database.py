import psycopg2
from constant import *


def get_connection():
    conn = psycopg2.connect(
        dbname=DBNAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )
    return conn


def create_database():
    with get_connection() as conn:
        query = """
        CREATE TABLE IF NOT EXISTS heroes(
            id SERIAL PRIMARY KEY,
            hero_name VARCHAR(255) NOT NULL,
            history text DEFAULT NULL,
            friendly_degree INTEGER DEFAULT 0,
            items INTEGER[] NOT NULL,
            skills INTEGER[] DEFAULT NULL
        );
        
        CREATE TABLE IF NOT EXISTS players(
            id SERIAL PRIMARY KEY,
            nick_name VARCHAR(255) NOT NULL,
            hero_id INTEGER REFERENCES heroes(id) DEFAULT 1,
            steps text[],
            feedback text DEFAULT NULL
        );
        
        CREATE TABLE IF NOT EXISTS dices(
            id SERIAL PRIMARY KEY,
            name_of_dice VARCHAR(255) NOT NULL,
            num_of_faces INTEGER DEFAULT 1,
            description text DEFAULT NULL
        );
        
        CREATE TABLE IF NOT EXISTS items(
            id SERIAL PRIMARY KEY,
            item_name VARCHAR(255) NOT NULL,
            description text DEFAULT NULL,
            type_of_item VARCHAR(255) DEFAULT 'strange item'
        );
        
        CREATE TABLE IF NOT EXISTS regions(
            id SERIAL PRIMARY KEY,
            region_name VARCHAR(255),
            description text DEFAULT NULL,
            heroes_placed INTEGER[],
            neighbourhood INTEGER[]
        );
        
        CREATE TABLE IF NOT EXISTS skills(
            id SERIAL PRIMARY KEY,
            skill_name VARCHAR(255) NOT NULL,
            type_of_skills VARCHAR(255) DEFAULT 'strange skill',
            description text DEFAULT NULL
        );
        
        CREATE TABLE IF NOT EXISTS texts(
            id SERIAL PRIMARY KEY,
            content text NOT NULL,
            degree_of_friendly INTEGER DEFAULT 0,
            region_id INTEGER REFERENCES regions(id)
        );
        
        CREATE TABLE IF NOT EXISTS faces(
            id SERIAL PRIMARY KEY,
            face_name VARCHAR(255) NOT NULL,
            description text NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS answer_words(
            id SERIAL PRIMARY KEY,
            content text NOT NULL,
            degree_of_friendly INTEGER DEFAULT 0,
            region_id INTEGER REFERENCES regions(id)
        );
        """
        conn.cursor().execute(query)
        conn.commit()


def update_info(table_name: str, file_name: str):
    pass
