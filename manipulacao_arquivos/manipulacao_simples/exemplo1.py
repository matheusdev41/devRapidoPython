import os 

# Abrindo o arquivo em modo escrita 
arquivo = open('exemplo.txt', 'w', encoding='utf-8')

# Exibindo atributos 
print("Nome do arquivo: ", arquivo.name)
print("Modo de abertura: ", arquivo.mode)
print("Arquivo está fechado? ", arquivo.closed)

# Escrevendo no arquivo
arquivo.write('Olá mundo!')

# Fechando o arquivo
arquivo.close()

# Verificando se o arquivo foi fechado
print("Arquivo está fechado? ", arquivo.closed)

# Verificando conteúdo do arquivo 
with open('exemplo.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print('Conteúdo do arquivo: ', conteudo)

relpath = os.path.relpath('exemplo.txt')
abspath = os.path.abspath('exemplo.txt')

print('Caminho relativo do arquivo: ', relpath)
print('Caminho absoluto do arquivo: ', abspath)