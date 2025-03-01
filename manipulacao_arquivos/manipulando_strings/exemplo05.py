with open('dados.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    count = texto.count("Olá")
    
    print(repr(texto))
    print("Total de Olás = ", count)