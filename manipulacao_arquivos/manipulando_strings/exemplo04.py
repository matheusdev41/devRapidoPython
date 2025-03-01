import os 

with open('dados.txt', 'r', encoding='utf-8') as arquivo:
    count = 0
    print('Representação do arquivo')
    for linha in arquivo:
        print(repr(linha))
        if linha:
            count += 1
    print("Total de linhas = ", count)

with open('dados.txt', 'r', encoding='utf-8') as arquivo:
    count = 0
    print('Representação do arquivo')
    for linha in arquivo:
        linha_limpa = linha.strip()
        print(repr(linha_limpa))
        if linha_limpa:
            count += 1
    print("Total de linhas = ", count)