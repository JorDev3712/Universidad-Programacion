#Mostramos el titulo
print('***** Calculadora en Python *****')
#Variable para terminar while
exit = False
while not exit:
    print(f'''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir''')
    # Obtener la opcion desde la consola
    option = int(input('Escoje una opcion: '))
    value_a = 0.00
    value_b = 0.00
    # Este if y las variables fueron tomadas de la solucion del curso
    # Si en caso se quiere agregar otra opcion, se tiene que modificar el if
    if 1 <= option <= 4:
        value_a = float(input('Dame el valor 1: '))
        value_b = float(input('Dame el valor 2: '))
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