import sqlite3 as conector

try:
    # Abertura de conexão
    conexao = conector.connect('meu_banco.db')

    # Aquisição de cursor
    cursor = conexao.cursor()

    # Criando tabela Veiculo
    comando = '''CREATE TABLE IF NOT EXISTS veiculo (
    placa CHARACTER(7) NOT NULL,
    ano INTEGER NOT NULL,
    cor TEXT NOT NULL,
    proprietario INTEGER NOT NULL,
    marca INTEGER NOT NULL,
    PRIMARY KEY(placa),
    FOREIGN KEY(proprietario) REFERENCES pessoa(cpf)
    );'''

    cursor.execute(comando)

    # Efetivação do comando 
    conexao.commit()
    
except conector.DatabaseError as err:
    print("Erro no banco de dados", err)
    
finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()
