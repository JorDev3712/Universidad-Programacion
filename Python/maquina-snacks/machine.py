# Crear variable de snacks
snacks = [
    {'id': 0, 'name': 'Papas', 'cost': 2.5},
    {'id': 1, 'name': 'Gaseosa', 'cost': 3.00},
    {'id': 2, 'name': 'Sandwich', 'cost': 8.9}
]
# Variable para guardar las compras
shopping_cart = []
# Mostrar título y snacks disponibles
print('*** Maquina de Snacks ***')
print(' Snacks Disponibles:')
for snack in snacks:
    print(f'\tId: {snack['id']} -> {snack['name']} - Precio: S/{snack['cost']}')

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
        for snack in snacks:
            if snack_id == snack['id']:
                shopping_cart.append(snack)
                found = True
                print(f'Ok, snack agregado: {snack}')
        if found == False:
            print(f'No se encontró un snack con el id:{snack_id}')
            print(' Snacks Disponibles:')
            for snack in snacks:
                print(f'\tId: {snack['id']} -> {snack['name']} - Precio: S/{snack['cost']}')
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