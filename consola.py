def menu():
    print("Repositorio v1")
    print("==============")
    print("")
    print("1.- Libros Informática")
    print("2.- Libros de Trenes")
    print("3.- Libros Electrónicos")
    print("4.- CD's")
    print("5.- Aplicaciones Instaladas")
    print("6.- Juegos Instalados")
    print("")
    print("0.- Salir")
    print("")
    print("Introduce Opción: ")

    opcion = -1

    while opcion > 6 or opcion < 0:
        try:
            opcion = int(input())
        except ValueError:
            opcion = -1

        if opcion < 0 or opcion > 6:
            print("Opción no válida")

    return opcion


def menu_libro_informatica():
    print("Menú Libro Informática")
    print("======================")
    print()
    print("1.- Lista Libros")
    print("2.- Añadir Libro")
    print("3.- Buscar Libro")
    print("4.- Modificar Libro")
    print("5.- Baja Libro")
    print("6.- Exportar Libros a CSV")
    print("7.- Exportar Libros a Excel")
    print()
    print("0.- Salir")
    print()
    print("Introduce Opción")

    opcion = -1

    while opcion > 7 or opcion < 0:
        try:
            opcion = int(input())
        except ValueError:
            opcion = -1

        if opcion < 0 or opcion > 6:
            print("Opción no válida")

    return opcion


def presenta_datos(cabecera, result):
    texto = ''
    for dato in cabecera:
        texto = texto + dato.ljust(30, ' ')
    print(texto)
    for datos in result:
        linea = ""
        for r2 in datos:
            linea = linea + f"{r2}".ljust(30, ' ').replace('\n', '')[0:30]
        print(linea)


def menu_alta(cabecera):
    retorno = []
    valor = ""

    for titulo, tipo in cabecera.items():
        if titulo != "ID":
            correcto = False
            while not correcto:
                entrada = input(titulo + ": ")
                if tipo == "INT":
                    try:
                        valor = int(entrada)
                    except ValueError:
                        print("Valor Incorrecto.")
                        continue
                elif tipo == "STR":
                    valor = entrada.upper()
                correcto = True
                retorno.append(valor)
    return retorno


def obtener_info(mensaje):
    dato = input('Introduce '+mensaje+': ')
    return dato


def obtener_id(mensaje):
    identificador = -1
    while identificador == -1:
        dato = obtener_info(mensaje)
        try:
            identificador = int(dato)
        except ValueError:
            print("Valor incorrecto, vuelva a intentarlo")
    return identificador


def menu_modificacion(cabecera, valores):
    retorno = []
    valor = ""

    for titulo, tipo in cabecera.items():
        if titulo != "ID":
            correcto = False
            while not correcto:
                entrada = input(f"{titulo} ({valores[titulo]}): ")
                if entrada == "":
                    valor = valores[titulo]
                else:
                    if tipo == "INT":
                        try:
                            valor = int(entrada)
                        except ValueError:
                            print("Valor Incorrecto.")
                            continue
                    elif tipo == "STR":
                        valor = entrada.upper()
                correcto = True
                retorno.append(valor)

    retorno.append(valores["ID"])
    return retorno


def pedir_nombre_fichero():
    nombre = input("Introduce el nombre del fichero a exportar: ")
    return nombre
