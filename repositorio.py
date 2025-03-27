import acceso_datos
import pantallas

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    con = acceso_datos.Conexion()
    ventana = pantallas.Pantallas(con)
    ventana.menu_aplicacion()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
