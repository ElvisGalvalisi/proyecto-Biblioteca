# PRINCIPAL
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox as mb
import sys
import os
import frmAcceso as acc
import frmAfiliados as afil
import frmPrestamo as pres




class Principal:
    def __init__(self):
        
        self.ventanaPrincipal= tk.Tk()
        self.ventanaPrincipal.title("Administración de Biblioteca")

        self.ventanaPrincipal.geometry("1366x768") # se define la pantalla a un tamaño default
        self.ventanaPrincipal.resizable(0,0) # se impide achicar la pantalla

        # visualizamos el Menu
        self.menu() 
        # se muestran funciones en pantalla
        self.funciones()

        #contol de evento para cierre de ventana.
        self.ventanaPrincipal.protocol("WM_DELETE_WINDOW", self.salir)

        # se muestra la ventana
        self.ventanaPrincipal.mainloop()
            
        #else:
        #mb.showerror("ERROR","Ha ocurrido un error al abrir la pantalla principal.")
    

    def menu(self):
        mnu = tk.Menu(self.ventanaPrincipal) # se crea el menú
        self.ventanaPrincipal.config(menu = mnu) # se agrega el menú a la ventana
        opciones = tk.Menu(mnu, tearoff = 0) # creamos las opciones del menú
        opciones.add_command(label = "Préstamos", command = self.abrirPrestamos) #falta agregar command:
        opciones.add_separator() # se crea un separador en forma de línea. 
        opciones.add_command(label = "Salir", command = self.salir) 
        mnu.add_cascade(label = "Archivo", menu = opciones) # se agregan las opciones al menú.

        opciones2 = tk.Menu(mnu, tearoff = 0)
        opciones2.add_command(label = "Libros", command = self.abrirLibros)
        opciones2.add_command(label = "Afiliados", command = self.abrirAfiliados)
        mnu.add_cascade(label = "Herramientas", menu = opciones2)
    
    def funciones(self):
        #label Frame
        self.lblFramePrestamo = ttk.Labelframe(self.ventanaPrincipal, text = "Alquiler")
        self.lblFramePrestamo.grid(column =0, row =0, padx = 5, pady = 0)

        self.lblFrameGestores = ttk.Labelframe(self.ventanaPrincipal, text = "Gestores")
        self.lblFrameGestores.grid(column =1, row =0, padx = 5, pady = 5)

        # buttons
        btnPrestamo = ttk.Button(self.lblFramePrestamo, text = "PRÉSTAMO", command = self.abrirPrestamos)
        btnPrestamo.grid(column =0, row =0, padx = 5, pady = 5)

        btnLibros = ttk.Button(self.lblFrameGestores, text = "LIBROS", command = self.abrirLibros)
        btnLibros.grid(column =0, row =0, padx = 5, pady = 5)

        btnAfiliado = ttk.Button(self.lblFrameGestores, text = "AFILIADOS", command = self.abrirAfiliados)
        btnAfiliado.grid(column =0, row =1, padx = 5, pady = 5)
        
        
    
    
    def salir(self):
        resp = mb.askyesno("ATENCIÓN", "¿Realmente desea Salir?")

        if resp == True:
            sys.exit()

    
    def abrirLibros(self):
        # se cierra la ventana principal
        self.ventanaPrincipal.destroy()
        # se importa el modulo del formulario de libros
        import frmLibros as lib
        # se abre el formulario.
        lib.Libro()

    def abrirAfiliados(self):
        # se cierra la ventana principal
        self.ventanaPrincipal.destroy()
        
        # se abre el formulario.
        afil.Afiliado()
    
    def abrirPrestamos(self):
        # se cierra la ventana principal
        self.ventanaPrincipal.destroy()
        
        # se abre el formulario.
        pres.Prestamo()
        