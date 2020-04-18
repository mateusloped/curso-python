#calculo de IMG: abaixo 18.5 abaixo; 18.5 ate 25 peso ideal; 25.1 até 30 sobrepeso; 30.1 até 40 obesidade; acima de 40 obesidade mórbida
peso = float(input('Digite seu peso {} KG '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print('Você está a baixo do peso "SECÃO"! ')
elif imc>18.5 >=25:
    print('Seu peso está ideal')
elif imc> 25.1 >=30:
    print('Você está com sobrepeso. ')
elif imc>30.1 >=40:
    print('Ta gordão, né fi? Partiu regime e academia')
elif imc >40:
    print('Ta gordo de mais rolha de poço, cirurgia já! \n Obesidade mórbida')

