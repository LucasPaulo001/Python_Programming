#Faça um programa que leia um número e informe o seu dobro, o seu triplo e a sua raiz quadrada

#importando a biblioteca math para usar a função sqrt(calcular raíz quadrada)
import math

num = int(input('Informe um número: '))
dobro = num*2
triplo = num*3
raiz = math.sqrt(num)
print(f'Dobro: {dobro}\nTriplo {triplo}\nRaiz quadrada {raiz}')