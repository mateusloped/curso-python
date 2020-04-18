'''primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
c = 0
while c<10:
    print(primeiro, end='>>>')
    primeiro+= razão
    c+= 1
print('fim')'''
print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo da PA: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 0
while cont<= 10:
    print('{}>>>'.format(termo), end='')
    termo += razão
    cont +=1
print('FIM')
