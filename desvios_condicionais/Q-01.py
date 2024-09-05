#Escreva um programa que leia um número inteiro e verifique se ele é par ou ímpar.

num = int(input('Informe um número inteiro: '))
if num % 2 == 0:
    print(f'O número {num} é PAR')

else:
    print(f'O número {num} é ÍMPAR')

