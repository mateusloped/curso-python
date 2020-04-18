times = 'CORITIANS' ,'PALMEIRAS','SANTOS','GREMIO','CRUZEIRO','FLAMENGO','VASCO','CHAPECOENSE','ATLETICO','BOTAFOGO','ATLETICO-PR','BAHIA','SAO PAULO','FLUMINENCE','ESPORTE','VITORIA','CORITIBA','AVAI','PONTE PRETA','ATLETICO GOIANIENSE '
print('Times do BRASILEIRÃO: ', times)
print('Os cinco primeiros times sao', end='')
print(times[0:5])
print('Os ultimos quatro times são: ' ,end='')
print(times[-4:])
print(f'Times em ordem alfabetica{sorted(times)}')
print(f'O time Chapecoense está na {times.index("CHAPECOENSE")+1}ª posiçao')
