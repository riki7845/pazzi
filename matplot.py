import matplotlib.pyplot as plt

import sqlite3 as sql
import pandas as pd


path = r'C:\Users\RiccardoCazzola\OneDrive - ITS Incom\Desktop\Tutte\Pazzi\iot2\dati_sensori_IoT_novembre_2023.sql'

conn = sql.connect(':memory:')

with open(path, 'r') as file:
    sql_script = file.read()
    conn.executescript(sql_script)


query = "SELECT * FROM dati_sensori"
df = pd.read_sql_query(query,conn)




df['Data'] = pd.to_datetime(df['Giorno'])

media_giorno = df.groupby(df['Data'].dt.date)['Temperatura'].mean()

media_giorno.plot(kind='line')
plt.title('media giorno temperatura')
plt.xlabel('Data')
plt.ylabel('Temperatura')
plt.show()

conn.close()