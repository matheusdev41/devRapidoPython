import mysql.connector as conector
try:
    conn = conector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'loja1'
    )

    print("Conexão com o Banco de Dados aberta com sucesso")

except Error as e:
    print(f"Erro ao se conectar com o banco de dados: {e}")

cursor = conn.cursor()