import csv
import pandas as pd


class Aplicaciones:
    cabecera = ["ID", "APLICACION", "ORIGEN", "INSTALAR", "FAVORITOS", "NOTAS"]
    cabecera_alta = {"ID": "INT", "APLICACION": "STR", "ORIGEN": "STR", "INSTALAR": "STR", "FAVORITOS": "STR",
                     "NOTAS": "STR"}

    _con = None
    _ventana = None

    _titulo = None

    def __init__(self, con, ventana):
        self._con = con
        self._ventana = ventana

    def lista_completa(self):
        result = self._con.consulta_sin_parametros("SELECT * FROM APLICACIONES")
        self._ventana.presenta_datos(self.cabecera, result)

    def alta_aplicacion(self, aplicacion):
        self._con.consulta("INSERT INTO APLICACIONES (APLICACION, ORIGEN, INSTALAR, FAVORITOS, NOTAS) "
                           "VALUES (?,?,?,?,?)", aplicacion)
        self._con.commit()
        self.lista_completa()

    def buscar_aplicacion(self, aplicacion):
        aplicacion = "%" + aplicacion + "%"
        result = self._con.consulta("SELECT * FROM APLICACIONES WHERE APLICACION LIKE ?", [aplicacion.upper(), ])
        if len(result) == 0:
            self._ventana.messagebox("ERROR", "Registro no encontrado")
        else:
            self._ventana.presenta_datos(self.cabecera, result)

    def modificar_aplicacion(self, identificador):
        result = self._con.consulta("SELECT * FROM APLICACIONES WHERE APLICACION_ID = ?", [identificador, ])
        if len(result) != 0:
            self._ventana.modificar_aplicacion(result[0])
        else:
            self._ventana.messagebox("ERROR", "Registro no encontrado")

    def procesa_modificar_aplicacion(self, result):
        self._con.consulta("UPDATE APLICACIONES SET APLICACION = ?, ORIGEN = ?, INSTALAR = ?, FAVORITOS = ?, "
                           "NOTAS = ? WHERE APLICACION_ID = ?", result)
        self._con.commit()
        self._ventana.messagebox("INFO", "Resgistro modificado correctamente")
        self.lista_completa()

    def borrar_aplicacion(self, identificador):
        self._con.consulta("DELETE FROM APLICACIONES WHERE APLICACION_ID = ?", [identificador, ])
        self._con.commit()
        self._ventana.messagebox("INFO", "Resgistro borrado correctamente")
        self.lista_completa()

    def export_csv(self, nombre):
        result = self._con.consulta_sin_parametros("SELECT * FROM APLICACIONES")
        lista = [list(item) for item in result]
        with open(nombre, "w") as fichero:
            wr = csv.writer(fichero, delimiter=";", dialect="excel")
            wr.writerows(lista)

    def export_excel(self, nombre):
        result = self._con.consulta_sin_parametros("SELECT * FROM APLICACIONES")
        df = pd.DataFrame(result, columns=self.cabecera)
        df.to_excel(nombre, sheet_name="Aplicaciones", index=False)

    def import_csv(self, nombre):
        with open(nombre, "r") as fichero:
            reader = csv.reader(fichero, delimiter=";", dialect="excel")
            for aplicacion in reader:
                self.alta_aplicacion(aplicacion)
