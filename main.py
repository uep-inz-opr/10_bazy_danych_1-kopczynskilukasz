## test kodu
import csv
import sqlite3
from datetime import date

if __name__ == "__main__":
    sqlite_con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cur = sqlite_con.cursor()
    cur.execute("""CREATE TABLE polaczenia (from_subscriber data_type INTEGER, 
                    to_subscriber data_type INTEGER, 
                    datetime data_type timestamp, 
                    duration data_type INTEGER , 
                    celltower data_type INTEGER);""") 
    filename = input()
    
    with open(filename,'r') as fin: 
        reader = csv.reader(fin, delimiter = ";")
        next(reader, None)  
        rows = [x for x in reader]
        cur.executemany("INSERT INTO polaczenia (from_subscriber, to_subscriber, datetime, duration , celltower) VALUES (?, ?, ?, ?, ?);",  rows)
        sqlite_con.commit()
        
    cur.execute("Select sum(duration) from polaczenia")
    result = cur.fetchone()[0]

    print(int(result))
