from faker import Faker
from connect import conn, cursor

# Configurando gerador
fake = Faker('pt_BR')

for _ in range(50):
    nome = fake.word()
    preco = round(fake.random_number(digits=5) / 100, 2)
    print(nome, preco)
    
    cursor.execute('''
        INSERT INTO Produto (nome, preco) VALUES (%s, %s)
        ''', (nome, preco))
    
conn.commit()
print("Dados inseridos com sucesso!")

cursor.close()
conn.close()