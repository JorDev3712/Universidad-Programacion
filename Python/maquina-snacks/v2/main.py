# Crear variable de snacks
from snacks import Snacks

# Codigo principal

# Variable para guardar las compras
snacks = Snacks()
shopping_cart = []

# Show title and snacks available
print('*** Maquina de Snacks ***')
print(' Snacks Disponibles:')
print(snacks.__str__())

# Crear variable para while y menu
exit = False
while not exit:
    print(f'''Menu:
    1. Comprar Snack.
    2. Mostrar ticket.
    3. Salir''')
    # Obtener la opción desde la consola
    option = int(input(' Escoge una opcion: '))
    if option == 1: # Comprar snack
        # Obtener el id del snack de la consola
        snack_id = int(input(' Que snack quieres (id)?: '))
        found = False
        for snack in snacks.list_snacks:
            if snack_id == snack.id:
                shopping_cart.append(snack)
                found = True
                print(f'Ok, snack agregado: {snack}')
        if found == False:
            print(f'No se encontró un snack con el id:{snack_id}')
            print(' Snacks Disponibles:')
            print(snacks.__str__())
    elif option == 2: # Mostrar ticket
        # Mostrar titulo de ticket
        print('*** Ticker de Venta ***')
        cost_total = 0
        for shop in shopping_cart:
            print(f'- {shop['name']} - S/{shop['cost']}')
            cost_total += shop['cost']
        print(f'TOTAL -> {cost_total}')
    elif option == 3:
        exit = True
        print('Saliendo del Maquina de Snacks. Hasta pronto...')
    else:
        print('La opcion ingresada no exite, por favor selecciona una opcion correcta.')