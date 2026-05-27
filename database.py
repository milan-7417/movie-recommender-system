import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash



import os

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATABASE = os.path.join(
    BASE_DIR,
    "database",
    "movie.db"
)


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # USERS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # RATINGS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ratings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        movie_name TEXT,
        rating INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # WATCHLIST TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS watchlist (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        movie_name TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()


def create_user(username, email, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    hashed_password = generate_password_hash(password)

    try:
        cursor.execute("""
        INSERT INTO users (username, email, password)
        VALUES (?, ?, ?)
        """, (username, email, hashed_password))

        conn.commit()
        return True

    except:
        return False

    finally:
        conn.close()


def login_user(email, password):
    conn = get_db_connection()

    user = conn.execute("""
    SELECT * FROM users WHERE email = ?
    """, (email,)).fetchone()

    conn.close()

    if user and check_password_hash(user["password"], password):
        return user

    return None

def add_to_watchlist(user_id, movie_name):

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO watchlist
    (user_id, movie_name)
    VALUES (?, ?)
    """, (user_id, movie_name))

    conn.commit()
    conn.close()


def get_watchlist(user_id):

    conn = get_db_connection()

    movies = conn.execute("""
    SELECT movie_name
    FROM watchlist
    WHERE user_id = ?
    """, (user_id,)).fetchall()

    conn.close()

    return movies

def add_to_watchlist(user_id, movie_name):

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO watchlist
    (user_id, movie_name)
    VALUES (?, ?)
    """, (user_id, movie_name))

    conn.commit()
    conn.close()


def get_watchlist(user_id):

    conn = get_db_connection()

    movies = conn.execute("""
    SELECT movie_name
    FROM watchlist
    WHERE user_id = ?
    """, (user_id,)).fetchall()

    conn.close()

    return movies

def delete_from_watchlist(
    user_id,
    movie_name
):

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM watchlist
    WHERE user_id = ?
    AND movie_name = ?
    """, (
        user_id,
        movie_name
    ))

    conn.commit()
    conn.close()    