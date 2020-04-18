from random import randint
print('-='*15)
print('VAMOS jOGAR PAR OU ÍMPAR')
print('-='*15)
v = 0
while True:
    n = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = n + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [p/I]? ')).strip().upper()[0]
    print(f'Você jogou {n} e o computador {computador}. O total é de {total}', end='')
    print('DEU PAR'if total %2 ==0 else 'DEU ÍMPAR' )
    if tipo == 'P':
        if total % 2 ==0 :
            v+= 1
            print('VOCÊ VENCEU !')
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2==1:
            v+=1
            print('VOCÊ VENCEU! ')
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes ')

