#idade para se alistar com acrescimo de sexo criado por mim
from datetime import date
atual = date.today().year
print('      Alistamento obrigatório Militar')
print('Para sexo MASCULINO digite [1]\n Para sexo FEMININO digite [2] ')
sexo = int(input('Qual é o seu sexo? '))
if sexo == 1:
     nasc = int(input('Digite seu ano de nascimento: '))
     idade = atual - nasc
     print('quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
     if idade == 18:
          print('Você precisa se alistar imadiatamente')
     if idade < 18:
          saldo = 18 - idade
          print(' Ainda faltam {} anos para seu alistamento'.format(saldo))
          ano = atual + saldo
          print('Seu alistamento será em {}'.format(ano))
     if idade > 18:
          saldo = idade - 18
          print('Você deveria ter se alistado há {} anos '.format(saldo))
          ano = atual - saldo
          print('seu alistamento foi no ano {}'.format(ano))
else:
     print('Você não precisa se alistar')