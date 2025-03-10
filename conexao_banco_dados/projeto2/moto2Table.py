import sqlite3 as conector

try:
    conexao = conector.connect('meu_banco.db')

    cursor = conexao.cursor()

    #comando1 = '''DROP TABLE veiculo;'''

    #cursor.execute(comando1)

    comando2 = '''CREATE TABLE IF NOT EXISTS veiculo (
                   placa CHARACTER(7) NOT NULL,
                   ano INTEGER NOT NULL,
                   cor TEXT NOT NULL,
                   motor REAL NOT NULL,
                   proprietario INTEGER NOT NULL,
                   marca INTEGER NOT NULL,
                   PRIMARY KEY(placa),
                   FOREIGN KEY(proprietario) REFERENCES pessoa(cpf),
                   FOREIGN KEY(marca) REFERENCES marca(id)
                   );'''
    
    cursor.execute(comando2)

    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados ",err)

finally:
    if conexao:
        cursor.close()
        conexao.close()