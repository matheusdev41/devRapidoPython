import sqlite3 as conector
from modelo import Pessoa
from modelo import Marca

# Abertura de conexao
conexao = conector.connect('meu_banco.db')
cursor = conexao.cursor()

pessoa = Pessoa(60530833301, 'Maria', '1999-01-02', False)
pessoa2 = Pessoa(12345678918, 'Fernando', '1999-01-03', True)

marca = Marca(1, 'BMW', 'bmw')

#comando = '''
#INSERT INTO pessoa (cpf, nome, nascimento, oculos)
#VALUES (?, ?, ?, ?);'''

comando2 = '''
INSERT INTO marca (id, nome, sigla)
VALUES (?, ?, ?)'''

#cursor.execute(comando, (pessoa2.cpf,
#                         pessoa2.nome,
#                         pessoa2.data_nascimento,
#                         pessoa2.usa_oculos))

cursor.execute(comando2, (marca.id,
                         marca.nome,
                         marca.sigla))

conexao.commit()

cursor.close()
conexao.close()

