import math
num = float(input('Digite o angulo que voce deseja:'))
seno = math.sin(math.radians(num))
print('O angulo de {} tem o seno de {:.2f}'.format(num, seno))
cosseno = math.cos(math.radians(num))
print('O angulo de {} tem o cosseno de {:.2f}'.format(num, cosseno))
tangente = math.tan(math.radians(num))
print('O angulo de {} tem a tangente de {:.2f}'.format(num, tangente))
