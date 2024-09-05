#Um banco está realizando uma grande promoção em seus financiamentos. Ele financia qualquer valor em 5 prestações. O valor da primeira prestação corresponde à 20% do valor do empréstimo. Os valores das demais prestações correspondem ao valor da parcela anterior acrescido de uma taxa de juros de 7%. Com base nestas informações, escreva um programa que leia o valor a ser financiado por um cliente e calcule: ovalor de cada prestação, o valor total que o cliente vai pagar pelo empréstimo e o total de juros que o cliente vai pagar pelo empréstimo.

#'TAXA' é a variável fixa para expecificar os juros 7/100
TAXA = 0.07 


valor = float(input('Informe o valor a ser financiado: '))
prestacoes = valor/5
prestacao_01 = prestacoes + (prestacoes * TAXA)
prestacao_02 = prestacao_01 + (prestacao_01 * TAXA)
prestacao_03 = prestacao_02 + (prestacao_02 * TAXA)
prestacao_04 = prestacao_03 + (prestacao_03 * TAXA)
prestacao_05 = prestacao_04 + (prestacao_04 * TAXA) 
print(f'Primeira prestação: {prestacao_01}\nSegunda prestação: { prestacao_02}\nTerceira prestação: {prestacao_03}\nQuarta prestação: {prestacao_04}\nQuinta prestação{prestacao_05}')