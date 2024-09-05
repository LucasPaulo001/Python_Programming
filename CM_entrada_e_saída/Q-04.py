#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

res = input('Digite algo: ')
#métodos para verificar as características do tipo primitivo

#(type) => método para verificar o tipo da variável, como não convertemos para nenhum tipo ela será uma string
print('O tipo primitivo desse valor é', type(res))

#(isnumeric) => Verifica se a variável é numérica
print('É um número? ', res.isnumeric())

#(isspace) => Verifica se só foram informados espaços
print('Só tem espaços? ', res.isspace())

#(isalnum) => Verifica se é um alfanumérico
print('É alfanumérico? ', res.isalnum())

#(isalpha) => Verifica se é alfabético
print('É alfabético? ', res.isalpha())

#(isupper) => Verifica se foram informadas apenas letras maiúsculas
print('Está em maiúsculas? ', res.isupper())

#(islower) => Verifica se foram informadas apenas letras minúsculas
print('Está em minúsculas? ', res.islower())

#(iltitle) => Verifica se a primeira letra é maiúscula
print('A primeira letra é maiúscula? ', res.istitle())