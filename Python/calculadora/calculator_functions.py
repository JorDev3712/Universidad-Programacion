# Reto de calculadora con funciones
# 1. Mostrar el menu en una funcion
# 2. Solicitar los valores de los operandos en una funcion
# 3. La operacion a ejecutar va en otra funcion por separado
print('***** Calculadora en Python con Funciones *****')
''' Definimos la función para mostrar menu '''
def showMenu():
    print(f'''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir''')
    # Obtener la opcion desde la consola
    option = int(input('Escoje una opcion: '))
    return option


''' Definimos la función para solicitar los valores '''
def requestValues():
    value_a = float(input('Dame el valor 1: '))
    value_b = float(input('Dame el valor 2: '))
    return (value_a, value_b)


''' Definimos la funcion para ejecutar la operacion solicitada '''
def executeOperation(option, exit):
    value_a = 0.00
    value_b = 0.00
    if 1 <= option <= 4:
        value_a, value_b = requestValues()
    # Verificar las opciones que se ingresó
    if option == 1:
        resultant = value_a + value_b
        print(f'El resultado de la suma es: {resultant:.2f}')
    elif option == 2:
        resultant = value_a - value_b
        print(f'El resultado de la resta es: {resultant:.2f}')
    elif option == 3:
        resultant = value_a * value_b
        print(f'El resultado de la multiplicacion es: {resultant:.2f}')
    elif option == 4:
        if value_a <= 0:
            print('El número ingresado debe ser mayor o igual a 1.')
        resultant = value_a / value_b
        print(f'El resultado de la division es: {resultant:.2f}')
    elif option == 5:
        exit = True
        print('Saliendo del programa Calculadora. Hasta pronto!')
    else:
        print('La opcion ingresada no exite, por favor selecciona una opcion correcta.')
    return exit

# Codigo principal
exit = False
while not exit: 
    option = showMenu()
    exit = executeOperation(option, exit)