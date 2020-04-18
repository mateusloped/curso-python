#calculando a média abaixo de 5 reprovado; entre 5 e 6.9 recuperação; acima de 7 aprovado;
n1 = float( input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2)/2

if média < 5:
    print(('Você não atinguiu a média. REPROVADO'))
elif média >= 5 >= 6.9 :
    print('Você tirou {:.2f}, precisa fazer a RECUPERAÇÃO'.format(média))
elif média >= 7:
    print('Você foi APROVADO.\nPARABÉNS!')
