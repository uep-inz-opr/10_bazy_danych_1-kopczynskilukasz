## test 3

import csv
import sqlite3

con = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cur = con.cursor()
cur.execute('''CREATE TABLE polaczenia (from_subscriber data_type INTEGER,
                  to_subscriber data_type INTEGER,
                  datetime data_type timestamp,
                  duration data_type INTEGER ,
                  celltower data_type INTEGER);''')

def read_data(filename):
    with open(filename, 'r') as fin:
        reader = csv.reader(fin, delimiter=",")
        next(reader, None)
        rows = [x for x in reader]
        cur.executemany("INSERT INTO polaczenia (from_subscriber, to_subscriber, datetime, duration , celltower) "
                        "VALUES ( ?, ?, ?, ?, ?);", rows)
        con.commit()

if __name__ == "__main__":
    read_data(input())
    cur.execute('SELECT sum(duration) FROM polaczenia')
    print(cur.fetchone()[0])