# INSERIR VALORES EM CRIAÇÃO
import sqlite3 as conector

conexao = conector.connect('meu_banco.db')
cursor = conexao.cursor()

comando = '''INSERT INTO pessoa (cpf, nome, nascimento, oculos)
             VALUES (07375498318, 'João', '2000-01-01', 1);'''

cursor.execute(comando)

conexao.commit()

cursor.close()
conexao.close()