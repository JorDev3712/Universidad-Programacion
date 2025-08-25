from mysql.connector import pooling
from mysql.connector import Error

class ConnectionMysql:

    # Define constructor
    def __init__(self, db_name, user, password, db_port = '3306', host_name = 'localhost'):
        self.__database = db_name
        self.__username = user
        self.__password = password
        self.__host_port = db_port
        self.__host = host_name
        self.__poolName = 'zona_fit_pool'
        self.__pool = None

    def obtenerPool(self):
        if self.__pool is None: # It need create the object pool
            try:
                self.__pool = pooling.MySQLConnectionPool(
                    pool_size=5, 
                    pool_name=self.__poolName,
                    host=self.__host,
                    port=self.__host_port,
                    database=self.__database,
                    user=self.__username,
                    password=self.__password
                )
                return self.__pool
            except Error as e:
                print(f'Ocurrió un error al obtener pool: {e}')
        else:
            return self.__pool
            
    def open(self): # Creates a connection mysql
        return self.obtenerPool().get_connection()