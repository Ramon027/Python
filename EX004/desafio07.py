alt = float(input('Qual a altura da parede:'))
larg = float(input('Qual a largura da parede:'))
area = alt * larg
print('Sua parede tem a dimensão de {} x {} e sua Area é de {} m²'.format(larg, alt, area))
tinta = area / 2
print('A quantidade de tinta necessária para pintar uma área de {} m² é de {} litros.'.format(area, tinta))