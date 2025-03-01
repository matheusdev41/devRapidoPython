import os 

with open('dados.txt', 'r', encoding='utf-8') as arquivo:

    # Método readlines retorna todas as linhas
    conteudo = arquivo.readlines()

    print("Tipo de conteúdo", type(conteudo))

    print("Conteúdo retornado pelo read: ")

    print(repr(conteudo))

