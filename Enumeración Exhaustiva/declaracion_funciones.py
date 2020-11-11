def menu():
    print("""
    
    xxX Bienvenido al Programa de Soluciones Aproximadas para las raices cudradas Xxx

    Por favor, elija la opción de su preferencía:

    1.- Enumeración
    2.- Aproximacón
    3.- Busqueda Binaría
    
    """)

    opcion = int(input('Por favor ingrese la opción: '))

    if opcion == 1:
        print('Su selección fue Enumeración:')
        enum()
    elif opcion == 2:
        print('Su selección fue Aproximácion:')
        aprox()
    elif opcion == 3:
        print('Su selección fue Busqueda Binaría:1')
        busq()
    else:
        print('Su selección no existe :(')

def enum():
    objetivo = int(input('Escoje un entero: '))
    respuesta = 0

    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La Raiz cuadra de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')

def aprox():
    objetivo = int(input('Escoje un número: '))
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print( abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def busq():
    objetivo = int(input('Escoge un número: '))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo = {bajo}, alto={alto}, respuesta = {respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

menu()