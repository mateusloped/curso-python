'''from math import factorial
print(factorial(int(input('Digite um número para saber o seu fatorial: '))))'''
#Calculo fatorial sem usar a biblioteca math 
n = int(input('Digite um número para calcular o seu FATORIAL: '))
c = n
f = 1
print('Calcule {}! = '.format(c), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x 'if c > 1 else ' = ', end = '')
    f*=c
    c-= 1
print('{}'.format(f))
