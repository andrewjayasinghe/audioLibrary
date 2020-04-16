import sqlite3

conn = sqlite3.connect('song_db.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE song_tbl
          (song_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            artist TEXT NOT NULL,
            runtime TEXT,
            file_location TEXT NOT NULL,
            album TEXT NULL,
            genre TEXT NULL,
            date_added TEXT NULL,
            last_played TEXT,
            rating INTEGER,
            play_count INTEGER NOT NULL)
          ''')

conn.commit()
conn.close()
