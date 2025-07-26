import os

class Catalog:
    def __init__(self, fileName):
        self.__fileName = fileName
    
    def add_film(self, name):
        try:
            print('Abriendo el archivo:')
            file = open(self.__fileName, '+a')
        except Exception as e:
            print(f'Error al abrir archivo: {e}')
        else:
            print('Añadiendo pelicula!')
            file.write(name+'\n')
        finally:
            # Closing file
            if file is not None:
                file.close()
                print('Se cerro el archivo correctamente')

    def get_films(self):
        try:
            print('Abriendo el archivo: ')
            # If file not exits return empty list
            if not os.path.exists(self.__fileName):
                return []
            file = open(self.__fileName, 'r')
        except Exception as e:
            print(f'Error al abrir archivo: {e}')
        else:
            return file.readlines()
        finally:
            # Closing file
            if file is not None:
                file.close()
                print('Se cerro el archivo correctamente')

    def remove_cataloge(self):
        # Delete file
        if os.path.exists(self.__fileName):
            os.remove(self.__fileName)
            return True
        return False
    
    def getFileName(self):
        return self.__fileName
    
