import csv
import pandas as pd


class LibrTrenes:
    cabecera = ["ID", "TITULO", "AUTOR", "EDITORIAL", "AÑO", "LEIDO"]
    cabecera_alta = {"ID": "INT", "TITULO": "STR", "AUTOR": "STR", "EDITORIAL": "STR", "AÑO": "INT", "LEIDO": "STR"}

    _con = None
    _ventana = None

    _titulo = None

    def __init__(self, con, ventana):
        self._con = con
        self._ventana = ventana

    def lista_completa(self):
        result = self._con.consulta_sin_parametros("SELECT * FROM LIBRO_TRENES")
        self._ventana.presenta_datos(self.cabecera, result)

    def alta_libro(self, libro):
        self._con.consulta("INSERT INTO LIBRO_TRENES (TITULO, AUTOR, EDITORIAL, ANYO, LEIDO) VALUES (?,?,?,?,?)", libro)
        self._con.commit()
        self.lista_completa()

    def buscar_libro(self, titulo):
        titulo = "%" + titulo + "%"
        result = self._con.consulta("SELECT * FROM LIBRO_TRENES WHERE TITULO LIKE ?", [titulo.upper(), ])
        if len(result) == 0:
            self._ventana.messagebox("ERROR", "Registro no encontrado")
        else:
            self._ventana.presenta_datos(self.cabecera, result)

    def modificar_libro(self, identificador):
        result = self._con.consulta("SELECT * FROM LIBRO_TRENES WHERE LIBRO_ID = ?", [identificador, ])
        if len(result) != 0:
            self._ventana.modificar_libro_trenes(result[0])
        else:
            self._ventana.messagebox("ERROR", "Registro no encontrado")

    def procesa_modificar_libro(self, result):
        self._con.consulta("UPDATE LIBRO_TRENES SET TITULO = ?, AUTOR = ?, EDITORIAL = ?, ANYO = ?, "
                           "LEIDO = ? WHERE LIBRO_ID = ?", result)
        self._con.commit()
        self._ventana.messagebox("INFO", "Resgistro modificado correctamente")
        self.lista_completa()

    def borrar_libro(self, identificador):
        self._con.consulta("DELETE FROM LIBRO_TRENES WHERE LIBRO_ID = ?", [identificador, ])
        self._con.commit()
        self._ventana.messagebox("INFO", "Resgistro borrado correctamente")
        self.lista_completa()

    def export_csv(self, nombre):
        result = self._con.consulta_sin_parametros("SELECT * FROM LIBRO_TRENES")
        lista = [list(item) for item in result]
        with open(nombre, "w") as fichero:
            wr = csv.writer(fichero, delimiter=";", dialect="excel")
            wr.writerows(lista)

    def export_excel(self, nombre):
        result = self._con.consulta_sin_parametros("SELECT * FROM LIBRO_TRENES")
        df = pd.DataFrame(result, columns=self.cabecera)
        df.to_excel(nombre, sheet_name="Libros Informatica", index=False)

    def import_csv(self, nombre):
        with open(nombre, "r") as fichero:
            reader = csv.reader(fichero, delimiter=";", dialect="excel")
            for libro in reader:
                self.alta_libro(libro)
