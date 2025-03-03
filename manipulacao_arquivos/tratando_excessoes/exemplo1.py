# PermissionError, FileExistsError e FileNotFoundoError

try:
    # Tentativa de criar um arquivo em um diretório protegido por permissões
    with open("/ditetorio_protegido/arquivo.txt", "w") as arquivo:
        arquivo.write("Conteúdo do arquivo")
except PermissionError:
    print("Você não tem permisssão para criar o arquivo.")

try:
    # Tentativa de criar um arquivo que já existe
    with open("arquivo_existente.txt", "x") as arquivo:
        arquivo.write("Conteúdo do arquivo")
except FileExistsError:
    print("O arquivo já existe")
try:
    #Tentativa de abrir um arquivo que não existe
    with open("arquivo_inexistente.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")

