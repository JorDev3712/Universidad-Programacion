# Crear variable de snacks
from snacks import Snacks

# Codigo principal

# Variable para guardar las compras
snacks = Snacks()
shopping_cart = []

def buy_snack():
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


def show_ticket():
    # Mostrar titulo de ticket
    print('*** Ticker de Venta ***')
    cost_total = 0
    for shop in shopping_cart:
        print(f'- {shop.name} - S/{shop.cost}')
        cost_total += shop.cost
    print(f'TOTAL -> {cost_total}')


def add_snack():
    print('Por favor completa los datos para añadir un nuevo snack:')
    snack_name = input('Ingresa el nombre: ')
    if snack_name == '' or snack_name == ' ':
        print('Debe ingresar un nombre válido.')
        pass

    snack_cost = float(input('Ingresa el precio: '))
    if snack_cost <= 0:
        print('Debe ingresar un precio mayor que 0.')
        pass
    snacks.add_snack_values(snack_name, snack_cost)
    print(f'Nuevo snack agregado: {snack_name}:{snack_cost}')
    print(' Snacks Disponibles:')
    print(snacks.__str__())


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
    3. Añadir Snack.
    4. Salir''')
    # Obtener la opción desde la consola
    option = int(input(' Escoge una opcion: '))
    if option == 1: # Comprar snack
        buy_snack()
    elif option == 2: # Mostrar ticket
       show_ticket()
    elif option == 3: # Añadir nuevo snack
        add_snack()
    elif option == 4: # Exit
        exit = True
        print('Saliendo del Maquina de Snacks. Hasta pronto...')
    else:
        print('La opcion ingresada no exite, por favor selecciona una opcion correcta.')