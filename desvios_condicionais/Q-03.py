#Escreva um programa que leia dois números inteiros M e N e verifique se N é múltiplo de M.

m = int(input('Informe o primeiro número: '))
n = int(input('Informe o segundo número: '))
if n % m == 0:
    print(f'O número {n} é divisível por {m}')
else:
    print(f'O número {n} não é divisível por {m}')