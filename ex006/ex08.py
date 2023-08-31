nome = str(input('Digite seu nome:')).strip()
print('Seu nome em maisculas é', nome.upper()) 
print('Seu nome em minusculas é', nome.lower()) 
print('Seu nome tem ao total de {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu  primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


