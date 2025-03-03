from datetime import datetime

frutas = ['Jabuticaba', 'Laranja', 'Uva', 'Banana']

for fruta in frutas: #{fruta:12} dá 12 espaços depois da variável para organizar o texto 
    minha_fruta = f"Nome: {fruta:12} - Números de letras: {len(fruta): 3}"
    print(minha_fruta)

print()

pi = 3.1415
meu_numero = f'O numero PI é: {pi:.1f}'
meu_numero_deslocado = f'O número PI deslocado é: {pi:6.1f}'
meu_numero_preciso = f'O numero PI mais preciso é: {pi:.4f}'

print(meu_numero)
print(meu_numero_deslocado)
print(meu_numero_preciso)

print()

data = datetime.now()
minha_data = f'A data de hoje é {data}'
minha_data_formatada = f'A data de hoje é {data:%d/%m/%Y}'

print(minha_data)
print(minha_data_formatada)