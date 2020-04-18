#PROGRAMA DE PAGAMENTO: DINHEIRO/CHEQUE 10% DE DESC.; A VISTA NO CARTÃO 5%; 2 VEZES PREÇO NORMAL; MAIS 3 OU MAIS 20% JUROS;
pag = float(input('Valor a ser pago:'))
print('''[1]DINHEIRO ou CHEQUE
 [2]A VISTA 
 [3]PARCELADO EM 2 VEZES 
 [4] PARCELADO EM 3X OU MAIS''')
forma = int(input('Qual a forma de pagamento? '))
if forma == 1:
    calc = pag - (pag * 10/100)
    print('Total a pagar R${} de R${}'.format(calc, pag))
elif forma == 2:
    calc = pag - (pag * 5/100)
    print('Total a pagar R${:.2f} de R${}'.format(calc, pag))
elif forma == 3:
    print('Total a pagar R${}'.format(pag))
elif forma == 4:
    calc = pag + (pag * 20 /100)
    print('Total a ser pago 3x ou mais R${}'.format(calc))
