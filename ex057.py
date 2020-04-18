#escreva um programa que a pessoa vai digitar o sexo, se for diferente de m ou f solicite que tente novamente
sexo = str(input('Digite o seu sexo[M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos, digite seu sexo novamente: ')).upper().strip()[0]
print('Sexo {} computado com sucesso'.format(sexo))
