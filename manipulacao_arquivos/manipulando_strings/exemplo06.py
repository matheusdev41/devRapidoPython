frase1 = "Eu amo comer amoras no café da manhã"

# Método split separando a string pelos espaços
lista_termos1 = frase1.split()
print(lista_termos1)

# Demonstrando que posso separar com um ou mais espaços
frase2 = "Amora abacaxi   abacate    banana"
lista_termos2 = frase2.split()
print(lista_termos2)

# Posso passar um parâmetro de separação para o split 
frase3 = "Carro,moto,avião"
lista_termos3 = frase3.split(',')
print(lista_termos3)