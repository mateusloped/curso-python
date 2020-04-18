'''#tuplas
lanche = 'hamburgaer', 'suco','Pizza','Pudim','Batata Frita'
#ambas tem o mesmo resultado
#Se nao for necessario utilizar a posicao
for comida in lanche:
    print(f'Eu vou comer {comida}')
for cont in range (0, len(lanche)):
    print(f' Eu vou comer {lanche[cont]} na posicao {cont}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}, na posicao {pos}')
print('comi pra caramba')



lanche = 'hamburgaer', 'suco','Pizza','Pudim','Batata Frita'

#vai organizar em ordem alfabetica
print(sorted(lanche))'''

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
# a e b são estruturas compostas, logo, a operação de baixo é diferente da de cima
'''c = b + a'''
#count index ... outros diversos metodos podem ser aplicados
print(c.count(4))
