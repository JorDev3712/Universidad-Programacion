#Mostramos el título
print("*** Cajero Automatico de Ciudad Gotica ***")
# Crear variable de saldo
money = 1000.00
# Crear variable para while
exit = False
while not exit:
    print('''Operaciones que puedes realizar:
    1. Consultar tu saldo
    2. Retirar
    3. Depositar
    4. Salir''')
    #Leer la opción de la consola y convertirlo a entero
    option = int(input("Escoje una opcion: "))
    if option == 1:
        print(f"Tu saldo actual es: ${money}")
    elif option == 2:
        money_left = int(input("Ingresa monto a retirar: "))
        if money_left < 0:
            print("No puedes retirar un monto negativo.")
            continue

        if money_left > money:
            print("No tienes suficiente saldo para retirar ese monto.")
        else:
            money -= money_left
        print(f"Tu saldo actual es: ${money}")
    elif option == 3:
        money_add = int(input("Ingresa el monto a depositar: "))
        if money_add < 0:
            print("No puedes depositar un monto negativo.")
            continue

        money += money_add
        print(f"Tu nuevo saldo: ${money}")
    elif option == 4:
        exit = True
        print("Saliendo del cajero automatico. Hasta pronto...")
