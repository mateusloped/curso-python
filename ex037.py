# Conversor de decimal para binário, octal e hexadecimal
num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para hEXADECIMAL''')
opção = int(input('sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:])) # O dois é usado para fatiamento de palavra, assim não aparece os números de controle 0b+resultado
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:])) # O dois é usado para fatiamento de palavra, assim não aparece os números de controle 0o+ resultado
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {} '.format(num, hex(num)[2:]))# O dois é usado para fatiamento de palavra, assim não aparece os números de controle 0x+ resultado
else:
    print('Opção invalida, ANIMAL !')
