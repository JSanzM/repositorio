import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import libro_informatica as libinf
import libro_trenes as ltren
import libro_electronico as lelec
import cds as cds
import aplicaciones as app
import juegos as j


class Pantallas:

    _frm = None
    _con = None
    _ventana = None
    _linf = None
    _ltren = None
    _lelec = None
    _cds = None
    _app = None
    _juego = None

    def __init__(self, con):
        self._con = con
        self._linf = libinf.LibroInformatica(self._con, self)
        self._ltren = ltren.LibrTrenes(self._con, self)
        self._lelec = lelec.LibroElectronico(self._con, self)
        self._cds = cds.Cds(self._con, self)
        self._app = app.Aplicaciones(self._con, self)
        self._juego = j.Juegos(self._con, self)

    def menu_lib_inf(self, barra_menus):
        menu_libro_informatica = tk.Menu(barra_menus, tearoff=False)
        menu_libro_informatica.add_command(label="Lista Libros", command=self._linf.lista_completa)
        menu_libro_informatica.add_command(label="Añadir Libro", command=self.alta_libro_informatica)
        menu_libro_informatica.add_command(label="Buscar Libro",
                                           command=lambda: self.pedir_dato("TITULO", "INFORMATICA_TITULO"))
        menu_libro_informatica.add_command(label="Modificar Libro",
                                           command=lambda: self.pedir_dato("IDENTIFICADOR", "INFORMATICA_MODIFICAR"))
        menu_libro_informatica.add_command(label="Baja Libro",
                                           command=lambda: self.pedir_dato("IDENTIFICADOR", "INFORMATICA_BORRAR"))
        menu_libro_informatica.add_command(label="Exportar Libros a CSV",
                                           command=lambda: self.pedir_fichero("csv", "INFORMATICA"))
        menu_libro_informatica.add_command(label="Exportar Libros a Excel",
                                           command=lambda: self.pedir_fichero("xlsx", "INFORMATICA"))
        menu_libro_informatica.add_command(label="Importar Libros (CSV)",
                                           command=lambda: self.importar_fichero("csv", "INFORMATICA"))
        return menu_libro_informatica

    def menu_lib_trenes(self, barra_menus):
        menu_libro_trenes = tk.Menu(barra_menus, tearoff=False)
        menu_libro_trenes.add_command(label="Lista Libros", command=self._ltren.lista_completa)
        menu_libro_trenes.add_command(label="Añadir Libro", command=self.alta_libro_trenes)
        menu_libro_trenes.add_command(label="Buscar Libro",
                                      command=lambda: self.pedir_dato("TITULO", "TREN_TITULO"))
        menu_libro_trenes.add_command(label="Modificar Libro",
                                      command=lambda: self.pedir_dato("IDENTIFICADOR", "TREN_MODIFICAR"))
        menu_libro_trenes.add_command(label="Baja Libro",
                                      command=lambda: self.pedir_dato("IDENTIFICADOR", "TREN_BORRAR"))
        menu_libro_trenes.add_command(label="Exportar Libros a CSV",
                                      command=lambda: self.pedir_fichero("csv", "TREN"))
        menu_libro_trenes.add_command(label="Exportar Libros a Excel",
                                      command=lambda: self.pedir_fichero("xlsx", "TREN"))
        menu_libro_trenes.add_command(label="Importar Libros (CSV)",
                                      command=lambda: self.importar_fichero("csv", "TREN"))
        return menu_libro_trenes

    def menu_lib_electronico(self, barra_menus):
        menu_libro_electronico = tk.Menu(barra_menus, tearoff=False)
        menu_libro_electronico.add_command(label="Lista Libros", command=self._lelec.lista_completa)
        menu_libro_electronico.add_command(label="Añadir Libro", command=self.alta_libro_electronico)
        menu_libro_electronico.add_command(label="Buscar Libro",
                                           command=lambda: self.pedir_dato("TITULO", "ELECTRONICO_TITULO"))
        menu_libro_electronico.add_command(label="Modificar Libro",
                                           command=lambda: self.pedir_dato("IDENTIFICADOR", "ELECTRONICO_MODIFICAR"))
        menu_libro_electronico.add_command(label="Baja Libro",
                                           command=lambda: self.pedir_dato("IDENTIFICADOR", "ELECTRONICO_BORRAR"))
        menu_libro_electronico.add_command(label="Exportar Libros a CSV",
                                           command=lambda: self.pedir_fichero("csv", "ELECTRONICO"))
        menu_libro_electronico.add_command(label="Exportar Libros a Excel",
                                           command=lambda: self.pedir_fichero("xlsx", "ELECTRONICO"))
        menu_libro_electronico.add_command(label="Importar Libros (CSV)",
                                           command=lambda: self.importar_fichero("csv", "ELECTRONICO"))
        return menu_libro_electronico

    def menu_cds(self, barra_menus):
        menu_cd = tk.Menu(barra_menus, tearoff=False)
        menu_cd.add_command(label="Lista CDs/DVDs", command=self._cds.lista_completa)
        menu_cd.add_command(label="Añadir CDs/DVDs", command=self.alta_cds)
        menu_cd.add_command(label="Buscar CDs/DVDs",
                            command=lambda: self.pedir_dato("TITULO", "CD_TITULO"))
        menu_cd.add_command(label="Modificar CDs/DVDs",
                            command=lambda: self.pedir_dato("IDENTIFICADOR", "CD_MODIFICAR"))
        menu_cd.add_command(label="Baja CDs/DVDs",
                            command=lambda: self.pedir_dato("IDENTIFICADOR", "CD_BORRAR"))
        menu_cd.add_command(label="Exportar CDs/DVDs a CSV",
                            command=lambda: self.pedir_fichero("csv", "CD"))
        menu_cd.add_command(label="Exportar CDs/DVDs a Excel",
                            command=lambda: self.pedir_fichero("xlsx", "CD"))
        menu_cd.add_command(label="Importar CDs/DVDs (CSV)",
                            command=lambda: self.importar_fichero("csv", "CD"))
        return menu_cd

    def menu_aplicaciones(self, barra_menus):
        menu_aplicaciones = tk.Menu(barra_menus, tearoff=False)
        menu_aplicaciones.add_command(label="Lista Aplicaciones", command=self._app.lista_completa)
        menu_aplicaciones.add_command(label="Añadir Aplicación", command=self.alta_aplicacion)
        menu_aplicaciones.add_command(label="Buscar Aplicación",
                                      command=lambda: self.pedir_dato("APLICACION", "APLICACION_APLICACION"))
        menu_aplicaciones.add_command(label="Modificar Aplicación",
                                      command=lambda: self.pedir_dato("IDENTIFICADOR", "APLICACION_MODIFICAR"))
        menu_aplicaciones.add_command(label="Baja Aplicación",
                                      command=lambda: self.pedir_dato("IDENTIFICADOR", "APLICACION_BORRAR"))
        menu_aplicaciones.add_command(label="Exportar Aplicaciones a CSV",
                                      command=lambda: self.pedir_fichero("csv", "APLICACION"))
        menu_aplicaciones.add_command(label="Exportar Aplicaciones a Excel",
                                      command=lambda: self.pedir_fichero("xlsx", "APLICACION"))
        menu_aplicaciones.add_command(label="Importar Aplicaciones (CSV)",
                                      command=lambda: self.importar_fichero("csv", "APLICACION"))
        return menu_aplicaciones

    def menu_juegos(self, barra_menus):
        menu_juegos = tk.Menu(barra_menus, tearoff=False)
        menu_juegos.add_command(label="Lista Juegos", command=self._juego.lista_completa)
        menu_juegos.add_command(label="Añadir Juego", command=self.alta_juego)
        menu_juegos.add_command(label="Buscar Juego",
                                      command=lambda: self.pedir_dato("JUEGO", "JUEGO_JUEGO"))
        menu_juegos.add_command(label="Modificar Juego",
                                      command=lambda: self.pedir_dato("IDENTIFICADOR", "JUEGO_MODIFICAR"))
        menu_juegos.add_command(label="Baja Juego",
                                      command=lambda: self.pedir_dato("IDENTIFICADOR", "JUEGO_BORRAR"))
        menu_juegos.add_command(label="Exportar Juegos a CSV",
                                      command=lambda: self.pedir_fichero("csv", "JUEGO"))
        menu_juegos.add_command(label="Exportar Juegos a Excel",
                                      command=lambda: self.pedir_fichero("xlsx", "JUEGO"))
        menu_juegos.add_command(label="Importar Juegos (CSV)",
                                      command=lambda: self.importar_fichero("csv", "JUEGO"))
        return menu_juegos

    def menu_aplicacion(self):
        self._ventana = tk.Tk()
        self._ventana.title("Barra de menus en Tk")
        # self._ventana.config(width=2280, height=600)
        self._ventana.geometry("1920x1080")
        barra_menus = tk.Menu()

        # Creando menú Informática
        menu_libro_informatica = self.menu_lib_inf(barra_menus)
        barra_menus.add_cascade(menu=menu_libro_informatica, label="Libro Informática")

        # Creando menú Trenes
        menu_libro_trenes = self.menu_lib_trenes(barra_menus)
        barra_menus.add_cascade(menu=menu_libro_trenes, label="Libro Trenes")

        # Creando menú Electrónico
        menu_libro_electronico = self.menu_lib_electronico(barra_menus)
        barra_menus.add_cascade(menu=menu_libro_electronico, label="Libro Electrónico")

        # Creando menú CD's
        menu_cd = self.menu_cds(barra_menus)
        barra_menus.add_cascade(menu=menu_cd, label="CDs/DVDs")

        # Creando menú Aplicaciones
        menu_aplicaciones = self.menu_aplicaciones(barra_menus)
        barra_menus.add_cascade(menu=menu_aplicaciones, label="Aplicaciones")

        # Creando menú Juegos
        menu_juegos = self.menu_juegos(barra_menus)
        barra_menus.add_cascade(menu=menu_juegos, label="Juegos")

        # Creando menú Salir
        menu_salir = tk.Menu(barra_menus, tearoff=False)
        menu_salir.add_command(label="Salir", accelerator='Ctrl+X', command=exit)
        barra_menus.add_cascade(menu=menu_salir, label="Salir")

        self._frm = ttk.Frame(self._ventana)

        self._ventana.config(menu=barra_menus)
        self._ventana.mainloop()

    @staticmethod
    def messagebox(tipo, texto):
        if tipo == "ERROR":
            messagebox.showerror("ERROR", texto)
        elif tipo == "INFO":
            messagebox.showinfo("INFO", texto)

    def presenta_datos2(self, cabecera, result):
        self._frm.destroy()
        self._frm = ttk.Frame(self._ventana)
        self._frm.pack(side="left", fill="both", expand=True)

        # Canvas para hacer scroll
        canvas = tk.Canvas(self._frm)

        # Scroll
        scrollbar = tk.Scrollbar(self._frm, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        scrollbarh = tk.Scrollbar(self._frm, orient="horizontal", command=canvas.xview)
        scrollbarh.pack(side="bottom", fill="x")
        canvas.configure(yscrollcommand=scrollbar.set, xscrollcommand=scrollbarh.set)
        canvas.pack(side="left", fill="both", expand=True)

        # Frame dentro del canvas para hacer scroll
        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame)

        # contenido del canvas
        texto = ''
        for dato in cabecera:
            texto = texto + dato.ljust(30, ' ')
        ttk.Label(inner_frame, text=texto, justify="left").pack()

        for datos in result:
            linea = ""
            for r2 in datos:
                linea = linea + f"{r2}".ljust(30, ' ').replace('\n', '')[0:30]
            ttk.Label(inner_frame, text=linea, justify="left").pack()

        # para ajustar el scroll.
        inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    def presenta_datos(self, cabecera, result):
        self._frm.destroy()
        self._frm = ttk.Frame(self._ventana)
        self._frm.pack(side="left", fill="both", expand=True)

        # Canvas para hacer scroll
        canvas = tk.Canvas(self._frm)

        # Scroll
        scrollbar = tk.Scrollbar(self._frm, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        scrollbarh = tk.Scrollbar(self._frm, orient="horizontal", command=canvas.xview)
        scrollbarh.pack(side="bottom", fill="x")
        canvas.configure(yscrollcommand=scrollbar.set, xscrollcommand=scrollbarh.set)
        canvas.pack(side="left", fill="both", expand=True)

        # Frame dentro del canvas para hacer scroll
        inner_frame = tk.Frame(master=canvas, relief=tk.RAISED, borderwidth=2)
        canvas.create_window((0, 0), window=inner_frame)

        # contenido del canvas
        col = 0
        for dato in cabecera:
            texto = dato.ljust(40, ' ')
            ttk.Label(inner_frame, text=texto, justify="left", font=('Arial', 12, 'bold'), relief=tk.RAISED,
                      borderwidth=2).grid(row=0, column=col)
            col = col + 1

        fila = 1
        for datos in result:
            col = 0
            for r2 in datos:
                linea = f"{r2}".ljust(40, ' ').replace('\n', '')[0:40]
                ttk.Label(inner_frame, text=linea, justify="left").grid(row=fila, column=col)
                col = col + 1
            fila = fila + 1

        # para ajustar el scroll.
        inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    def pedir_dato(self, texto, tipo):
        ltexto = None
        opcion = None

        self._frm.destroy()
        self._frm = ttk.Frame(self._ventana)
        self._frm.grid()
        self._frm.pack(side="left", fill="both", expand=True)
        if texto == "TITULO":
            ltexto = "Introduce Título (o parte de el): "
            opcion = tk.StringVar()
        elif texto == "IDENTIFICADOR":
            ltexto = "Introduce Identificador: "
            opcion = tk.IntVar()
        elif texto == "APLICACION":
            ltexto = "Introduce Nombre de Aplicación (o parte de ella): "
            opcion = tk.StringVar()
        elif texto == "JUEGO":
            ltexto = "Introduce Nombre del Juego (o parte de el): "
            opcion = tk.StringVar()

        ttk.Label(self._frm, text=ltexto).grid(column=0, row=0)
        ttk.Entry(self._frm, textvariable=opcion).grid(column=1, row=0)
        ttk.Button(self._frm, text="Buscar", command=lambda: self.procesar_dato(opcion, tipo)).grid(column=1, row=1)

    def procesar_dato(self, dato, tipo):
        if tipo == "INFORMATICA_TITULO":
            self._linf.buscar_libro(dato.get().upper())
        if tipo == "INFORMATICA_MODIFICAR":
            self._linf.modificar_libro(dato.get())
        if tipo == "INFORMATICA_BORRAR":
            self._linf.borrar_libro(dato.get())
        if tipo == "TREN_TITULO":
            self._ltren.buscar_libro(dato.get().upper())
        if tipo == "TREN_MODIFICAR":
            self._ltren.modificar_libro(dato.get())
        if tipo == "TREN_BORRAR":
            self._ltren.borrar_libro(dato.get())
        if tipo == "CD_TITULO":
            self._cds.buscar_cd(dato.get().upper())
        if tipo == "CD_MODIFICAR":
            self._cds.modificar_cd(dato.get())
        if tipo == "CD_BORRAR":
            self._cds.borrar_cd(dato.get())
        if tipo == "ELECTRONICO_TITULO":
            self._lelec.buscar_libro(dato.get().upper())
        if tipo == "ELECTRONICO_MODIFICAR":
            self._lelec.modificar_libro(dato.get())
        if tipo == "ELECTRONICO_BORRAR":
            self._lelec.borrar_libro(dato.get())
        if tipo == "APLICACION_APLICACION":
            self._app.buscar_aplicacion(dato.get().upper())
        if tipo == "APLICACION_MODIFICAR":
            self._app.modificar_aplicacion(dato.get())
        if tipo == "APLICACION_BORRAR":
            self._app.borrar_aplicacion(dato.get())
        if tipo == "JUEGO_JUEGO":
            self._juego.buscar_juego(dato.get().upper())
        if tipo == "JUEGO_MODIFICAR":
            self._juego.modificar_juego(dato.get())
        if tipo == "JUEGO_BORRAR":
            self._juego.borrar_juego(dato.get())

    def alta_libro_informatica(self):
        self._frm.destroy()
        self._frm = ttk.Frame(self._ventana)
        self._frm.grid()
        self._frm.pack(side="left", fill="both", expand=True)

        ttk.Label(self._frm, text="Título:".ljust(15, ' ')).grid(column=0, row=0)
        titulo = tk.StringVar()
        ttk.Entry(self._frm, textvariable=titulo).grid(column=1, row=0)
        ttk.Label(self._frm, text="Autor:".ljust(15, ' ')).grid(column=0, row=1)
        autor = tk.StringVar()
        ttk.Entry(self._frm, textvariable=autor).grid(column=1, row=1)
        ttk.Label(self._frm, text="Editorial:".ljust(15, ' ')).grid(column=0, row=2)
        editorial = tk.StringVar()
        ttk.Entry(self._frm, textvariable=editorial).grid(column=1, row=2)
        ttk.Label(self._frm, text="Año:".ljust(15, ' ')).grid(column=0, row=3)
        anyo = tk.IntVar()
        ttk.Entry(self._frm, textvariable=anyo).grid(column=1, row=3)
        ttk.Label(self._frm, text="Tipo:".ljust(15, ' ')).grid(column=0, row=4)
        tipo = tk.StringVar()
        ttk.Entry(self._frm, textvariable=tipo).grid(column=1, row=4)
        ttk.Label(self._frm, text="SubTipo:".ljust(15, ' ')).grid(column=0, row=5)
        subtipo = tk.StringVar()
        ttk.Entry(self._frm, textvariable=subtipo).grid(column=1, row=5)
        ttk.Label(self._frm, text="Leído:".ljust(15, ' ')).grid(column=0, row=6)
        leido = tk.StringVar()
        ttk.Entry(self._frm, textvariable=leido).grid(column=1, row=6)
        ttk.Button(self._frm, text="Alta",
                   command=lambda: self.procesar_alta("INFORMATICA_ALTA",
                                                      titulo.get().upper(), autor.get().upper(),
                                                      editorial.get().upper(), anyo.get(), tipo.get().upper(),
                                                      subtipo.get().upper(), leido.get().upper())).grid(column=1, row=8)

    def alta_libro_trenes(self):
        self._frm.destroy()
        self._frm = ttk.Frame(self._ventana)
        self._frm.grid()
        self._frm.pack(side="left", fill="both", expand=True)

        ttk.Label(self._frm, text="Título:".ljust(15, ' ')).grid(column=0, row=0)
        titulo = tk.StringVar()
        ttk.Entry(self._frm, textvariable=titulo).grid(column=1, row=0)
        ttk.Label(self._frm, text="Autor:".ljust(15, ' ')).grid(column=0, row=1)
        autor = tk.StringVar()
        ttk.Entry(self._frm, textvariable=autor).grid(column=1, row=1)
        ttk.Label(self._frm, text="Editorial:".ljust(15, ' ')).grid(column=0, row=2)
        editorial = tk.StringVar()
        ttk.Entry(self._frm, textvariable=editorial).grid(column=1, row=2)
        ttk.Label(self._frm, text="Año:".ljust(15, ' ')).grid(column=0, row=3)
        anyo = tk.IntVar()
        ttk.Entry(self._frm, textvariable=anyo).grid(column=1, row=3)
        ttk.Label(self._frm, text="Leído:".ljust(15, ' ')).grid(column=0, row=4)
        leido = tk.StringVar()
        ttk.Entry(self._frm, textvariable=leido).grid(column=1, row=4)
        ttk.Button(self._frm, text="Alta",
                   command=lambda: self.procesar_alta("TREN_ALTA",
                                                      titulo.get().upper(), autor.get().upper(),
                                                      editorial.get().upper(), anyo.get(),
                                                      leido.get().upper())).grid(column=1, row=5)

    def alta_libro_electronico(self):
        self._frm.destroy()
        self._frm = ttk.Frame(self._ventana)
        self._frm.grid()
        self._frm.pack(side="left", fill="both", expand=True)

        ttk.Label(self._frm, text="Título:".ljust(15, ' ')).grid(column=0, row=0)
        titulo = tk.StringVar()
        ttk.Entry(self._frm, textvariable=titulo).grid(column=1, row=0)
        ttk.Label(self._frm, text="Autor:".ljust(15, ' ')).grid(column=0, row=1)
        autor = tk.StringVar()
        ttk.Entry(self._frm, textvariable=autor).grid(column=1, row=1)
        ttk.Label(self._frm, text="Serie:".ljust(15, ' ')).grid(column=0, row=2)
        serie = tk.StringVar()
        ttk.Entry(self._frm, textvariable=serie).grid(column=1, row=2)
        ttk.Label(self._frm, text="Leído:".ljust(15, ' ')).grid(column=0, row=3)
        leido = tk.StringVar()
        ttk.Entry(self._frm, textvariable=leido).grid(column=1, row=3)
        ttk.Button(self._frm, text="Alta",
                   command=lambda: self.procesar_alta("ELECTRONICO_ALTA",
                                                      titulo.get().upper(), autor.get().upper(),
                                                      serie.get().upper(),
                                                      leido.get().upper())).grid(column=1, row=5)

    def alta_cds(self):
        self._frm.destroy()
        self._frm = ttk.Frame(self._ventana)
        self._frm.grid()
        self._frm.pack(side="left", fill="both", expand=True)

        ttk.Label(self._frm, text="Título:".ljust(15, ' ')).grid(column=0, row=0)
        titulo = tk.StringVar()
        ttk.Entry(self._frm, textvariable=titulo).grid(column=1, row=0)
        ttk.Label(self._frm, text="Grupo:".ljust(15, ' ')).grid(column=0, row=1)
        grupo = tk.StringVar()
        ttk.Entry(self._frm, textvariable=grupo).grid(column=1, row=1)
        ttk.Label(self._frm, text="Año:".ljust(15, ' ')).grid(column=0, row=2)
        anyo = tk.IntVar()
        ttk.Entry(self._frm, textvariable=anyo).grid(column=1, row=2)
        ttk.Label(self._frm, text="Notas:".ljust(15, ' ')).grid(column=0, row=3)
        notas = tk.StringVar()
        ttk.Entry(self._frm, textvariable=notas).grid(column=1, row=3)
        ttk.Label(self._frm, text="Falta:".ljust(15, ' ')).grid(column=0, row=4)
        falta = tk.StringVar()
        ttk.Entry(self._frm, textvariable=falta).grid(column=1, row=4)
        ttk.Label(self._frm, text="Tipo:".ljust(15, ' ')).grid(column=0, row=5)
        tipo = tk.StringVar()
        ttk.Entry(self._frm, textvariable=tipo).grid(column=1, row=5)
        ttk.Button(self._frm, text="Alta",
                   command=lambda: self.procesar_alta("CD_ALTA",
                                                      titulo.get().upper(), grupo.get().upper(), anyo.get(),
                                                      notas.get().upper(), falta.get().upper(),
                                                      tipo.get().upper())).grid(column=1, row=7)

    def alta_aplicacion(self):
        self._frm.destroy()
        self._frm = ttk.Frame(self._ventana)
        self._frm.grid()
        self._frm.pack(side="left", fill="both", expand=True)

        ttk.Label(self._frm, text="Aplicacion:".ljust(15, ' ')).grid(column=0, row=0)
        aplicacion = tk.StringVar()
        ttk.Entry(self._frm, textvariable=aplicacion).grid(column=1, row=0)
        ttk.Label(self._frm, text="Origen:".ljust(15, ' ')).grid(column=0, row=1)
        origen = tk.StringVar()
        ttk.Entry(self._frm, textvariable=origen).grid(column=1, row=1)
        ttk.Label(self._frm, text="Instalar:".ljust(15, ' ')).grid(column=0, row=2)
        instalar = tk.StringVar()
        ttk.Entry(self._frm, textvariable=instalar).grid(column=1, row=2)
        ttk.Label(self._frm, text="Favoritos:".ljust(15, ' ')).grid(column=0, row=3)
        favoritos = tk.StringVar()
        ttk.Entry(self._frm, textvariable=favoritos).grid(column=1, row=3)
        ttk.Label(self._frm, text="Notas:".ljust(15, ' ')).grid(column=0, row=4)
        notas = tk.StringVar()
        ttk.Entry(self._frm, textvariable=notas).grid(column=1, row=4)
        ttk.Button(self._frm, text="Alta",
                   command=lambda: self.procesar_alta("APLICACION_ALTA",
                                                      aplicacion.get().upper(), origen.get().upper(),
                                                      instalar.get().upper(), favoritos.get().upper(),
                                                      notas.get().upper())).grid(column=1, row=5)

    def alta_juego(self):
        self._frm.destroy()
        self._frm = ttk.Frame(self._ventana)
        self._frm.grid()
        self._frm.pack(side="left", fill="both", expand=True)

        ttk.Label(self._frm, text="Nombre:".ljust(15, ' ')).grid(column=0, row=0)
        nombre = tk.StringVar()
        ttk.Entry(self._frm, textvariable=nombre).grid(column=1, row=0)
        ttk.Label(self._frm, text="Tipo:".ljust(15, ' ')).grid(column=0, row=1)
        tipo = tk.StringVar()
        ttk.Entry(self._frm, textvariable=tipo).grid(column=1, row=1)
        ttk.Label(self._frm, text="Instalar:".ljust(15, ' ')).grid(column=0, row=2)
        instalar = tk.StringVar()
        ttk.Entry(self._frm, textvariable=instalar).grid(column=1, row=2)
        ttk.Label(self._frm, text="Origen:".ljust(15, ' ')).grid(column=0, row=3)
        origen = tk.StringVar()
        ttk.Entry(self._frm, textvariable=origen).grid(column=1, row=3)
        ttk.Label(self._frm, text="Notas:".ljust(15, ' ')).grid(column=0, row=4)
        notas = tk.StringVar()
        ttk.Entry(self._frm, textvariable=notas).grid(column=1, row=4)
        ttk.Button(self._frm, text="Alta",
                   command=lambda: self.procesar_alta("JUEGO_ALTA",
                                                      nombre.get().upper(), tipo.get().upper(),
                                                      instalar.get().upper(), origen.get().upper(),
                                                      notas.get().upper())).grid(column=1, row=5)

    def modificar_libro_informatica(self, entrada):
        self._frm.destroy()
        self._frm = ttk.Frame(self._ventana)
        self._frm.grid()
        self._frm.pack(side="left", fill="both", expand=True)

        identificador = tk.IntVar()
        identificador.set(entrada[0])
        ttk.Label(self._frm, text="Título:".ljust(15, ' ')).grid(column=0, row=0)
        titulo = tk.StringVar()
        titulo.set(entrada[1])
        ttk.Entry(self._frm, textvariable=titulo).grid(column=1, row=0)
        ttk.Label(self._frm, text="Autor:".ljust(15, ' ')).grid(column=0, row=1)
        autor = tk.StringVar()
        autor.set(entrada[2])
        ttk.Entry(self._frm, textvariable=autor).grid(column=1, row=1)
        ttk.Label(self._frm, text="Editorial:".ljust(15, ' ')).grid(column=0, row=2)
        editorial = tk.StringVar()
        editorial.set(entrada[3])
        ttk.Entry(self._frm, textvariable=editorial).grid(column=1, row=2)
        ttk.Label(self._frm, text="Año:".ljust(15, ' ')).grid(column=0, row=3)
        anyo = tk.IntVar()
        anyo.set(entrada[4])
        ttk.Entry(self._frm, textvariable=anyo).grid(column=1, row=3)
        ttk.Label(self._frm, text="Tipo:".ljust(15, ' ')).grid(column=0, row=4)
        tipo = tk.StringVar()
        tipo.set(entrada[5])
        ttk.Entry(self._frm, textvariable=tipo).grid(column=1, row=4)
        ttk.Label(self._frm, text="SubTipo:".ljust(15, ' ')).grid(column=0, row=5)
        subtipo = tk.StringVar()
        subtipo.set(entrada[6])
        ttk.Entry(self._frm, textvariable=subtipo).grid(column=1, row=5)
        ttk.Label(self._frm, text="Leído:".ljust(15, ' ')).grid(column=0, row=6)
        leido = tk.StringVar()
        leido.set(entrada[7])
        ttk.Entry(self._frm, textvariable=leido).grid(column=1, row=6)
        ttk.Button(self._frm, text="Modificar",
                   command=lambda: self.procesar_alta("INFORMATICA_MODIFICAR",
                                                      titulo.get().upper(),
                                                      autor.get().upper(), editorial.get().upper(),
                                                      anyo.get(), tipo.get().upper(), subtipo.get().upper(),
                                                      leido.get().upper(), identificador.get())).grid(column=1, row=7)

    def modificar_libro_trenes(self, entrada):
        self._frm.destroy()
        self._frm = ttk.Frame(self._ventana)
        self._frm.grid()
        self._frm.pack(side="left", fill="both", expand=True)

        identificador = tk.IntVar()
        identificador.set(entrada[0])
        ttk.Label(self._frm, text="Título:".ljust(15, ' ')).grid(column=0, row=0)
        titulo = tk.StringVar()
        titulo.set(entrada[1])
        ttk.Entry(self._frm, textvariable=titulo).grid(column=1, row=0)
        ttk.Label(self._frm, text="Autor:".ljust(15, ' ')).grid(column=0, row=1)
        autor = tk.StringVar()
        autor.set(entrada[2])
        ttk.Entry(self._frm, textvariable=autor).grid(column=1, row=1)
        ttk.Label(self._frm, text="Editorial:".ljust(15, ' ')).grid(column=0, row=2)
        editorial = tk.StringVar()
        editorial.set(entrada[3])
        ttk.Entry(self._frm, textvariable=editorial).grid(column=1, row=2)
        ttk.Label(self._frm, text="Año:".ljust(15, ' ')).grid(column=0, row=3)
        anyo = tk.IntVar()
        anyo.set(entrada[4])
        ttk.Entry(self._frm, textvariable=anyo).grid(column=1, row=3)
        ttk.Label(self._frm, text="Leído:".ljust(15, ' ')).grid(column=0, row=4)
        leido = tk.StringVar()
        leido.set(entrada[5])
        ttk.Entry(self._frm, textvariable=leido).grid(column=1, row=4)
        ttk.Button(self._frm, text="Modificar",
                   command=lambda: self.procesar_alta("TREN_MODIFICAR",
                                                      titulo.get().upper(), autor.get().upper(),
                                                      editorial.get().upper(), anyo.get(), leido.get().upper(),
                                                      identificador.get())).grid(column=1, row=5)

    def modificar_libro_electronico(self, entrada):
        self._frm.destroy()
        self._frm = ttk.Frame(self._ventana)
        self._frm.grid()
        self._frm.pack(side="left", fill="both", expand=True)

        identificador = tk.IntVar()
        identificador.set(entrada[0])
        ttk.Label(self._frm, text="Título:".ljust(15, ' ')).grid(column=0, row=0)
        titulo = tk.StringVar()
        titulo.set(entrada[1])
        ttk.Entry(self._frm, textvariable=titulo).grid(column=1, row=0)
        ttk.Label(self._frm, text="Autor:".ljust(15, ' ')).grid(column=0, row=1)
        autor = tk.StringVar()
        autor.set(entrada[2])
        ttk.Entry(self._frm, textvariable=autor).grid(column=1, row=1)
        ttk.Label(self._frm, text="Serie:".ljust(15, ' ')).grid(column=0, row=2)
        serie = tk.StringVar()
        serie.set(entrada[3])
        ttk.Entry(self._frm, textvariable=serie).grid(column=1, row=2)
        ttk.Label(self._frm, text="Leído:".ljust(15, ' ')).grid(column=0, row=3)
        leido = tk.StringVar()
        leido.set(entrada[4])
        ttk.Entry(self._frm, textvariable=leido).grid(column=1, row=3)
        ttk.Button(self._frm, text="Modificar",
                   command=lambda: self.procesar_alta("ELECTRONICO_MODIFICAR",
                                                      titulo.get().upper(), autor.get().upper(),
                                                      serie.get().upper(), leido.get().upper(),
                                                      identificador.get())).grid(column=1, row=5)

    def modificar_cds(self, entrada):
        self._frm.destroy()
        self._frm = ttk.Frame(self._ventana)
        self._frm.grid()
        self._frm.pack(side="left", fill="both", expand=True)

        identificador = tk.IntVar()
        identificador.set(entrada[0])

        ttk.Label(self._frm, text="Título:".ljust(15, ' ')).grid(column=0, row=0)
        titulo = tk.StringVar()
        titulo.set(entrada[1])
        ttk.Entry(self._frm, textvariable=titulo).grid(column=1, row=0)
        ttk.Label(self._frm, text="Grupo:".ljust(15, ' ')).grid(column=0, row=1)
        grupo = tk.StringVar()
        grupo.set(entrada[2])
        ttk.Entry(self._frm, textvariable=grupo).grid(column=1, row=1)
        ttk.Label(self._frm, text="Año:".ljust(15, ' ')).grid(column=0, row=2)
        anyo = tk.IntVar()
        anyo.set(entrada[3])
        ttk.Entry(self._frm, textvariable=anyo).grid(column=1, row=2)
        ttk.Label(self._frm, text="Notas:".ljust(15, ' ')).grid(column=0, row=3)
        notas = tk.StringVar()
        notas.set(entrada[4])
        ttk.Entry(self._frm, textvariable=notas).grid(column=1, row=3)
        ttk.Label(self._frm, text="Falta:".ljust(15, ' ')).grid(column=0, row=4)
        falta = tk.StringVar()
        falta.set(entrada[5])
        ttk.Entry(self._frm, textvariable=falta).grid(column=1, row=4)
        ttk.Label(self._frm, text="Tipo:".ljust(15, ' ')).grid(column=0, row=5)
        tipo = tk.StringVar()
        tipo.set(entrada[6])
        ttk.Entry(self._frm, textvariable=tipo).grid(column=1, row=5)
        ttk.Button(self._frm, text="Modificar",
                   command=lambda: self.procesar_alta("CD_MODIFICACION",
                                                      titulo.get().upper(), grupo.get().upper(), anyo.get(),
                                                      notas.get().upper(), falta.get().upper(),
                                                      tipo.get().upper(), identificador.get())).grid(column=1, row=7)

    def modificar_aplicacion(self, entrada):
        self._frm.destroy()
        self._frm = ttk.Frame(self._ventana)
        self._frm.grid()
        self._frm.pack(side="left", fill="both", expand=True)

        identificador = tk.IntVar()
        identificador.set(entrada[0])
        ttk.Label(self._frm, text="Aplicación:".ljust(15, ' ')).grid(column=0, row=0)
        aplicacion = tk.StringVar()
        aplicacion.set(entrada[1])
        ttk.Entry(self._frm, textvariable=aplicacion).grid(column=1, row=0)
        ttk.Label(self._frm, text="Origen:".ljust(15, ' ')).grid(column=0, row=1)
        origen = tk.StringVar()
        origen.set(entrada[2])
        ttk.Entry(self._frm, textvariable=origen).grid(column=1, row=1)
        ttk.Label(self._frm, text="Instalar:".ljust(15, ' ')).grid(column=0, row=2)
        instalar = tk.StringVar()
        instalar.set(entrada[3])
        ttk.Entry(self._frm, textvariable=instalar).grid(column=1, row=2)
        ttk.Label(self._frm, text="Favoritos:".ljust(15, ' ')).grid(column=0, row=3)
        favoritos = tk.StringVar()
        favoritos.set(entrada[4])
        ttk.Entry(self._frm, textvariable=favoritos).grid(column=1, row=3)
        ttk.Label(self._frm, text="Notas:".ljust(15, ' ')).grid(column=0, row=4)
        notas = tk.StringVar()
        notas.set(entrada[5])
        ttk.Entry(self._frm, textvariable=notas).grid(column=1, row=4)
        ttk.Button(self._frm, text="Modificar",
                   command=lambda: self.procesar_alta("APLICACION_MODIFICAR",
                                                      aplicacion.get().upper(), origen.get().upper(),
                                                      instalar.get().upper(), favoritos.get().upper(),
                                                      notas.get().upper(), identificador.get())).grid(column=1, row=5)

    def modificar_juego(self, entrada):
        self._frm.destroy()
        self._frm = ttk.Frame(self._ventana)
        self._frm.grid()
        self._frm.pack(side="left", fill="both", expand=True)

        identificador = tk.IntVar()
        identificador.set(entrada[0])
        ttk.Label(self._frm, text="Nombre:".ljust(15, ' ')).grid(column=0, row=0)
        nombre = tk.StringVar()
        nombre.set(entrada[1])
        ttk.Entry(self._frm, textvariable=nombre).grid(column=1, row=0)
        ttk.Label(self._frm, text="Tipo:".ljust(15, ' ')).grid(column=0, row=1)
        tipo = tk.StringVar()
        tipo.set(entrada[2])
        ttk.Entry(self._frm, textvariable=tipo).grid(column=1, row=1)
        ttk.Label(self._frm, text="Instalar:".ljust(15, ' ')).grid(column=0, row=2)
        instalar = tk.StringVar()
        instalar.set(entrada[3])
        ttk.Entry(self._frm, textvariable=instalar).grid(column=1, row=2)
        ttk.Label(self._frm, text="Origen:".ljust(15, ' ')).grid(column=0, row=3)
        origen = tk.StringVar()
        origen.set(entrada[4])
        ttk.Entry(self._frm, textvariable=origen).grid(column=1, row=3)
        ttk.Label(self._frm, text="Notas:".ljust(15, ' ')).grid(column=0, row=4)
        notas = tk.StringVar()
        notas.set(entrada[5])
        ttk.Entry(self._frm, textvariable=notas).grid(column=1, row=4)
        ttk.Button(self._frm, text="Modificar",
                   command=lambda: self.procesar_alta("JUEGO_MODIFICAR",
                                                      nombre.get().upper(), tipo.get().upper(),
                                                      instalar.get().upper(), origen.get().upper(),
                                                      notas.get().upper(), identificador.get())).grid(column=1, row=5)

    def procesar_alta(self, tipo, *args):
        if tipo == "INFORMATICA_ALTA":
            self._linf.alta_libro(list(args))
        elif tipo == "INFORMATICA_MODIFICAR":
            self._linf.procesa_modificar_libro(list(args))
        elif tipo == "TREN_ALTA":
            self._ltren.alta_libro(list(args))
        elif tipo == "TREN_MODIFICAR":
            self._ltren.procesa_modificar_libro(list(args))
        elif tipo == "CD_ALTA":
            self._cds.alta_cd(list(args))
        elif tipo == "CD_MODIFICACION":
            self._cds.procesa_modificar_cd(list(args))
        elif tipo == "ELECTRONICO_ALTA":
            self._lelec.alta_libro(list(args))
        elif tipo == "ELECTRONICO_MODIFICAR":
            self._lelec.procesa_modificar_libro(list(args))
        elif tipo == "APLICACION_ALTA":
            self._app.alta_aplicacion(list(args))
        elif tipo == "APLICACION_MODIFICAR":
            self._app.procesa_modificar_aplicacion(list(args))
        elif tipo == "JUEGO_ALTA":
            self._juego.alta_juego(list(args))
        elif tipo == "JUEGO_MODIFICAR":
            self._juego.procesa_modificar_juego(list(args))

    def pedir_fichero(self, tipfichero, proceso):
        tipos = (("Fichero "+tipfichero, "*."+tipfichero), )

        filename = filedialog.asksaveasfilename(initialdir=".", title="Selecciona Fichero", filetypes=tipos)
        if proceso == "INFORMATICA":
            if tipfichero == "csv":
                self._linf.export_csv(filename)
            else:
                self._linf.export_excel(filename)
        elif proceso == "TREN":
            if tipfichero == "csv":
                self._ltren.export_csv(filename)
            else:
                self._ltren.export_excel(filename)
        elif proceso == "CD":
            if tipfichero == "csv":
                self._cds.export_csv(filename)
            else:
                self._cds.export_excel(filename)
        elif proceso == "ELECTRONICO":
            if tipfichero == "csv":
                self._lelec.export_csv(filename)
            else:
                self._lelec.export_excel(filename)
        elif proceso == "APLICACION":
            if tipfichero == "csv":
                self._app.export_csv(filename)
            else:
                self._app.export_excel(filename)
        elif proceso == "JUEGO":
            if tipfichero == "csv":
                self._juego.export_csv(filename)
            else:
                self._juego.export_excel(filename)

    def importar_fichero(self, tipfichero, proceso):
        tipos = (("Fichero "+tipfichero, "*."+tipfichero), )

        filename = filedialog.askopenfilename(initialdir=".", title="Selecciona Fichero", filetypes=tipos)
        if proceso == "INFORMATICA":
            self._linf.import_csv(filename)
        elif proceso == "TREN":
            self._ltren.import_csv(filename)
        elif proceso == "CD":
            self._cds.import_csv(filename)
        elif proceso == "ELECTRONICO":
            self._lelec.import_csv(filename)
        elif proceso == "APLICACION":
            self._app.import_csv(filename)
        elif proceso == "JUEGO":
            self._juego.import_csv(filename)
