#incrementado
m = 0
print('Escolha a TABUADA que deseja')
t = int(input('''[1]multiplicação 
[2]divisão 
[3]POTÊNCIA :'''))
n = int(input('Digite um número para ver sua tabuada:'))
for c in range(0, 11):
    if t ==1:
        m = n * c
        print('{}x{:2}={}'.format(c,n,m))
    elif t== 2:
        d = n *c
        print('{}/{:2}={}'.format(c, n, d))
    elif t == 3:
        p = n ** c
        print('{}^{:2}={}'.format(c, n, p))
