def change():
    expense = 23.75
    money = 100

    cambio = money - expense
    pesos = int(cambio)
    centavos = (cambio - pesos)*100

    print("Ingresar gasto:")
    print(expense)
    print("Dinero resivido:")
    print(money)
    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
