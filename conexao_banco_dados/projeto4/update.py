import sqlite3 as conector

try:

    conexao = conector.connect('meu_banco.db')

    # Trabalhando respeitando as chaves estrangeiras
    conexao.execute("PRAGMA foreign_keys = on")

    cursor = conexao.cursor()

    #comando1 = '''UPDATE pessoa SET oculos= 1;'''
    #cursor.execute(comando1)

    comando2 = '''UPDATE pessoa SET oculos= ? WHERE cpf= 17375498318;'''
    cursor.execute(comando2, (False,))

    comando3 = '''UPDATE pessoa SET oculos= :usa_oculos WHERE cpf= :cpf;'''
    cursor.execute(comando3, {"usa_oculos": False,
                              "cpf": 12345678918})

    conexao.commit()

except conexao.DatabaseError as err:
    print("Erro no banco de dados: ", err)

finally:
    if conexao:
        cursor.close()
        conexao.close() 
