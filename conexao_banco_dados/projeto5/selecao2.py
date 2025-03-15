import sqlite3 as conector 
import os 
from modelo import Pessoa

# Abertura de conexao
base_dir = "c:/Users/User/Desktop/faculdade/CIÊNCIA DA COMPUTAÇÃO/DEVRAPPYTHON/conexao_banco_dados"
db_path = os.path.join(base_dir, "meu_banco.db")

conexao = conector.connect(db_path)
cursor = conexao.cursor()

# Definição de comandos
comando = '''SELECT * FROM pessoa WHERE oculos= :usa_oculos;'''

cursor.execute(comando, {"usa_oculos": True})

# Recuperação de registros 

registros = cursor.fetchall()

for registro in registros:
    pessoa = Pessoa(*registro)
    print("cpf: ", type(pessoa.cpf), pessoa.cpf)
    print("nome: ", type(pessoa.nome), pessoa.nome)
    print("nascimento: ", type(pessoa.data_nascimento), pessoa.data_nascimento)
    print("oculos", type(pessoa.usa_oculos), pessoa.usa_oculos)

# Fechamento de conexões
cursor.close()
conexao.close()