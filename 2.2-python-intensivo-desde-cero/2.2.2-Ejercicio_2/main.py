agenda = []


def agregarContacto():
    nombre = input("Ingrese su nombre: ")
    telefono = int(input("Ingrese su teléfono: "))
    contacto = (nombre, telefono)
    agenda.append(contacto)
    print(agenda)


def buscarContacto():
    nombre = input("Ingrese el nombre de la persona que desea buscar: ")
    resultados = [contacto for contacto in agenda if contacto[0].startswith(nombre)]
    if resultados:
        print("Resultados:")
        for contacto in resultados:
            print(f"{contacto[0]}: {contacto[1]}")
    else:
        print("No se encontraron resultados.")


while True:
    print("----- AGENDA DE TELÉFONOS -----")
    print("1. Añadir persona")
    print("2. Buscar teléfono")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregarContacto()
    elif opcion == "2":
        buscarContacto()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Intente nuevamente.")