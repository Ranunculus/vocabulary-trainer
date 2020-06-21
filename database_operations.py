import sqlite3

def get_connection():
    return sqlite3.connect('vocabulary.sqlite')


def init_database():
    conn = sqlite3.connect('vocabulary.sqlite')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Words
        (id INTEGER PRIMARY KEY, word TEXT, transcription TEXT, translation TEXT)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Trainings
        (id INTEGER PRIMARY KEY, word_id INTEGER, successes INTEGER, failures INTEGER, last_failure REAL,
        FOREIGN KEY(word_id) REFERENCES Words(id))''')
    cur.close()
    conn.close()



def create_new_words(rows):
    connection = get_connection()
    cursor = connection.cursor()
    for row in rows:
        cursor.execute('INSERT OR IGNORE INTO Words (word, transcription, translation) VALUES ( ?, ?, ? )',
                       (row['word'], row['transcription'], row['translation']))
    connection.commit()
    cursor.close()
    connection.close()
