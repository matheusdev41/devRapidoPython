import os

arquivo = open('dados.txt', 'r', encoding='utf-8')

conteudo = arquivo.read()

print("Tipo de conteudo", type(conteudo))

print('Conteudo retornado pelo read:')

print(repr(conteudo))

arquivo.close()