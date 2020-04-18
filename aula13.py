# ESTRUTURAS DE CONTROLE (REPETIÇÃO)
'''for c in range(0, 6):
    print('OI')
print('fim')'''

# o ultimo número é ignorado
'''for c in range(1,7):
    print(c)
print('fim')'''

# -1 que diz qual a ITERAÇÃO, neste caso, contagem regressiva
'''for c in range(6,0,-1):
    print(c)
print('fim')'''
# Com a ITERAÇÃO 2 ele diz que a estura deve mostrar de 2 em 2
'''for c in range(0, 7, 2):
    print(c)
print('FIM')'''

# ITERAÇÃO COM INPUT (O N+1 É PARA MOSTRAR O NÚMERO FINAL DIGITADO)
'''n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')'''
# Inicio, fim e de quanto em quantos passos desejo mostrar
'''i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo:'))
for c in range(i,f+1, p):
    print(c)
print('FIM')'''
# Colocando o input dentro do for ele repete quantas vezes você desejar
'''for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')'''
# Somatória dos números
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n  # S recebe(+=) N
print('O somatório de todos os valores foi {}'.format(s))
