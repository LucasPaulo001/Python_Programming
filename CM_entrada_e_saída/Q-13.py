#Escreva um programa que leia a largura e a altura de uma parede em metros calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

largura = float(input('Informe a largura: '))
altura = float(input('Informe a altura: '))
area = largura*altura
unidade_litro = area/2
print(f'Área: {area}\nQuantidade de tinta necessária: {unidade_litro}L')