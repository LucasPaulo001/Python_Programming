#Escrever um programa que leia o dia o mês e o ano de nascimento e informar a data formatada

#Armazenando as informações lidas com o tipo 'int' nas respectivas variáveis
dia = int(input('Informe o dia de nascimento: '))
mes = int(input('Informe o mês de nascimento: '))
ano = int(input('Informe o ano de nascimento: '))

#Agora usamos outro método para informar dados ao usuário, o método 'format', abaixo nós colocamos o 'f' fora das aspas e em cada chaves a variável que será informada 
print(f'Data de nascimento: {dia}/{mes}/{ano}')

# Outro exemplo de formas de informar: print('{}/{}/{}'. format(dia, mes, ano))
