real = float(input('Quantos reais você tem na carteira ?'))
dol = real / 4.98
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dol))
