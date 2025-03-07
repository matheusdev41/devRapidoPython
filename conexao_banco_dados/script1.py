import sqlite3 as conector

# Abertura de conexão
conexao = conector.connect("sensor.db")

# Aquisição de um cursor
cursor = conexao.cursor()

# Execução comandos: SELECT..CREATE...
cursor.execute("""
CREATE TABLE IF NOT EXISTS leituras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperatura REAL NOT NULL,
    data_hora TEXT NOT NULL
);
""")

#Inserir uma leitura de temperatura
cursor.execute("INSERT INTO leituras (temperatura, data_hora) VALUES (?, ?)", (25.5, "2025-03-06 12:30:00"))
cursor.execute("INSERT INTO leituras (temperatura, data_hora) VALUES (?, ?)", (30.3, "2025-03-07 12:32:00"))
# Confirmação de inserção
conexao.commit()

# Consultar todas as leituras
cursor.execute("SELECT * FROM leituras")
dados = cursor.fetchall() # Retorna todos os dados da consulta
 
# Exibir os dados
for linha in dados:
    print(linha)

# Fechamento das conexões
cursor.close()
conexao.close()