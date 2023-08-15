print('figuras validas: \n',\
     '1.calculadora area del circulo \n',\
     '2.calculadora area del rectangulo \n',\
     '3.calculadora area del triangulo \n')

fig=input('ingrese el nombre de la figura: ')
a='NAN'

if (fig.lower()=='circulo'):
    r=int(input('ingrese el valor del radio: '))
    a=3.1416*r**2
elif(fig.lower()=='rectangulo'):
    b=int(input('ingrese el valor de la base: '))
    h=int(input('ingrese el valor de la altura'))
    a=b*h
elif(fig.lower()=='triangulo'):
    b=int(input('ingrese el valor de la base: '))
    h=int(input('ingrese el valor de la altura'))
    a=b*h/2
else:
    print('ingreso una opcion no valida.')
print('el valor del area es: ',a)