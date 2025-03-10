import os

def processar_arquivo(arquivo_origem, arquivo_destino):
    try:
        with open(arquivo_origem, 'r', encoding='utf-8') as f_origem:
            conteudo = f_origem.read()
    except FileNotFoundError:
        print(f'Arquivo {arquivo_origem} não encontrado.')
        return
    except PermissionError:
        print(f'Sem permissão para ler {arquivo_origem}')
        return
    except Exception as e:
        print(f'Erro inesperado ao ler {arquivo_origem}')
        return
    
    try:
        with open(arquivo_destino, 'w', encoding='utf8') as f_destino:
            f_destino.write("Cabeçalho: Conteúdo do Arquivo\n")
            f_destino.write(conteudo)
            print(f"Conteúdo escrito em {arquivo_destino}.")
    except PermissionError:
        print(f'Sem permissão para escrever em {arquivo_destino}')
    except Exception as e:
        print(f'Erro inesperado ao escrever {arquivo_destino}')

def main():
    diretorio_trabalho = "diretorio_trabalho"
    arquivo_origem = os.path.join(diretorio_trabalho, "arquivo_origem.txt")
    arquivo_destino = os.path.join(diretorio_trabalho, "arquivo_destino.txt")

    processar_arquivo(arquivo_origem, arquivo_destino)

if __name__=="__main__":
    main()