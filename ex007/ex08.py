sal = float(input('Qual o valor do seu salário :R$'))
if sal <= 1250:
    aumento = (sal * 0.15) + sal
else:
    aumento = (sal * 0.10) + sal

print('Seu novo salário é : R${:.2F}'.format(aumento))