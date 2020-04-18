print('Emprestimo bancário')
casa = float(input('Qual o valor da casa que deseja comprar: R$'))
salário = float(input('Qual a sua renda mensal? '))
anos = int(input('Em quantos anos deseja pagar? '))

prestação = casa/(anos*12)
mínimo = salário * 30/100

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f} '.format(casa, anos , prestação))
if prestação <= mínimo:
    print('Seu credito foi aprovado')
else:
    print('Emprestimo negado!')
