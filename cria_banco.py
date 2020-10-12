import sqlite3

connection = sqlite3.connect("banco.db")
cursor = connection.cursor()


criar_tabela = "CREATE TABLE IF NOT EXISTS hoteis(" \
               "hotel_id int PRIMARY KEY," \
               "nome text," \
               "estrelas real," \
               "diaria real," \
               "cidade text" \
               ")"

criar_hotel = "INSERT INTO hoteis VALUES(1,'alpha hotel',2.3, 250, 'Fortaleza')"

cursor.execute(criar_tabela)
cursor.execute(criar_hotel)
connection.commit()
connection.close()