import mysql.connector as conector

conn = conector.connect(
    host ='localhost',
    user = 'root',
    password = '',
    database = 'pytestes'
)

cursor = conn.cursor()

# Atualizar dados da tabela 
cursor.execute('''UPDATE Agenda 
                  SET nome = 'teste atualizado'
                  WHERE id = 1;''')

conn.commit()

# Ler dados 
cursor.execute('''SELECT * FROM Agenda;''')

rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, NOME: {row[1]}, TELEFONE: {row[2]}")

conn.commit()

if conn:
    cursor.close()
    conn.close()