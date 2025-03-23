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
    
    def data_update(self, codigo, nome, preco):
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
            confirmation = input(f"Tem certeza que deseja excluir o produto com o codigo {codigo}? (s/n)")
            if confirmation  != 's':
                print("Exclusão cancelada.")
                return
            
            self.cur.execute(
                '''DELETE FROM Produto WHERE codigo = %s;''',
                (codigo,)
            )
            self.conn.commit()
            print("Exclusão realizada com sucesso")
        except (Exception, Error) as error:
            print("Erro ao excluir registro", error)
    
    def close_connection(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        print("Conexão com Banco de Dados fechada.")
            
if __name__ == '__main__':
    app_bd = AppBD()
    fake = Faker('pt-br')
    
    for _ in range(20):
        nome = fake.word()
        preco = round(fake.random_number(digits=5) / 100, 2)
        app_bd.data_insert(nome, preco)
        app_bd.close_connection()            
