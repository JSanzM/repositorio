import csv
import pandas as pd


class Cds:
    cabecera = ["ID", "TITULO", "GRUPO", "AÑO", "NOTAS", "FALTA", "TIPO"]
    cabecera_alta = {"ID": "INT", "TITULO": "STR", "GRUPO": "STR", "AÑO": "INT", "NOTAS": "STR",
                     "FALTA": "STR", "TIPO": "STR"}

    _con = None
    _ventana = None

    _titulo = None

    def __init__(self, con, ventana):
        self._con = con
        self._ventana = ventana

    def lista_completa(self):
        result = self._con.consulta_sin_parametros("SELECT * FROM CDS")
        self._ventana.presenta_datos(self.cabecera, result)

    def alta_cd(self, cd):
        self._con.consulta("INSERT INTO CDS (TITULO, GRUPO, ANYO,  NOTAS, "
                           "FALTA, TIPO) VALUES (?,?,?,?,?,?)", cd)
        self._con.commit()
        self.lista_completa()

    def buscar_cd(self, titulo):
        titulo = "%" + titulo + "%"
        result = self._con.consulta("SELECT * FROM CDS WHERE TITULO LIKE ?", [titulo.upper(), ])
        if len(result) == 0:
            self._ventana.messagebox("ERROR", "Registro no encontrado")
        else:
            self._ventana.presenta_datos(self.cabecera, result)

    def modificar_cd(self, identificador):
        result = self._con.consulta("SELECT * FROM CDS WHERE CD_ID = ?", [identificador, ])
        if len(result) != 0:
            self._ventana.modificar_cds(result[0])
        else:
            self._ventana.messagebox("ERROR", "Registro no encontrado")

    def procesa_modificar_cd(self, result):
        self._con.consulta("UPDATE CDS SET TITULO = ?, GRUPO = ?, ANYO = ?, NOTAS = ?,"
                           " FALTA = ?, TIPO = ? WHERE CD_ID = ?", result)
        self._con.commit()
        self._ventana.messagebox("INFO", "Resgistro modificado correctamente")
        self.lista_completa()

    def borrar_cd(self, identificador):
        self._con.consulta("DELETE FROM CDS WHERE CD_ID = ?", [identificador, ])
        self._con.commit()
        self._ventana.messagebox("INFO", "Resgistro borrado correctamente")
        self.lista_completa()

    def export_csv(self, nombre):
        result = self._con.consulta_sin_parametros("SELECT * FROM CDS")
        lista = [list(item) for item in result]
        with open(nombre, "w") as fichero:
            wr = csv.writer(fichero, delimiter=";", dialect="excel")
            wr.writerows(lista)

    def export_excel(self, nombre):
        result = self._con.consulta_sin_parametros("SELECT * FROM CDS")
        df = pd.DataFrame(result, columns=self.cabecera)
        df.to_excel(nombre, sheet_name="Libros Informatica", index=False)

    def import_csv(self, nombre):
        with open(nombre, "r") as fichero:
            reader = csv.reader(fichero, delimiter=";", dialect="excel")
            for cd in reader:
                self.alta_cd(cd)
