largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
l = 1 
x = '#'
a = 1 
while a <= altura: 
   print(x * largura, end = '') 
   print() 
   a = a + 1 
   while a > 1 and a < altura: 
      print(x + ' ' * (largura - 2) + x) 
      a = a + 1 