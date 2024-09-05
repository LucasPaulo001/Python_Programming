#Escreva um programa que leia a idade de uma pessoa e verifique se ela é criança (0-12 anos), adolescente (13-17 anos), adulta (18-59) ou idosa (acima de 60 anos).

idade = int(input('Informe a idade: '))

if idade <= 12:
    print('Criança')
elif idade <= 17:
    print('Adolescente')
elif idade <= 59:
    print('Adulto')
else:
    print('Idoso')