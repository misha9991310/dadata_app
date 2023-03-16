import sqlite3


def create_db(token, secret, language):
    conn = sqlite3.connect('oreders.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS parameters(
                    token text, 
                    api text, 
                    language text)''')
    settings = (token, secret, language)
    cur.execute("insert into parameters values (?, ?, ?);", settings)
    conn.commit()


def parameters():
    conn = sqlite3.connect('oreders.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM parameters')
    result = cur.fetchall()
    conn.commit()
    return result


def exit():
    conn = sqlite3.connect('oreders.db')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS parameters')
    conn.commit()
