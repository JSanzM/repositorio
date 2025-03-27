import sqlite3


class Conexion:

    _con = None
    _cur = None

    def __init__(self):
        self._con = sqlite3.connect("BaseDatos/repositorio.db")
        self._cur = self._con.cursor()

    def consulta(self, sentencia, parameters):
        self._cur.execute(sentencia, parameters)
        return self._cur.fetchall()

    def consulta_sin_parametros(self, sentencia):
        self._cur.execute(sentencia)
        return self._cur.fetchall()

    def commit(self):
        self._con.commit()

    def rollback(self):
        self._con.rollback()
