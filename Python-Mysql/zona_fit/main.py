from db.conexion import ConnectionMysql
from services.clienteService import ClienteService
from controllers.appController import AppController

conn = ConnectionMysql('reto_mysql_db1', 'root', '')
clienteService = ClienteService(conn)
appController = AppController(clienteService)

print('*** Clientes de Zona Fit (GYM) ***')
while appController.exit is False:
    opt = appController.show_menu()
    appController.executeOption(opt)
