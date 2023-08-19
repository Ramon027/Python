sal = float(input('Qual e o salário do funcionário ? R$'))
aumento = sal + (sal * 15 / 100)
print('O funcionario que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(sal, aumento))