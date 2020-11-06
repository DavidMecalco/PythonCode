num1_ = int(input('Escoje un entero: '))
numer2 = int(input('Escoje otro numero: '))

if num1_ > numer2: 
    print('El primer numero es mayor que el segundo')
elif num1_ < numer2:
    print('El segundo numero es mayor que el primero')
else:
    print('Los dos numeros son iguales')

print(""" 
    Bienvenidos, este es un programa que compara las edades de dos personas
    Por favor necesito que ingreses las edades para poder compararlas,
    Espero que te guste el programa ;)
""")

edad1 = int(input('Cuales las edad de la primera personas: '))
edad2 = int(input('Cual esa la edad de la seguna personas: '))

if edad1 > edad2:
    print('La primera persona tiene más años que la segunda')
elif edad2 < edad1:
    print('La segunda tiene más años que la primera')
else:
    print('Las dos personas tiene la misma edad')

print('Vuelva pronto')