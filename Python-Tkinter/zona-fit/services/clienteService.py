from db.conexion import ConnectionMysql
from models.cliente import Cliente

class ClienteService:
    def __init__(self, connection: ConnectionMysql):
        self._connection = connection

    def get_auto_increment_of_client_table(self)->int:
        last_id = 0
        with self._connection.open() as db:
            with db.cursor() as cursor:
                cursor.execute("SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME ='clientes'")
                result = cursor.fetchone()
                if result:
                    last_id = result[0]
        return last_id

    def getClients(self):
        clientes = []
        # with allows management of resources
        # try:
        #     db = self._connection.open()
        #     cursor = db.cursor()
        #     cursor.execute('SELECT * FROM `clientes`')
        #     result = cursor.fetchall()
        #     for client in result:
        #         id, name, lastname, membership = client
        #         clientes.append(Cliente(id, name, lastname, membership))
        #     return clientes
        # except Exception as e:
        #     print(f'Ocurrio un error al seleccionar clientes: {e}')
        # finally:
        #     if db is not None:
        #         cursor.close()
        #         db.close()
        with self._connection.open() as db:
            with db.cursor() as cursor:
                cursor.execute('SELECT * FROM `clientes`')
                result = cursor.fetchall()
                for client in result:
                    id, name, lastname, membership = client
                    clientes.append(Cliente(id, name, lastname, membership))
        return clientes
    
    def getCliente(self, id: int)->Cliente:
        client = None
        with self._connection.open() as db:
            with db.cursor() as cursor:
                sql = 'SELECT * FROM `clientes` WHERE (`id`=%s)'
                cursor.execute(sql, (id,))
                id, name, lastname, membership = cursor.fetchone()
                client = Cliente(id, name, lastname, membership)
        return client

    def addClient(self, name: str, lastname: str, membership: int)->bool:
        result = False
        # with allows management of resources
        with self._connection.open() as db:
            with db.cursor() as cursor:
                # Creates sql sentence
                sql = ('INSERT INTO `clientes`(`name`, `lastname`, `membership`)'
                    'VALUES(%s, %s, %s)')
                values = (name, lastname, membership)
                cursor.execute(sql, values)

                # Saves the changes into db
                db.commit()
                result = True
        return result

    def updateClient(self, cliente: Cliente)->bool:
        result = False
        # with allows management of resources
        with self._connection.open() as db:
            with db.cursor() as cursor:
                # Creates sql sentence
                sql = ('UPDATE `clientes` SET `name`=%s, `lastname`=%s, `membership`=%s WHERE (`id`=%s)')
                values = (cliente.name, cliente.last_name, cliente.membership, cliente.id)
                cursor.execute(sql, values)

                # Saves the changes into db
                db.commit()
                result = True
        return result

    def deleteClient(self, cliente: Cliente)->bool:
        result = False
        # with allows management of resources
        with self._connection.open() as db:
            with db.cursor() as cursor:
                # Creates sql sentence
                sql = 'DELETE FROM `clientes` WHERE (`id`=%s)'
                cursor.execute(sql, (cliente.id,))

                # Saves the changes into db
                db.commit()
                result = True
        return result

