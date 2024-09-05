#Escreva um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input('Informe o preço do produto: '))
desconto = preco - (preco*0.05)
print(f'Preço: {preco}\nPreço com desconto: {desconto}')