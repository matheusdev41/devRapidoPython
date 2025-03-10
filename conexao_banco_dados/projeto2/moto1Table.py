import sqlite3 as conector

try:
    # Abertura de conexão
    conexao = conector.connect("meu_banco.db")

    # Aquisição do cursor
    cursor = conexao.cursor()

    comando = '''ALTER TABLE veiculo
                    ADD motor REAL;'''

    cursor.execute(comando)

    # Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    # Fechamento de conexão
    if conexao:
        cursor.close()
        conexao.close()