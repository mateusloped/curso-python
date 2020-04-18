#Fatiamento de strings
frase = 'Curso em Video Python'
#pega somente uma letra
frase[9]


#fatiamento de espacos especificos
frase[9:13]#Ira fatiar da string 9(V) ate 13 mas ira exibir ate o 12(e)
frase[:9]#vai do inicio ate o caractere 9(sendo que mostrara ate o 8)
frase[9:]#mostra de 9 ate o ultimo caractere
frase[::2]#mostra dos os caracteres pulando de dois em dois 
frase[9:21:2]
#Analise de strings

frase.replace('Python','Android')# substitui Phyton por Android

frase.upper()#coloca todas as letras em maiusculo
#Esse metodo diz quantas caracteres tem na frase
frase = 'Curso em Video Python'
len(frase)
frase.strip()#remove os espacos antes e depois da frase
frase.lstrip()#remove o espaco a esquerda
frase.rstrip()#remove o espaco a esquerda



frase.split() #transforma as palavras separadas por espaco em "blocos" de uma lista (strings separadas)

'-'.join(frase)#junta os blocos, onde tinha espaco fica com um traco (junta os strings com traco )
#Este metodo conta quantos determinados caracteres aparecem (So as maiusculas ou minusculas)
frase.count('o', 0, 13)
