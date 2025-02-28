from PIL import Image
import numpy as np

def main():
    # Carregar a imagem original
    img = Image.open("monalisa.jpg")

    # Converter a imagem em dados binários
    img_data = np.array(img)
    binary_data = img_data.tobytes()

    print("\n", img_data.shape, "\n")

    # Salvar os dados bináriios em um arquivo
    with open("monalisa_img.bin", "wb") as file:
        file.write(binary_data)

    # Copiar o arquivo binário
    with open("monalisa_img.bin", "rb") as original_file:
        data = original_file.read()  # Lendo o arquivo original

    with open("copy_monalisa_img.bin", "wb") as copy_monalisa:
        copy_monalisa.write(data) # Fazendo cópia


    # Manipulação dos dados do arquivo binário cópia
    # Exemplo: Inverter os bytes 
    data = bytearray(data) # Convertendo para bytearray para manipulação
    data.reverse() # Invertendo todos os bytes 

    with open("copy_monalisa_img.bin", "wb") as file:
        file.write(data)

    # Carregar e mostrar imagem manipulada
    modified_data = np.frombuffer(data, dtype=np.uint8).reshape(img_data.shape)

    #inverte todos os bytes
    modified_data = np.fliplr(modified_data)

    modified_img = Image.fromarray(modified_data)
    modified_img.show()

if __name__ == "__main__":
    main()