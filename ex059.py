'''operação = 0
while operação != 5:
    operação = int(input("""Qual operação você deseja fazer?
    [1] Soma
    [2] Subtração
    [3] Divisão 
    [4] Multiplicação
    [5] Sair do programa"""))
    if operação == 5:
        print('Sair')
    else:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        if operação == 1:
            soma = n1+n2
            print('A soma de {}+{}={}'.format(n1,n2,soma))
        elif operação == 2:
            subtração = n1 - n2
            print('o resultado da subtração é {}-{}={}'.format(n1,n2,subtração))
        elif operação ==3:
            divisão = n1/n2
            print('O resultado da operação é {]/{}={}'.format(n1,n2,divisão))
        elif operação == 4:
            multiplicação = n1*n2
            print('O produto de {}x{}={}'.format(n1,n2,multiplicação))

        print('Sair')
print('Fim do Programa')'''

