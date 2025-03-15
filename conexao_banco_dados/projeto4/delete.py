import sqlite3 as conector

try:
    conexao = conector.connect('meu_banco.db')
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    comando = '''DELETE FROM Pessoa WHERE cpf= 12345678918;'''
    cursor.execute(comando)

    conexao.commit()

except conexao.DatabaseError as err:
    print("Erro no banco de dados: ", err)
finally:
    if conexao:
        cursor.close()
        conexao.close()