x = int(input('Por favor, entre com o número de segundos que deseja converter: '))
a = x//86400
b = (x - a*86400)//3600
c = (x - b*3600 - a*86400)//60
d = (x - c*60 - b*3600 - a*86400)
print('{} dias, {} horas, {} minutos e {} segundos.'.format(a,b,c,d))