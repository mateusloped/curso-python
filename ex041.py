#classificação de categoria por idade até 9 mirim; até 14 infantil;até 19 junior; até 20 senior; acima master
from datetime import date
nasc = int(input('Digite seu ano de nascimento para conferir sua categoria:'))
atual =  date. today().year
idade = atual - nasc

if 0< idade <= 9:
    saldo = 9 - idade
    print('Com {} anos você pertence a categoria MIRIM que vai até 9 anos'.format(idade))
    ano = atual + saldo
    print('No ano de {} você passará para a infantil. continue praticando.'.format(ano))


elif idade>=10 <= 14:
    saldo = 14 - idade
    print('Com {} anos você está na categoia INFANTIL que vai de 10 a 14 anos.'.format(idade))
    ano = atual + saldo
    print('No ano de {} você passará para a categoria Junior, continue praticando esportes.'.format(ano))


elif idade>=15 <=19:
    saldo = 19 - idade
    print('Com {} você classifica-se na categoria JUNIOR, que vai de 15 a 19 anos'.format(idade))
    ano = atual + saldo
    print('No ano de {} você passará para a catégoria Senior'. format(ano))


elif idade > 19 <=20:
    saldo = 20 - idade
    print('Com {} Você enqadra-se na categoria SENIOR,que vai até 20 anos. '.format(idade))
    ano = atual +saldo
    print('No ano de {} Você passará para a categoria Master '.format(ano))
    