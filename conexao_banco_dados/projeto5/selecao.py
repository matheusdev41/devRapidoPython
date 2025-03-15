import sqlite3 as conector

def conectar_banco(nome_banco):
    conexao = conector.connect(nome_banco)
    return conexao

def selecao_tabelas(conexao):
    cursor = conexao.cursor()
    comando = '''SELECT quantidade, data_pedido FROM Pedidos;'''
    cursor.execute(comando)

    registros = cursor.fetchall()
    print("Tipo retornado pelo fetchall(): ", type(registros))

    for registro in registros:
        print("Tipo: ", type(registro), " - Conteúdo: ", registro)

    cursor.close()

if __name__ == '__main__':
    conexao = conectar_banco('ecommerce.db')
    selecao_tabelas(conexao)

    conexao.close()