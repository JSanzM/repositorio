import csv
import pandas as pd


class Juegos:
    cabecera = ["ID", "NOMBRE", "TIPO", "INSTALAR", "ORIGEN", "NOTAS"]
    cabecera_alta = {"ID": "INT", "NOMBRE": "STR", "TIPO": "STR", "INSTALAR": "STR", "ORIGEN": "STR",
                     "NOTAS": "STR"}

    _con = None
    _ventana = None

    _titulo = None

    def __init__(self, con, ventana):
        self._con = con
        self._ventana = ventana

    def lista_completa(self):
        result = self._con.consulta_sin_parametros("SELECT * FROM JUEGOS")
        self._ventana.presenta_datos(self.cabecera, result)

    def alta_juego(self, juego):
        self._con.consulta("INSERT INTO JUEGOS (NOMBRE, TIPO, INSTALAR, ORIGEN, NOTAS) "
                           "VALUES (?,?,?,?,?)", juego)
        self._con.commit()
        self.lista_completa()

    def buscar_juego(self, juego):
        juego = "%" + juego + "%"
        result = self._con.consulta("SELECT * FROM JUEGOS WHERE NOMBRE LIKE ?", [juego.upper(), ])
        if len(result) == 0:
            self._ventana.messagebox("ERROR", "Registro no encontrado")
        else:
            self._ventana.presenta_datos(self.cabecera, result)

    def modificar_juego(self, identificador):
        result = self._con.consulta("SELECT * FROM JUEGOS WHERE JUEGO_ID = ?", [identificador, ])
        if len(result) != 0:
            self._ventana.modificar_juego(result[0])
        else:
            self._ventana.messagebox("ERROR", "Registro no encontrado")

    def procesa_modificar_juego(self, result):
        self._con.consulta("UPDATE JUEGOS SET NOMBRE = ?, TIPO = ?, INSTALAR = ?, ORIGEN = ?, "
                           "NOTAS = ? WHERE JUEGO_ID = ?", result)
        self._con.commit()
        self._ventana.messagebox("INFO", "Resgistro modificado correctamente")
        self.lista_completa()

    def borrar_juego(self, identificador):
        self._con.consulta("DELETE FROM JUEGOS WHERE JUEGO_ID = ?", [identificador, ])
        self._con.commit()
        self._ventana.messagebox("INFO", "Resgistro borrado correctamente")
        self.lista_completa()

    def export_csv(self, nombre):
        result = self._con.consulta_sin_parametros("SELECT * FROM JUEGOS")
        lista = [list(item) for item in result]
        with open(nombre, "w") as fichero:
            wr = csv.writer(fichero, delimiter=";", dialect="excel")
            wr.writerows(lista)

    def export_excel(self, nombre):
        result = self._con.consulta_sin_parametros("SELECT * FROM JUEGOS")
        df = pd.DataFrame(result, columns=self.cabecera)
        df.to_excel(nombre, sheet_name="Juegos", index=False)

    def import_csv(self, nombre):
        with open(nombre, "r") as fichero:
            reader = csv.reader(fichero, delimiter=";", dialect="excel")
            for juego in reader:
                self.alta_juego(juego)
