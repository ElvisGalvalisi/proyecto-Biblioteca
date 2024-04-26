import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import ConexionDB

class Libro:
    def __init__(self):
        # se crea la conexión
        self.con = ConexionDB.Conectarse()
        self.con.conectar()

        self.frmLibro = tk.Tk()
        self.frmLibro.title("Gestor de Libros")
        self.frmLibro.geometry("430x450")
        self.frmLibro.resizable(0,0)

        self.panel = ttk.Notebook(self.frmLibro)
        self.panel.grid(column =0, row =0, padx = 5, pady =5)

        # mostramos las pestañas
        self.pestanaBuscar()
        self.pestanaAlta()
        #self.pestanaModificar()
        #self.pestanaEliminar()
        
        



        self.frmLibro.mainloop()
    """--------------------------------------------------------------------------------------------------------"""

    def pestanaBuscar(self):
        # se crear el frame buscar
        self.frameBuscarB = ttk.Frame(self.panel)
        self.panel.add(self.frameBuscarB, text = "BUSCAR")

        # se crea el label frame de buscar
        self.lblFrameBuscarB = ttk.Labelframe(self.frameBuscarB, text = "Ingresar nombre: ")
        self.lblFrameBuscarB.grid(column =0, row =0, padx = 5, pady =5)

        # label buscar
        self.datoBuscarLibroB = tk.StringVar()
        self.txtBuscarLibroB = ttk.Entry(self.lblFrameBuscarB, width = 30, textvariable = self.datoBuscarLibroB)
        self.txtBuscarLibroB.grid(column =0, row =0, padx = 5, pady =5, sticky="e")

        #button Buscar
        self.btnBuscarLibro = ttk.Button(self.lblFrameBuscarB, text = "BUSCAR", command = self.buscarTit)
        self.btnBuscarLibro.grid(column =1, row =0, padx = 5, pady =5)


        # se crea el label frame de buscar
        self.lblFrameDatosB = ttk.Labelframe(self.frameBuscarB, text = "Datos: ")
        self.lblFrameDatosB.grid(column =0, row =1, padx = 5, pady =5, sticky="n")

        # label 
        self.lblID = ttk.Label(self.lblFrameDatosB, text = "ID: ")
        self.lblID.grid(column =0, row =0, padx = 5, pady =5, sticky="w")

        self.lblTitulo = ttk.Label(self.lblFrameDatosB, text = "TÍTULO: ")
        self.lblTitulo.grid(column =0, row =1, padx = 5, pady =5, sticky="w")

        self.lblAutor = ttk.Label(self.lblFrameDatosB, text = "AUTOR: ")
        self.lblAutor.grid(column =0, row =2, padx = 5, pady =5, sticky="w")

        self.lblEdicion = ttk.Label(self.lblFrameDatosB, text = "EDICIÓN: ")
        self.lblEdicion.grid(column =0, row =3, padx = 5, pady =5, sticky="w")

        self.lblLugarImpresion = ttk.Label(self.lblFrameDatosB, text = "LUGAR DE IMPRESIÓN: ")
        self.lblLugarImpresion.grid(column =0, row =4, padx = 5, pady =5, sticky="w")

        self.lblEditorial = ttk.Label(self.lblFrameDatosB, text = "EDITORIAL: ")
        self.lblEditorial.grid(column =0, row =5, padx = 5, pady =5, sticky="w")

        self.lblTraduccion = ttk.Label(self.lblFrameDatosB, text = "TRADUCCIÓN: ")
        self.lblTraduccion.grid(column =0, row =6, padx = 5, pady =5, sticky="w")

        self.lblPaginas = ttk.Label(self.lblFrameDatosB, text = "CANT. PAGINAS: ")
        self.lblPaginas.grid(column =0, row =7, padx = 5, pady =5, sticky="w")

        self.lblEstado = ttk.Label(self.lblFrameDatosB, text = "ESTADO: ")
        self.lblEstado.grid(column =0, row =8, padx = 5, pady =5, sticky="w")


        # Entry
        self.datoIDB = tk.StringVar()
        self.txtIDLibroB = ttk.Entry(self.lblFrameDatosB, width = 40, textvariable = self.datoIDB)
        self.txtIDLibroB.grid(column =1, row =0, padx = 5, pady =5)

        self.datoTituloB = tk.StringVar()
        self.txtTituloB = ttk.Entry(self.lblFrameDatosB, width = 40, textvariable = self.datoTituloB)#, state= "disabled")
        self.txtTituloB.grid(column =1, row =1, padx = 5, pady =5)

        self.datoAutorB = tk.StringVar()
        self.txtAutorB = ttk.Entry(self.lblFrameDatosB, width = 40, textvariable = self.datoAutorB)#, state="readonly")
        self.txtAutorB.grid(column =1, row =2, padx = 5, pady =5)

        self.datoEdicionB = tk.StringVar()
        self.txtEdicionB = ttk.Entry(self.lblFrameDatosB, width = 40, textvariable = self.datoEdicionB)#, state="readonly")
        self.txtEdicionB.grid(column =1, row =3, padx = 5, pady =5)

        self.datoLugarImpresionB = tk.StringVar()
        self.txtLugarImpresionB = ttk.Entry(self.lblFrameDatosB, width = 40, textvariable = self.datoLugarImpresionB)#, state="readonly")
        self.txtLugarImpresionB.grid(column =1, row =4, padx = 5, pady =5)

        self.datoEditorialB = tk.StringVar()
        self.txtEditorialB = ttk.Entry(self.lblFrameDatosB, width = 40, textvariable = self.datoEditorialB)#, state="readonly")
        self.txtEditorialB.grid(column =1, row =5, padx = 5, pady =5)

        
        
        self.cmbxTraduccionB = ttk.Combobox(self.lblFrameDatosB, width = 37)#, state= "disabled")
        self.cmbxTraduccionB.grid(column =1, row =6, padx = 5, pady =5)
        self.cmbxTraduccionB["values"] = ["SI", "NO"]
        self.datoTraduccionB = self.cmbxTraduccionB.get()
        self.indexCmbxTraduccionB = self.cmbxTraduccionB.current() # se obtiene el valor de índice 


        self.datoPaginasB = tk.StringVar()
        self.txtPaginasB = ttk.Entry(self.lblFrameDatosB, width = 40, textvariable = self.datoPaginasB)#, state="readonly")
        self.txtPaginasB.grid(column =1, row =7, padx = 5, pady =5)

        self.cmbxEstadoB = ttk.Combobox(self.lblFrameDatosB, width = 37)#, state= "disabled")
        self.cmbxEstadoB.grid(column =1, row =8, padx = 5, pady =5)
        self.cmbxEstadoB["values"] = ["Seleccionar...", "Prestado", "Disponible", "Retraso", "Restauración"]
        self.datoEstadoB = self.cmbxEstadoB.get()
        self.indexCmbxEstadoB = self.cmbxEstadoB.current() # se obtiene el valor de índice
        self.cmbxEstadoB.set("Seleccionar...")

    """--------------------------------------------------------------------------------------------------------"""

    def pestanaAlta(self):

        # se crea el frame Nuevo
        self.frameNuevo = ttk.Frame(self.panel)
        self.panel.add(self.frameNuevo, text = "NUEVO")


        # se crea el label frame de Nuevo
        self.lblFrameDatos = ttk.Labelframe(self.frameNuevo, text = "Datos: ")
        self.lblFrameDatos.grid(column =0, row =0, padx = 5, pady =5, sticky="n")

        # label 
        self.lblIDA = ttk.Label(self.lblFrameDatos, text = "ID: ")
        self.lblIDA.grid(column =0, row =0, padx = 5, pady =5, sticky="w")

        self.lblTituloA = ttk.Label(self.lblFrameDatos, text = "TÍTULO: ")
        self.lblTituloA.grid(column =0, row =1, padx = 5, pady =5, sticky="w")

        self.lblAutorA = ttk.Label(self.lblFrameDatos, text = "AUTOR: ")
        self.lblAutorA.grid(column =0, row =2, padx = 5, pady =5, sticky="w")

        self.lblEdicionA = ttk.Label(self.lblFrameDatos, text = "EDICIÓN: ")
        self.lblEdicionA.grid(column =0, row =3, padx = 5, pady =5, sticky="w")

        self.lblLugarImpresionA = ttk.Label(self.lblFrameDatos, text = "LUGAR DE IMPRESIÓN: ")
        self.lblLugarImpresionA.grid(column =0, row =4, padx = 5, pady =5, sticky="w")

        self.lblEditorialA = ttk.Label(self.lblFrameDatos, text = "EDITORIAL: ")
        self.lblEditorialA.grid(column =0, row =5, padx = 5, pady =5, sticky="w")

        self.lblTraduccionA = ttk.Label(self.lblFrameDatos, text = "TRADUCCIÓN: ")
        self.lblTraduccionA.grid(column =0, row =6, padx = 5, pady =5, sticky="w")

        self.lblPaginasA = ttk.Label(self.lblFrameDatos, text = "CANT. PAGINAS: ")
        self.lblPaginasA.grid(column =0, row =7, padx = 5, pady =5, sticky="w")

        self.lblEstadoA = ttk.Label(self.lblFrameDatos, text = "ESTADO: ")
        self.lblEstadoA.grid(column =0, row =8, padx = 5, pady =5, sticky="w")


        # Entry
        self.datoIDA = tk.StringVar()
        self.txtIDLibroA = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoIDA, state="disabled")
        self.txtIDLibroA.grid(column =1, row =0, padx = 5, pady =5)

        self.datoTituloA = tk.StringVar()
        self.txtTituloA = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoTituloA)
        self.txtTituloA.grid(column =1, row =1, padx = 5, pady =5)

        self.datoAutorA = tk.StringVar()
        self.txtAutorA = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoAutorA)
        self.txtAutorA.grid(column =1, row =2, padx = 5, pady =5)

        self.datoEdicionA = tk.StringVar()
        self.txtEdicionA = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoEdicionA)
        self.txtEdicionA.grid(column =1, row =3, padx = 5, pady =5)

        self.datoLugarImpresionA = tk.StringVar()
        self.txtLugarImpresionA = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoLugarImpresionA)
        self.txtLugarImpresionA.grid(column =1, row =4, padx = 5, pady =5)

        self.datoEditorialA = tk.StringVar()
        self.txtEditorialA = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoEditorialA)
        self.txtEditorialA.grid(column =1, row =5, padx = 5, pady =5)

        
        
        self.cmbxTraduccionA = ttk.Combobox(self.lblFrameDatos, width = 37, state = "readonly")
        self.cmbxTraduccionA.grid(column =1, row =6, padx = 5, pady =5)
        self.cmbxTraduccionA["values"] = ["SI", "NO"]
        self.datoTraduccionA = self.cmbxTraduccionA.get()
        self.indexCmbxTraduccionA = self.cmbxTraduccionA.current() # se obtiene el valor de índice 


        self.datoPaginasA = tk.StringVar()
        self.txtPaginasA = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoPaginasA)
        self.txtPaginasA.grid(column =1, row =7, padx = 5, pady =5)

        self.cmbxEstadoA = ttk.Combobox(self.lblFrameDatos, width = 37, state = "readonly")
        self.cmbxEstadoA.grid(column =1, row =8, padx = 5, pady =5)
        self.cmbxEstadoA["values"] = ["Seleccionar...", "Prestado", "Disponible", "Retraso", "Restauración"]
        self.datoEstadoA = self.cmbxEstadoA.get()
        self.indexCmbxEstadoA = self.cmbxEstadoA.current() # se obtiene el valor de índice
        self.cmbxEstadoA.set("Seleccionar...")

        #Label frame operaciones
        self.lblFrameAccion = ttk.Labelframe(self.frameNuevo)
        self.lblFrameAccion.grid(column = 0, row = 1, padx =5, pady = 5)
        # button Guardar
        self.btnGuardar = ttk.Button(self.lblFrameAccion, text = "GUARDAR", command = self.nuevoLibro) 
        self.btnGuardar.grid(column = 0, row = 0, padx = 5, pady = 5)

        # button Cancelar
        self.btnCancelar = ttk.Button(self.lblFrameAccion, text = "CANCELAR", command = self.cancelar) # DEFINIR EL COMMMAND
        self.btnCancelar.grid(column = 1, row = 0, padx = 5, pady = 5)

    """--------------------------------------------------------------------------------------------------------"""
    
    def pestanaModificar(self):

        # se crea el frame Modifica
        self.frameModifica = ttk.Frame(self.panel)
        self.panel.add(self.frameModifica, text = "MODIFICAR")


        # se crea el label frame de Modificar
        self.lblFrameDatos = ttk.Labelframe(self.frameModifica, text = "Datos: ")
        self.lblFrameDatos.grid(column =0, row =0, padx = 5, pady =5, sticky="n")

        # label 
        self.lblID = ttk.Label(self.lblFrameDatos, text = "ID: ")
        self.lblID.grid(column =0, row =0, padx = 5, pady =5, sticky="w")

        self.lblTitulo = ttk.Label(self.lblFrameDatos, text = "TÍTULO: ")
        self.lblTitulo.grid(column =0, row =1, padx = 5, pady =5, sticky="w")

        self.lblAutor = ttk.Label(self.lblFrameDatos, text = "AUTOR: ")
        self.lblAutor.grid(column =0, row =2, padx = 5, pady =5, sticky="w")

        self.lblEdicion = ttk.Label(self.lblFrameDatos, text = "EDICIÓN: ")
        self.lblEdicion.grid(column =0, row =3, padx = 5, pady =5, sticky="w")

        self.lblLugarImpresion = ttk.Label(self.lblFrameDatos, text = "LUGAR DE IMPRESIÓN: ")
        self.lblLugarImpresion.grid(column =0, row =4, padx = 5, pady =5, sticky="w")

        self.lblEditorial = ttk.Label(self.lblFrameDatos, text = "EDITORIAL: ")
        self.lblEditorial.grid(column =0, row =5, padx = 5, pady =5, sticky="w")

        self.lblTraduccion = ttk.Label(self.lblFrameDatos, text = "TRADUCCIÓN: ")
        self.lblTraduccion.grid(column =0, row =6, padx = 5, pady =5, sticky="w")

        self.lblPaginas = ttk.Label(self.lblFrameDatos, text = "CANT. PAGINAS: ")
        self.lblPaginas.grid(column =0, row =7, padx = 5, pady =5, sticky="w")

        self.lblEstado = ttk.Label(self.lblFrameDatos, text = "ESTADO: ")
        self.lblEstado.grid(column =0, row =8, padx = 5, pady =5, sticky="w")


        # Entry
        self.datoID = tk.StringVar()
        self.txtIDLibro = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoID, state="disabled")
        self.txtIDLibro.grid(column =1, row =0, padx = 5, pady =5)

        self.datoTitulo = tk.StringVar()
        self.txtTitulo = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoTitulo, state="normal")
        self.txtTitulo.grid(column =1, row =1, padx = 5, pady =5)

        self.datoAutor = tk.StringVar()
        self.txtAutor = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoAutor, state="normal")
        self.txtAutor.grid(column =1, row =2, padx = 5, pady =5)

        self.datoEdicion = tk.StringVar()
        self.txtEdicion = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoEdicion, state="normal")
        self.txtEdicion.grid(column =1, row =3, padx = 5, pady =5)

        self.datoLugarImpresion = tk.StringVar()
        self.txtLugarImpresion = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoLugarImpresion, state="normal")
        self.txtLugarImpresion.grid(column =1, row =4, padx = 5, pady =5)

        self.datoEditorial = tk.StringVar()
        self.txtEditorial = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoEditorial, state="normal")
        self.txtEditorial.grid(column =1, row =5, padx = 5, pady =5)

        
        
        self.cmbxTraduccion = ttk.Combobox(self.lblFrameDatos, width = 37, state="normal")
        self.cmbxTraduccion.grid(column =1, row =6, padx = 5, pady =5)
        self.cmbxTraduccion["values"] = ["SI", "NO"]
        self.datoTraduccion = self.cmbxTraduccion.get()
        self.indexCmbxTraduccion = self.cmbxTraduccion.current() # se obtiene el valor de índice 


        self.datoPaginas = tk.StringVar()
        self.txtPaginas = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoPaginas, state="normal")
        self.txtPaginas.grid(column =1, row =7, padx = 5, pady =5)

        self.cmbxEstado = ttk.Combobox(self.lblFrameDatos, width = 37, state="normal")
        self.cmbxEstado.grid(column =1, row =8, padx = 5, pady =5)
        self.cmbxEstado["values"] = ["Seleccionar...", "Prestado", "Disponible", "Retraso", "Restauración"]
        self.datoEstado = self.cmbxEstado.get()
        self.indexCmbxEstado = self.cmbxEstado.current() # se obtiene el valor de índice
        self.cmbxEstado.set("Seleccionar...")

        #Label frame operaciones
        self.lblFrameAccion = ttk.Labelframe(self.frameModifica)
        self.lblFrameAccion.grid(column = 0, row = 1, padx =5, pady = 5)
        # button Guardar
        self.btnGuardar = ttk.Button(self.lblFrameAccion, text = "MODIFICAR") # DEFINIR EL COMMMAND
        self.btnGuardar.grid(column = 0, row = 0, padx = 5, pady = 5)

        # button Cancelar
        self.btnCancelar = ttk.Button(self.lblFrameAccion, text = "CANCELAR") # DEFINIR EL COMMMAND
        self.btnCancelar.grid(column = 1, row = 0, padx = 5, pady = 5)

    """--------------------------------------------------------------------------------------------------------"""

    def pestanaEliminar(self):

        # se crea el frame Eliminar
        self.frameEliminar = ttk.Frame(self.panel)
        self.panel.add(self.frameEliminar, text = "ELIMINAR")

        # se crea el label frame de Eliminar
        self.lblFrameBuscar = ttk.Labelframe(self.frameEliminar, text = "Ingresar nombre: ")
        self.lblFrameBuscar.grid(column =0, row =0, padx = 5, pady =1)

        # label buscar
        self.datoBuscarLibroE = tk.StringVar()
        self.txtBuscarLibroE = ttk.Entry(self.lblFrameBuscar, width = 30, textvariable = self.datoBuscarLibroE)
        self.txtBuscarLibroE.grid(column =0, row =0, padx = 5, pady =1, sticky="e")

        #button Buscar
        self.btnBuscarLibroE = ttk.Button(self.lblFrameBuscar, text = "BUSCAR") # FALTA DEFINIR COMMAND
        self.btnBuscarLibroE.grid(column =1, row =0, padx = 5, pady =1)


        # se crea el label frame de buscar
        self.lblFrameDatos = ttk.Labelframe(self.frameEliminar, text = "Datos: ")
        self.lblFrameDatos.grid(column =0, row =1, padx = 5, pady =0, sticky="n")

        
        # label 
        self.lblID = ttk.Label(self.lblFrameDatos, text = "ID: ")
        self.lblID.grid(column =0, row =0, padx = 5, pady =5, sticky="w")

        self.lblTitulo = ttk.Label(self.lblFrameDatos, text = "TÍTULO: ")
        self.lblTitulo.grid(column =0, row =1, padx = 5, pady =5, sticky="w")

        self.lblAutor = ttk.Label(self.lblFrameDatos, text = "AUTOR: ")
        self.lblAutor.grid(column =0, row =2, padx = 5, pady =5, sticky="w")

        self.lblEdicion = ttk.Label(self.lblFrameDatos, text = "EDICIÓN: ")
        self.lblEdicion.grid(column =0, row =3, padx = 5, pady =5, sticky="w")

        self.lblLugarImpresion = ttk.Label(self.lblFrameDatos, text = "LUGAR DE IMPRESIÓN: ")
        self.lblLugarImpresion.grid(column =0, row =4, padx = 5, pady =5, sticky="w")

        self.lblEditorial = ttk.Label(self.lblFrameDatos, text = "EDITORIAL: ")
        self.lblEditorial.grid(column =0, row =5, padx = 5, pady =5, sticky="w")

        self.lblTraduccion = ttk.Label(self.lblFrameDatos, text = "TRADUCCIÓN: ")
        self.lblTraduccion.grid(column =0, row =6, padx = 5, pady =5, sticky="w")

        self.lblPaginas = ttk.Label(self.lblFrameDatos, text = "CANT. PAGINAS: ")
        self.lblPaginas.grid(column =0, row =7, padx = 5, pady =5, sticky="w")

        self.lblEstado = ttk.Label(self.lblFrameDatos, text = "ESTADO: ")
        self.lblEstado.grid(column =0, row =8, padx = 5, pady =5, sticky="w")


        # Entry
        self.datoID = tk.StringVar()
        self.txtIDLibro = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoID, state="disabled")
        self.txtIDLibro.grid(column =1, row =0, padx = 5, pady =5)

        self.datoTitulo = tk.StringVar()
        self.txtTitulo = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoTitulo, state="disabled")
        self.txtTitulo.grid(column =1, row =1, padx = 5, pady =5)

        self.datoAutor = tk.StringVar()
        self.txtAutor = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoAutor, state="disabled")
        self.txtAutor.grid(column =1, row =2, padx = 5, pady =5)

        self.datoEdicion = tk.StringVar()
        self.txtEdicion = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoEdicion, state="disabled")
        self.txtEdicion.grid(column =1, row =3, padx = 5, pady =5)

        self.datoLugarImpresion = tk.StringVar()
        self.txtLugarImpresion = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoLugarImpresion, state="disabled")
        self.txtLugarImpresion.grid(column =1, row =4, padx = 5, pady =5)

        self.datoEditorial = tk.StringVar()
        self.txtEditorial = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoEditorial, state="disabled")
        self.txtEditorial.grid(column =1, row =5, padx = 5, pady =5)

        
        
        self.cmbxTraduccion = ttk.Combobox(self.lblFrameDatos, width = 37, state= "disabled")
        self.cmbxTraduccion.grid(column =1, row =6, padx = 5, pady =5)
        self.cmbxTraduccion["values"] = ["SI", "NO"]
        self.datoTraduccion = self.cmbxTraduccion.get()
        self.indexCmbxTraduccion = self.cmbxTraduccion.current() # se obtiene el valor de índice 


        self.datoPaginas = tk.StringVar()
        self.txtPaginas = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoPaginas, state="disabled")
        self.txtPaginas.grid(column =1, row =7, padx = 5, pady =5)

        self.cmbxEstado = ttk.Combobox(self.lblFrameDatos, width = 37, state= "disabled")
        self.cmbxEstado.grid(column =1, row =8, padx = 5, pady =5)
        self.cmbxEstado["values"] = ["Seleccionar...", "Prestado", "Disponible", "Retraso", "Restauración"]
        self.datoEstado = self.cmbxEstado.get()
        self.indexCmbxEstado = self.cmbxEstado.current() # se obtiene el valor de índice
        self.cmbxEstado.set("Seleccionar...")

        #Label frame operaciones
        self.lblFrameAccion = ttk.Labelframe(self.frameEliminar)
        self.lblFrameAccion.grid(column = 0, row = 3, padx =5, pady = 0)
        # button Guardar
        self.btnEliminar = ttk.Button(self.lblFrameAccion, text = "ELIMINAR") # DEFINIR EL COMMMAND
        self.btnEliminar.grid(column = 0, row = 0, padx = 5, pady = 1)

        # button Cancelar
        self.btnCancelar = ttk.Button(self.lblFrameAccion, text = "CANCELAR") # DEFINIR EL COMMMAND
        self.btnCancelar.grid(column = 1, row = 0, padx = 5, pady = 1)

    """-----------------------------------FUNCIONES DEL FORMULARIO-------------------------------------------------"""
    def limpiarCampos(self):
        self.datoTituloA.set("")
        self.datoAutorA.set("")
        self.datoEdicionA.set("")
        self.datoLugarImpresionA.set("")
        self.datoEditorialA.set("")
        self.cmbxTraduccionA.set("")
        self.datoPaginasA.set("")
        self.cmbxEstadoA.set("")

    def buscarTit(self): # seguir revisando porque no toma el valor.
        try:
            datoTitulo = (self.txtBuscarLibroB.get())
            print("Dato Tit: ", datoTitulo)
            resp = self.con.buscarTitulo(datoTitulo)
            print("res: ", resp)
            if len(resp) > 1:
                mb.showwarning("¡ATENCIÓN!", "Puede haber más de un registro buscado, se tomará el primero.")

            if len(resp) > 0:
                #var = 9
                #self.datoIDB.set(var)
                self.datoIDB.set(resp[0][0])
                self.datoTituloB.set(resp[0][1])
                self.datoAutorB.set(resp[0][2])
                self.datoEdicionB.set(resp[0][3])
                self.datoLugarImpresionB.set(resp[0][4])
                self.datoEditorialB.set(resp[0][5])
                self.cmbxTraduccionB.set(resp[0][6])
                self.datoPaginasB.set(resp[0][7])
                self.cmbxEstadoB.set(resp[0][8])
            else:
                mb.showinfo("INFORMACIÓN", f"No existen datos que contengan: {datoTitulo}.")
        except:
            mb.showerror("¡Error!", "Se ha encontrado un error al buscar.")

    def nuevoLibro(self):
        try:

            dato = (self.txtTituloA.get(), self.txtAutorA.get(), self.txtEdicionA.get(), self.txtLugarImpresionA.get(), self.txtEditorialA.get(), self.cmbxTraduccionA.get(), self.txtPaginasA.get(), self.cmbxEstadoA.get())
            #Titulo, Autor, Edicion, LugarImpresion, Editorial, Traduccion, Paginas, Estado
            #print(dato)
            self.con.nuevoLibro(dato)
            mb.showinfo("INFORMACIÓN", "Datos guardados con éxito")
            self.limpiarCampos()
        
            self.txtTituloA.focus()
            self.frmLibro.destroy()
        except:
            mb.showwarning("¡ATENCIÓN!", "Los datos no se guardaron correctamente.")
    

    def modificarLibro(self, datoM):
        try:
            datoM = (self.txtTituloA.get(), self.txtAutorA.get(), self.txtEdicionA.get(), self.txtLugarImpresionA.get(), self.txtEditorialA.get(), self.cmbxTraduccionA.get(), self.txtPaginasA.get(), self.cmbxEstadoA.get(), self.txtIDLibro.get())
            self.con.modificarLibro(datoM)
            mb.showinfo("INFORMACIÓN", "El Libro fue modificado con éxito." )
        except:
            mb.showinfo("ATENCIÓN", "El Libro no fue modificado." )

    
    
    def cancelar(self):
        resp = mb.askyesnocancel("Cancelar", "¿Desea Cancelar? \n Se borrarán todos los campos y los cambios no se guardaran.")
        #print(resp)
        if resp == True:
            self.limpiarCampos()
#frm = Libro()
# seguir viendo el boton de nuevoLibro

