preço = float(input('Qual o preço do produto R$'))
desc = preço * (5 / 100)
tot = preço - desc 
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(preço, tot))