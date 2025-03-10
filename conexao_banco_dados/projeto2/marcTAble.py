import sqlite3 as conector

try:
    # Abertura de conexão
    conexao = conector.connect('meu_banco.db')

    # Aquisição do cursor
    cursor = conexao.cursor()

    # Criando tabela Marca
    comando = '''CREATE TABLE IF NOT EXISTS marca ( 
        id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        sigla CHARACTER(2) NOT NULL,
        PRIMARY KEY(id)
    );'''

    cursor.execute(comando)

    # Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados", err)
    
finally:
    if conexao:
        cursor.close()
        conexao.close()