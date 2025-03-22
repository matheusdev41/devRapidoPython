from mysql.connector import Error
from faker import Faker
from create_table import conn, cursor

class AppBD:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.connect_to_db()
        
    def connect_to_db(self):
        self.conn = conn
        self.cur = cursor
        print("Conexão com o Banco de Dados aberta com sucesso")
    
    def selecionar_dados(self):
        try:
            self.cur.execute("SELECT * FROM Produto ORDER BY codigo")
            registros = self.cur.fetchall()
            return registros
        except (Exception, Error) as error:
            print("Erro ao selecionar dados", error)
            return []
    
    def data_insert(self, nome, preco):
        try:
            self.cur.execute(
                '''INSERT INTO Produto (nome, preco) VALUES (%s, %s);''',
                (nome, preco)
            )
            self.conn.commit()
            print("Inserção realizada com sucesso")
        except (Exception, Error) as error:
            print("Erro ao inserir dados", error)
    
    def update_tables(self, codigo, nome, preco):
        try:
            self.cur.execute(
                '''UPDATE Produto SET nome = %s, preco = %s WHERE codigo = %s;''',
                (nome, preco, codigo)
            )
            self.conn.commit()
            print("Atualização realizada com sucesso")
        except (Exception, Error) as error:
            print("Erro ao atualizar o banco de dados", error)
            
    def data_delete(self, codigo):
        try:
            self.cur.execute(
                '''DELETE FROM Produto WHERE id = %s;''',
                (codigo)
            )
            self.conn.commit()
            print("Exclusão realizada com sucesso")
        except (Exception, Error) as error:
            print("Erro ao excluir registro", error)
            
if __name__ == '__main__':
    app_bd = AppBD()
    fake = Faker('pt-br')
    
    for _ in range(20):
        nome = fake.word()
        preco = round(fake.random_number(digits=5) / 100, 2)
        app_bd.data_insert(nome, preco)            
