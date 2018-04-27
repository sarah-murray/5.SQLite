import sqlite3


conn = sqlite3.connect('resultsdb.sqlite')
cursor =conn.cursor()

for row in cursor.execute('SELECT * FROM Results ORDER BY burglaries'):
    print(u'{1} burglaries have happened at {0}'.format(row[0], row[1]))