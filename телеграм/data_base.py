from ast import Try
from pydoc import cli
from re import S, U
import sqlite3 as sl

con = sl.connect('userdata.db') #подключение базы данных к коду
cur = con.cursor() #курсор для навигации по базе данных

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            phonenumber TEXT NOT NULL,
            cardnumber TEXT NOT NULL,
            balance TEXT NOT NULL,
            cvc TEXT NOT NULL,
            cardvalidity TEXT NOT NULL,
            cardstatus TEXT NOT NULL,
            transmissionhistory TEXT,
            purchaseshistory TEXT
        );
    """)
sql = '''INSERT or REPLACE INTO users (id, name, phonenumber, cardnumber, balance, cvc, cardvalidity, cardstatus, transmissionhistory, purchaseshistory) 
                                       values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

data = [(1, 'Равиль', '89998887733', '1234123412341234', '1023', '020', 'АКТИВНА', '05,29','','[(Ашан капуста 999)]'),
       (2, 'Ксения', '87776665544', '5678567856785678', '2020', '202', '07,28','ЗАБЛОКИРОВАНА', '[(Ксения Владислав 100), (Равиль Ксения 50)]', '')]
with con:
    con.executemany(sql, data)

cur.execute("SELECT * FROM users;")
all_users = cur.fetchall()