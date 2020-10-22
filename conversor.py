pesos = input("¿Cuantos pesos Méxicanos tienes?: ")
pesos = float(pesos)
valor_dolar = 22.23
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dolares")