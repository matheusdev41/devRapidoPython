import sqlite3 as conector

# Abertura de conexão
conexao = conector.conect('meu_banco.dp')

# Aquisição de cursor
cursor = conexao.cursor()

# Criando tabela Pessoa 
comando = '''CREATE TABLE IF NOT EXISTS pessoa (
cpf INTEGER PRIMARY KEY NOT NULL
nome TEXT NOT NULL
nascimento DATE NOT NULL
oculos BOOLEAN NOT NULL
);'''

cursor.execute(comando)

# Efetivação do comando
conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()

# Criando tabela marca
comando = '''CREATE TABLE IF NOT EXISTS marca(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL
sigla CHARACTER(2) NOT NULL
)'''