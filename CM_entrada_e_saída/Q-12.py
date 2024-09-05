#Escreva um programa que leia o valor em reais que uma pessoa tem e depois informe quantos dólares equivale

reais = float(input('Informe o valor em reais: '))
dolar = reais/5.57
print(f'Valor de {reais} em dólares: {round(dolar, 2)}')

#round => função para controlar casas decimais