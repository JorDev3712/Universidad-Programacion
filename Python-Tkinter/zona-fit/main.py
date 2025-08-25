from db.conexion import ConnectionMysql
from services.clienteService import ClienteService
from zona_fit_gui import ZonaFitWindow

conn = ConnectionMysql('reto_mysql_db1', 'root', '')
service = ClienteService(conn)
app = ZonaFitWindow(service)

if __name__ == '__main__':
    app.mainloop()