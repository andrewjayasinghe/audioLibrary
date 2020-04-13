import sqlite3

conn = sqlite3.connect('song_db.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE songs
          (song_id TEXT PRIMARY KEY,
            song_url TEXT NOT NULL)
          ''')

conn.commit()
conn.close()
