import mysql.connector as conector

conn = conector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'pytestes'
)

cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Agenda (
        id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
        nome VARCHAR(100) NOT NULL,
        telefone VARCHAR(15) NOT NULL
);""")

# Inserir dados na tabela 
cursor.execute("""INSERT INTO Agenda (nome, telefone)
                  VALUES ('Rosângela Assis', '31999498024');""")

cursor.execute("""INSERT INTO Agenda (nome, telefone)
                  VALUES ('Tadeu Lima','31992168160' );""")

conn.commit()

# Ler os dados

cursor.execute("""SELECT * FROM Agenda;""")

rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Nome: {row[1]}, Telefone: {row[2]}")
    
conn.commit()

# Fechar conexão
if conn:
    cursor.close()
    conn.close()