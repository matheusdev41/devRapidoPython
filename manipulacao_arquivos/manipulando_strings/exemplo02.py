import os 

with open('dados.txt', 'r', encoding='utf-8') as arquivo:

    # Método readline() retorna apenas a primeira linha do arquivo
    conteudo = arquivo.readline()

    print("Tipo de conteúdo: ", type(conteudo))

    print("Conteudo retornado pelo readline: ")
    print(repr(conteudo))

    proximo_conteudo = arquivo.readline()

    print("Proximo conteúdo retornado: ")
    print(repr(proximo_conteudo))