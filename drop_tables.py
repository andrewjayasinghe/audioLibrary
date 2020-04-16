import sqlite3

conn = sqlite3.connect('song_db.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE sqlite_sequence
          ''')

conn.commit()
conn.close()
