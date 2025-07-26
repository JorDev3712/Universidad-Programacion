from catalag import Catalog

def show_menu():
    print(f'''Opciones:
          1. Agregar Película
          2. Listar Películas
          3. Eliminar catálogo películas
          4. Salir''')
    return int(input('Escribe tu opción: '))

def add_movie(catalog: Catalog):
    name_movie = input('Proporciona el nombre de la película: ')
    catalog.add_film(name_movie)

def show_films(catalog: Catalog):
    print('------------------- Catálogo de Películas -----------------')
    movies = catalog.get_films()
    if len(movies) == 0:
        print('No se encontró películas añadidas.')
    else:
        for movie in movies:
            print(movie.strip())

def delete_movies(catalog: Catalog):
    result = catalog.remove_cataloge()
    if result:
        print(f'Archivo eliminado: {catalog.getFileName()}')
    else:
        print('Aún no hay un catálogo creado.')

def execute_option(option, cat):
    exit = False
    if option == 1:
        add_movie(cat)
    elif option == 2:
        show_films(cat)
    elif option == 3:
        delete_movies(cat)
    elif option == 4:
        exit = True
    else:
        print('Opción incorrecta, verifica las opciones disponibles')
    return exit

# Main Code
print('*** App catalogo de películas ***')
catalog = Catalog('peliculas.txt')
exit = False
while not exit:
    option = show_menu()
    exit = execute_option(option, catalog)