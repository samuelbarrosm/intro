
print('Dada uma equação do segundo grau do tipo: ax^2 + bx + c')
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
delta = (b**2 - 4*a*c)
x = (-b + (delta)**(1/2))/2*a
y = (-b - (delta)**(1/2))/2*a
if (delta) > 0: 
     print('as raízes da equação são {} e {}.'.format(y,x))
else: 
     print('esta equação não possui raízes reais')
if  (delta) == 0:
     print('a raiz desta equação é {}.'.format(x))
      
      