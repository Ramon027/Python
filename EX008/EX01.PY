casa = float(input('Qual o valor da casa: R$'))
sal = float(input('Qual o salário do comprador: R$'))
anos = float(input('Quantos anos de financiamento:'))
prestação = casa / (anos * 12)
minimo = sal * 0.30

print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação sera de R$ {:.2f}'.format(prestação))
if prestação > minimo:
    print('Emprestimo NEGADO !')
else:
    print('Emprestimo CONCEDIDO !')

