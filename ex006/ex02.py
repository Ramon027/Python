
import math 
num1 = float(input('Comprimento do cateto oposto:'))
num2 = num1 = float(input('Comprimento do cateto adjacente :'))
hi = math.hypot(num1,num2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
