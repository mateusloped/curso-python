somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemvelho= ''
totmulher20 = 0
for p in range(1,5):
    print('-'*10,'{}pessoa'.format(p),'-'*10,)
    nome = input('Nome:').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo[M/F]: ').strip()
    somaidade += idade #somaidade = somaidade + idade
    if p==1 and sexo in 'mM':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'mM'and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho= nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1# totmulher20 = totmulher20 + 1
mediaidade = somaidade /4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos '.format(totmulher20))
