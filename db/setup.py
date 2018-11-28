import sqlite3
import os

conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute('''CREATE TABLE if not exists users(
    id    INTEGER PRIMARY KEY,
    nickname  TEXT,
    discord_id TEXT,
    oauth_token TEXT
)''')
c.execute('''CREATE TABLE if not exists servers(
    id    INTEGER PRIMARY KEY,
    discord_id TEXT
)''')
c.execute('''CREATE TABLE if not exists auth_keys(
    id    INTEGER PRIMARY KEY,
    key TEXT
)''')
c.execute('''CREATE TABLE if not exists memes(
          server TEXT,
          trigger TEXT,
          response TEXT,
          FOREIGN KEY(server) REFERENCES servers(id)
)''')
conn.commit()
conn.close()
