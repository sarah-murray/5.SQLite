import sqlite3


conn = sqlite3.connect('resultsdb.sqlite')
cursor =conn.cursor()

#cursor.execute("CREATE TABLE Results (address text, burglaries integer)")
cursor.execute("INSERT INTO Results VALUES ('Queen Vic', 2)")
conn.commit()

conn.close()