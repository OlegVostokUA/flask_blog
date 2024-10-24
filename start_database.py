import sqlite3


conn = sqlite3.connect('database.db')

with open('shema.sql') as f:
    conn.executescript(f.read())

cur = conn.cursor()

cur.execute('INSERT INTO posts (title, content) VALUES (?,?)',
            ('First post', 'Text of first post, Text of first post')
            )

cur.execute('INSERT INTO posts (title, content) VALUES (?,?)',
            ('Second post', 'Text of second post, Text of second post')
            )

conn.commit()
conn.close()