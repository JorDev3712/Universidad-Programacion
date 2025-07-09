# Mensaje de bienvenida 1.
print("*** Bienvenido al sistema de generación email de cuidad gotica ***")

# Solicitar nombre y obtener el nombre de la consola
name = input("Cual es tu nombre: ")
name = name.lower()
# Solicitar apellido y obtener el apellido de la consola
lastname = input("Cual es tu apellido: ")
lastname = lastname.lower()

# Mensaje final
print(" Tu nuevo email generador por el sistema es: ")
print(f"\t{name}.{lastname}@ciudadgotica.com")
print("\t *** Felicidades ***")