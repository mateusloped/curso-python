from random import randint

print('''[1]PEDRA
[2]PAPEL
[3]TESOURA''')
escolha = int(input('Escolha: '))
computador = randint(1, 3)
if computador == 1:
    print('Computador escolheu [PEDRA]')
    if escolha == 2:
        print('Você escolheu PAPEL \nVOCÊ GANHOU!')
    elif escolha == 3:
        print('Você escolheu TESOURA\n Você perdeu, tente novamente')
    elif escolha == 1:
        print('Você escolheu PEDRA\nEmpate, tente novamente')
elif computador == 2:
    print('Computador escolheu [PAPEL]')
    if escolha == 3:
        print('Você escolheu TESOURA\n VOCÊ GANHOU')
    elif escolha == 1:
        print('Você escolheu PEDRA \nVocê perdeu')
    elif escolha == 2:
        print('Você escolheu PAPEL \nEmpate, tente novamente')
elif computador == 3:
    print('Computador escolheu [TESOURA]')
    if escolha == 1:
        print('Você escolheu PEDRA\nVOCÊ GANHOU')
    elif escolha == 2:
        print('Você escolheu PAPEL \nVocê perdeu ')
    elif escolha == 3:
        print('Você escolheu TESOURA \nEmpate, tente novamente')
else:
    print('Opção invalida')
