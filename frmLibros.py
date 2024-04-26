import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import ConexionDB
import Principal as p

class Libro:
    def __init__(self):
        # se crea la conexión
        self.con = ConexionDB.Conectarse()
        self.con.conectar()

        self.frmLibro = tk.Tk()
        self.frmLibro.title("Gestor de Libros")
        self.frmLibro.geometry("520x480")
        self.frmLibro.resizable(0,0)

        #self.panel = ttk.Notebook(self.frmLibro)
        #self.panel.grid(column =0, row =0, padx = 5, pady =5)

        # mostramos las pestañas
        self.graficos()
        
        self.habilitarCampos()
        self.bloquearBotones()

        
        self.frmLibro.protocol("WM_DELETE_WINDOW", self.cerrarVentana)

    



        self.frmLibro.mainloop()
        
    def cerrarVentana(self):
        resp = mb.askokcancel("¡ATENCIÓN!", "Al cerrar el formulario volverá a la pantalla principal.")
        if resp == True:
            self.frmLibro.destroy()
            p.Principal()

    """--------------------------------------graficos-------------------------------------------------------"""

    def graficos(self):
        # se crea el label frame de buscar
        self.lblFrameBuscar = ttk.Labelframe(self.frmLibro, text = "Ingresar nombre del título: ")
        self.lblFrameBuscar.grid(column =0, row =0, padx = 5, pady =5)

        # label buscar
        self.datoBuscarLibro = tk.StringVar()
        self.txtBuscarLibro = ttk.Entry(self.lblFrameBuscar, width = 30, textvariable = self.datoBuscarLibro)
        self.txtBuscarLibro.grid(column =0, row =0, padx = 5, pady =5, sticky="e")

        #button Buscar
        self.btnBuscarLibro = ttk.Button(self.lblFrameBuscar, text = "BUSCAR", command = self.buscarTit)
        self.btnBuscarLibro.grid(column =1, row =0, padx = 5, pady =5)

        # se crea el label frame de botones
        self.lblFrameComandos = ttk.Labelframe(self.frmLibro, text = "Guardar: ")
        self.lblFrameComandos.grid(column =1, row =1, padx = 5, pady =5)


        #button AMB
        self.btnAltaLibro = ttk.Button(self.lblFrameComandos, text = "ALTA", command = self.nuevoLibro)
        self.btnAltaLibro.grid(column =1, row =0, padx = 5, pady =1)

        self.btnModificarLibro = ttk.Button(self.lblFrameComandos, text = "MODIFICAR", command = self.modificarLibro)
        self.btnModificarLibro.grid(column =1, row =1, padx = 5, pady =1)

        self.btnBajaLibro = ttk.Button(self.lblFrameComandos, text = "BAJA", command = self.eliminarLibro)
        self.btnBajaLibro.grid(column =1, row =2, padx = 5, pady =1)



        # se crea el label frame de datos
        self.lblFrameDatos = ttk.Labelframe(self.frmLibro, text = "Datos: ")
        self.lblFrameDatos.grid(column =0, row =1, padx = 5, pady =5, sticky="n")

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
        self.txtTitulo = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoTitulo, state= "normal")
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

        
        
        self.cmbxTraduccion = ttk.Combobox(self.lblFrameDatos, width = 37, state= "readonly")
        self.cmbxTraduccion.grid(column =1, row =6, padx = 5, pady =5)
        self.cmbxTraduccion["values"] = ["SI", "NO"]
        self.datoTraduccion = self.cmbxTraduccion.get()
        self.indexCmbxTraduccion = self.cmbxTraduccion.current() # se obtiene el valor de índice 


        self.datoPaginas = tk.StringVar()
        self.txtPaginas = ttk.Entry(self.lblFrameDatos, width = 40, textvariable = self.datoPaginas, state="normal")
        self.txtPaginas.grid(column =1, row =7, padx = 5, pady =5)

        self.cmbxEstado = ttk.Combobox(self.lblFrameDatos, width = 37, state= "readonly")
        self.cmbxEstado.grid(column =1, row =8, padx = 5, pady =5)
        self.cmbxEstado["values"] = ["Prestado", "Disponible", "Retraso", "Restauración"]
        self.datoEstado = self.cmbxEstado.get()
        self.indexCmbxEstado = self.cmbxEstado.current() # se obtiene el valor de índice
        self.cmbxEstado.set("Disponible")

        # se crea el label frame de botones
        self.lblFrameAcciones = ttk.Labelframe(self.frmLibro, text = "Acciones: ")
        self.lblFrameAcciones.grid(column =0, row =3, padx = 5, pady =5)

        

        self.btnVolverPrincipalLibro = ttk.Button(self.lblFrameAcciones, text = "VOLVER A PRINCIPAL", command = self.volverPrincipal)#, command = self.buscarTit)
        self.btnVolverPrincipalLibro.grid(column =0, row =0, padx = 10, pady =5)

        self.btnLimpiarLibro = ttk.Button(self.lblFrameAcciones, text = "LIMPIAR", command = self.limpiar)
        self.btnLimpiarLibro.grid(column =1, row =0, padx = 10, pady =5)

    '''-------------------------------------------MANEJO DE WIDGETS--------------------------------------------------'''

    def limpiarCampos(self):
        self.datoID.set("")
        self.datoTitulo.set("")
        self.datoAutor.set("")
        self.datoEdicion.set("")
        self.datoLugarImpresion.set("")
        self.datoEditorial.set("")
        self.cmbxTraduccion.set("")
        self.datoPaginas.set("")
        self.cmbxEstado.set("")
    
    def limpiar(self):
        resp = mb.askyesnocancel("Limpiar", "¿Desea limpiar los campos? \n Se borrarán todos los campos y los cambios no se guardaran.")
        #print(resp)
        if resp == True:
            self.limpiarCampos()
            self.bloquearBotones()
            

    def habilitarCampos(self):
        self.txtTitulo.configure(state="normal")
        self.txtAutor.configure(state="normal")
        self.txtEdicion.configure(state="normal")
        self.txtLugarImpresion.configure(state="normal")
        self.txtEditorial.configure(state="normal")
        self.cmbxTraduccion.configure(state="readonly")
        self.txtPaginas.configure(state="normal")
        self.cmbxEstado.configure(state="readonly")
    
    def bloquearBotones(self):
        self.btnAltaLibro.configure(state="normal")
        self.btnModificarLibro.configure(state="disabled")
        self.btnBajaLibro.configure(state="disabled")

    def desbloquearBotones(self):
        self.btnAltaLibro.configure(state="disabled")
        self.btnModificarLibro.configure(state="normal")
        self.btnBajaLibro.configure(state="normal")
    
    def volverPrincipal(self):
        self.limpiarCampos()
        self.bloquearBotones()
        self.frmLibro.destroy()
        #import Principal as p 
        p.Principal()
    
    '''----------------------------------INTERACCION CON BASE DE DATOS-----------------------------------------------'''

    def buscarTit(self): 
        try:
            datoTitulo = (self.txtBuscarLibro.get())
            #print("Dato Tit: ", datoTitulo)
            resp = self.con.buscarTitulo(datoTitulo)
            #print("res: ", resp)
            if len(resp) > 1:
                mb.showwarning("¡ATENCIÓN!", "Puede haber más de un registro buscado, se tomará el primero.")
            
            self.habilitarCampos()

            if len(resp) > 0:
                self.desbloquearBotones()

                self.datoID.set(resp[0][0])
                self.datoTitulo.set(resp[0][1])
                self.datoAutor.set(resp[0][2])
                self.datoEdicion.set(resp[0][3])
                self.datoLugarImpresion.set(resp[0][4])
                self.datoEditorial.set(resp[0][5])
                self.cmbxTraduccion.set(resp[0][6])
                self.datoPaginas.set(resp[0][7])
                self.cmbxEstado.set(resp[0][8])
            else:
                mb.showinfo("INFORMACIÓN", f"No existen datos que contengan: {datoTitulo}.")
        except:
            mb.showerror("¡Error!", "Se ha encontrado un error al buscar.")
    
    # nuevo
    def nuevoLibro(self):
        try:

            datoN = (self.txtTitulo.get(), self.txtAutor.get(), self.txtEdicion.get(), self.txtLugarImpresion.get(), self.txtEditorial.get(), self.cmbxTraduccion.get(), self.txtPaginas.get(), self.cmbxEstado.get())
            #Titulo, Autor, Edicion, LugarImpresion, Editorial, Traduccion, Paginas, Estado
            #print(dato)
            self.con.nuevoLibro(datoN)
            mb.showinfo("INFORMACIÓN", "Datos guardados con éxito")
            
            self.limpiarCampos()
            self.bloquearBotones()

        
            self.txtTitulo.focus()
            #self.frmLibro.destroy()
        except:
            mb.showwarning("¡ATENCIÓN!", "Los datos no se guardaron correctamente.")


    # modificar
    def modificarLibro(self):
        try:
            if self.datoID == "":
                mb.showwarning("¡ATENCIÓN!", "El libro no existe o bien, no se ha buscado ninguno.")
            else:
                datoM = (self.txtTitulo.get(), self.txtAutor.get(), self.txtEdicion.get(), self.txtLugarImpresion.get(), self.txtEditorial.get(), self.cmbxTraduccion.get(), self.txtPaginas.get(), self.cmbxEstado.get(), self.txtIDLibro.get())
                self.con.modificarLibro(datoM)
                mb.showinfo("INFORMACIÓN", "El Libro fue modificado con éxito." )
                self.limpiarCampos()
                self.bloquearBotones()
        except:
            mb.showinfo("ATENCIÓN", "El Libro no fue modificado." )
        
    # eliminar libro
    def eliminarLibro(self):
        try:
            datoE = (self.txtIDLibro.get(), )
            if datoE == "":
                mb.showwarning("¡ATENCIÓN!", "El libro no existe o bien, no se ha buscado ninguno.")
            else:
                r = mb.askokcancel("¡ATENCIÓN!", "Está por eliminar definitivamente el registro.")
                if r == True:
                    self.con.eliminarLibro(datoE)
                    self.limpiarCampos()
        except:
            mb.showinfo("ATENCIÓN", "El Libro no fue Eliminado." )



