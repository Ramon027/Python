from random import randint
from time import sleep
computador = randint(0,5)
print('-=-'* 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que numero eu pensei ?'))
print('PROCESSANDO...')
sleep(3)
if jogador > 5:
    print('Escolha apenas um número de 1 á 5')
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI ! Eu pensei no numero {} e não no número {}'.format(computador,jogador))    
