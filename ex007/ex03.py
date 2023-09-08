vel = float(input('Qual a velocidade atual do carro:'))
if vel <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
       m = (vel-80) * 7
       print('MULTADO! Você excedeu o limite permitido que é de 80km/h \nVocê deve pagar uma multa de R${}\n' 'Tenha um bom dia! Dirija com segurança!'.format(m))
     


