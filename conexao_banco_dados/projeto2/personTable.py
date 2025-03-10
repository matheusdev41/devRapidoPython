import sqlite3 as conector

try:
    # Abertura de conexão
    conexao = conector.connect('meu_banco.db')  

    # Aquisição de cursor
    cursor = conexao.cursor()

    # Criando tabela Pessoa 
    comando = '''CREATE TABLE IF NOT EXISTS pessoa (
        cpf INTEGER PRIMARY KEY NOT NULL,
        nome TEXT NOT NULL,
        nascimento DATE NOT NULL,
        oculos BOOLEAN NOT NULL
    );'''
    
    cursor.execute(comando)

    # Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados:", err)

finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()
