from connect import conn, cursor

# Criação de tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Produto (
        codigo INT AUTO_INCREMENT NOT NULL,
        nome VARCHAR(100) NOT NULL,
        preco NUMERIC(10, 2) NOT NULL,
        PRIMARY KEY (codigo)
    );
''')

# just in case 
conn.commit()
print("Tabela criada com sucesso!")
conn.close()