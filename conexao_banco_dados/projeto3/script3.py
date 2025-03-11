import sqlite3 as conector

conexao = conector.connect('meu_banco.db')
cursor = conexao.cursor()

comando1 = '''CREATE TABLE IF NOT EXISTS pessoa_new (
                cpf INTEGER NOT NULL,
                nome TEXT NOT NULL,
                nascimento TEXT NOT NULL,
                oculos BOOLEAN NOT NULL,
                PRIMARY KEY (cpf)
                );'''

comando2 = '''DROP TABLE pessoa;'''

comando3 = '''ALTER TABLE pessoa_new RENAME TO pessoa;'''

#cursor.execute(comando1)
#cursor.execute(comando2)
cursor.execute(comando3)

conexao.commit()

cursor.close()
conexao.close()


