import sqlite3 as conector 
from modelo import Pessoa

try:
    # Abertura da conexão
    conexao = conector.connect('meu_banco.db')

    # Aquisição de cursor
    cursor = conexao.cursor()

    # Crição de um objeto Pessoa
    pessoa = Pessoa(17375498318,'jose', '1990-02-28', False)
    
    comando = '''INSERT INTO pessoa (cpf, nome, nascimento, oculos)
                    VALUES (:cpf, :nome, :data_nascimento, :usa_oculos);'''
    
    cursor.execute(comando, {"cpf": pessoa.cpf,
                             "nome": pessoa.nome,
                             "data_nascimento": pessoa.data_nascimento,
                             "usa_oculos": pessoa.usa_oculos})

    # Efetivação do comando

    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados: ", err)

finally:
    if conexao:
        cursor.close()
        conexao.close()