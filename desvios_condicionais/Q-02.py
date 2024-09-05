#Escreva um programa que leia dois números e determine se o segundo número é menor, igual ou maior que o primeiro.

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
if num1 > num2:
    print(f'O número {num1} é maior que o número {num2}')
elif num1 == num2:
    print('Os números informados são iguais')
else:
    print(f'O número {num2} é maior que o número {num1}')
     