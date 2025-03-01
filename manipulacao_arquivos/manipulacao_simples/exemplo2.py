def main():
    # Pede entrada de usuário para as frases
    print("Digite suas frases. Digite 'sair' para terminar e salvar o arquivo.")

    # Cria um array para armazenar as frases de entrada
    frases = []

    # loop infinito para Receber as frases e armazenar no array
    while True:
        entrada = input("> ") # Entrada recebendo um input 
        if entrada.lower() == "sair": # Condição para saída do programa
            break
        frases.append(entrada) # Recebimento dos dados no array

    # Abertura do arquivo em modo escrita
    with open("meu_arquivo.txt", "w") as arquivo:

        # Para cada frase em frases... 
        for frase in frases:
            arquivo.write(frase + "\n") # Escreva a frase + uma quebra de linha
    
    print("Arquivo original criado. Agora vamos manipular os dados.")
    dados_modificados = []
    with open("meu_arquivo.txt", "r") as arquivo:
        for linha in arquivo:
            dados_modificados.append(linha.strip().upper()) #Conversão para maiusculo
    
    # Sobrescrever arquivo com os dados que tenho em dados_modificados
    with open("meu_arquivo.txt", "w") as arquivo:
        for linha in dados_modificados:
            arquivo.write(linha + "\n")
            
    print("O arquivo foi sobrescrito com os dados modificados.")

if __name__ == "__main__":
    main()

