import pandas as pd
import sqlite3

path = r'C:\Users\RiccardoCazzola\OneDrive - ITS Incom\Desktop\Tutte\Pazzi\iot2\dati_sensori_IoT_novembre_2023.sql'

conn = sqlite3.connect(':memory:')

with open(path, 'r') as file:
    sql_script = file.read()
conn.executescript(sql_script)


query = "SELECT * FROM dati_sensori"
df = pd.read_sql_query(query,conn)

colonne_numeriche = df.select_dtypes(include=[int,float])

correlazioni = colonne_numeriche.corr()

print(correlazioni)

conn.close()
