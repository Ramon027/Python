n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
media = (n1 + n2) / 2
if media > 7:
    print('Tirando {} e {}, a média é {}\n O aluno está APROVADO.'.format(n1, n2, media))
elif media > 5 and media < 6.9:
    print('Tirando {} e {}, a média é {}\n O aluno está de RECUPERAÇÃO.'.format(n1, n2, media))
else:
    print('Tirando {} e {}, a média é {}\n O aluno está REPROVADO.'.format(n1, n2, media))    
