#Escreva um programa que leia o número total de questões existentes em uma prova e o número de questões que um candidato acertou e determine o seu percentual de acertos e o seu percentual de erros.

total_quest = int(input('Informe o total de questões da prova: '))
acertos = int(input('Infomre a quantidade de questões certas: '))
erros = total_quest - acertos
por_acertos = (acertos*100)/total_quest
por_erros = (erros*100)/total_quest
print(f'Porcentagem de acertos: {por_acertos}%\nPorcentagem erros: {por_erros}%')

