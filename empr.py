casa = float(input('Qual o valor da casa: R$ '))
salario = float(input('Salario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos, a prestação será de R$ {prestacao:.2f}.')
if prestacao <= minimo:
    print('Emprestimo pode ser APROVADO!')
else:
    print('Emprestimo NEGADO!')