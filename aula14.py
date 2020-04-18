#codigo com a quantidade de repetição determinada
'''for c in range(1,10)
    print(c)
print('fim')'''
#igual ao for
c = 1
'''while c < 10:
    print(c)
    c=+ 1
print('fim')'''
#lendo o número até chegar a 0

'''while n != 0 :
    n = int(input('Digite um valor: '))
print('fim')'''
#continua até o você apertar digitar N
'''r = 'S'
while r == 'S':
    n = int(input("digite um valor: "))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')'''
#mostrar todos os números pares e impares digitados parando com o zero (o zero não conta)

n = 1
par = impar = 0
while n !=0:
    n = int(input('Digite um valor: '))
    if n!= 0:
        if n % 2 == 0:
            par += 1
        else:
            impar +=1
print('Você digitou {} números pares e {]números ipares'.format(par, impar))