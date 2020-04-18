menor = total = totmil = cont = 0
print('Loja virtual')
barato =''
while True:
    produto = str(input('Produto: '))
    preco = float(input('preco do produto: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
         totmil += 1
    if cont == 1 or preco < preco:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print(f'A o valor total dos produtos foi de R${total:.2f}')
print(f'Total de produtos valendo mais de R$1000:  {totmil}')
print(f'O produto mais barato foi o {barato} e o seu preco foi de R${preco:.2f}')