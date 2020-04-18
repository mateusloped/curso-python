#meu primeiro exercicio feito com bugs
'''conth = contm = contmaior = contmmenor  = 0
siga = 'Ss'
while True:
    if siga in 'Ss':
        print('-' * 15)
        print('CADASTRE UMA PESSOA')
        print('-' * 15)
        idade = int(input('Digite a idade:  '))
        sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
        print('-' * 15)
        siga = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if idade >= 18:
            contmaior += 1
        if sexo in 'Mm':
            conth += 1
        elif sexo in 'Ff':
            contm += 1
            if idade < 20:
                contmmenor += 1
    elif siga in 'Nn':
        break
print('=' * 30)
print('=' * 10, 'FIM DO PROGRAMA', '=' * 10)
print(f'{contmaior} Pessoas foram cadastradas com mais de 18 anos')
print(f'{conth} Homens foram cadastrados')
print(f'{contmmenor} Mulheres tem menos de 20 anos')'''
# programa feito por Guanabara
tot18 = toth = totm20 = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    print('-'*20)
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{tot18} pessoas foram cadastradas com mais de 18')
print(f'{toth} homens foram cadastrados')
print(f'{totm20} mulheres foram cadastradas com mais de 20 anos')
print('='*10, 'FIM DO PROGRAMA', '='*10)

