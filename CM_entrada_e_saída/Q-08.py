#Escreva um programa que leia um valor em metros e transforme para cm e mm

metro = float(input('Informe o valor em metros: '))
cm = metro*100
mm = metro*1000
print(f'Valor em cm: {cm}\nValor em mm: {mm}')