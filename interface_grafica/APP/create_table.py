import mysql.connector as conector 

conn = conector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'loja2'
)
print("Conexão com o Banco de Dados aberta com sucesso")

# Criação do cursor
cursor = conn.cursor()

if __name__=='__main__':
    # Criação da tabela
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Produto (
            codigo SERIAL AUTO_INCREMENT NOT NULL,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10, 2) NOT NULL,
            PRIMARY KEY(codigo)
            )
    ''')
    
    conn.commit()
    print("Tabela criada com sucesso!")
    conn.close()