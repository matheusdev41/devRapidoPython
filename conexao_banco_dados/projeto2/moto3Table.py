import sqlite3 as conector

try:
    conexao = conector.connect('meu_banco.db')

    cursor = conexao.cursor()

    comando = '''ALTER TABLE veiculo
                    ADD motor REAL'''

    cursor.execute(comando)
    conexao.commit()
    
except conector.DatabaseError as err:
    print('Erro de banco de dados ', err)

finally:
    if conexao:
        cursor.close()
        conexao.close()