from services.clienteService import ClienteService

class AppController:
    exit = False

    def __init__(self, service: ClienteService):
        self._service = service

    def show_menu(self):
        print(f'''Menu:
        1. Listar clientes.
        2. Agregar cliente.
        3. Modificar cliente.
        4. Eliminar cliente.
        5. Salir''')
        return int(input('Escribe tu opción (1-5): '))
    
    def menu_show_clients(self):
        print('*** Listado de Clientes ***')
        clients = self._service.getClients()
        if len(clients) == 0:
            print('No se encontraron clientes registrados.')
        else:
            for cl in clients:
                print(cl)

    def menu_add_new_client(self):
        name = input('Escribe el nombre: ')
        last_name = input('Escribe el apellido: ')
        membership = int(input('Escribe la membresia: '))
        result = self._service.addClient(name, last_name, membership)
        if result:
            print('Nuevo cliente(a) agregado(a).')
        else:
            print('No se pudo agregar, intente más tarde.')

    def menu_edit_client(self):
        id = int(input('Escribe el id del cliente a modificar: '))
        # Get client to edit
        cliente = self._service.getCliente(id)
        # Check client
        if cliente is not None:
            res = input(f'El cliente a modificar es {cliente.name} con membresia: {cliente.membership} (y-n): ')
            if res.lower() == 'y':
                name = input('Escribe el nuevo nombre: ')
                last_name = input('Escribe el nuevo apellido: ')
                membership = int(input('Escribe la nueva membresia: '))
                cliente.name = name
                cliente.last_name = last_name
                cliente.membership = membership
                result = self._service.updateClient(cliente)
                if result:
                    print('Cliente(a) actualizado(a).')
                else:
                    print('No se pudo actualizar, intente más tarde.')
            else:
                print('No se ha realizado ningún cambio.')
        else:
            self.menu_show_clients()
            print('Por favor, ingresa el/la cliente correcto(a) a modificar.')

    def menu_delete_client(self):
        id = int(input('Escribe el id del cliente a eliminar: '))
        # Get client to delete
        cliente = self._service.getCliente(id)
        if cliente is not None:
            res = input(f'El cliente a eliminar es {cliente.name} con membresia: {cliente.membership} (y-n): ')
            if res.lower() == 'y':
                result = self._service.deleteClient(cliente)
                if result:
                    print('Cliente(a) eliminado(a).')
                else:
                    print('No se pudo eliminar, intente más tarde.')
            else:
                print('No se ha realizado ningún cambio.')
        else:
            self.menu_show_clients()
            print('Por favor, ingresa el/la cliente correcto(a) a eliminar.')

    def executeOption(self, option)->bool:
        if option == 1:
            self.menu_show_clients()
        elif option == 2:
            self.menu_add_new_client()
        elif option == 3:
            self.menu_edit_client()
        elif option == 4:
            self.menu_delete_client()
        elif option == 5:
            self.exit = True
        else:
            print('Por favor selecciona la opción correcta.')
        return self.exit

