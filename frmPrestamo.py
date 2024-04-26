import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as sc
import ConexionDB
import Principal as p
import sqlite3
from datetime import datetime
from datetime import timedelta


class Prestamo:
    def __init__(self):
        # se crea la conexión
        self.con = ConexionDB.Conectarse()
        self.con.conectar()

        self.frmPrestamo = tk.Tk()
        self.frmPrestamo.title("Gestor de Prestamos")
        self.frmPrestamo.geometry("420x400")
        self.frmPrestamo.resizable(0,0)
        
        self.panel = ttk.Notebook(self.frmPrestamo)
        self.panel.grid(column =0, row =0, padx = 5, pady =5)
        

        # mostramos las pestañas
        
        self.pestanaPrestamo()
        self.pestanaConsulta()
        
        self.aplicarNroPrestamo()

        self.aplicarDatoFecha()
        


        
        self.frmPrestamo.protocol("WM_DELETE_WINDOW", self.cerrarVentana)

        self.frmPrestamo.mainloop()
    

    '''-----------------------------WIDGETS-----------------------------------------------------------'''

    def pestanaPrestamo(self):
        self.framePrestamo = ttk.Frame(self.panel)
        self.panel.add(self.framePrestamo, text = "PRÉSTAMO")
        self.graficosPrestamo()

    def pestanaConsulta(self):
        self.frameConsulta = ttk.Frame(self.panel)
        self.panel.add(self.frameConsulta, text = "CONSULTA")
        self.graficosConsulta()


    def graficosPrestamo(self):
        #label frame
        self.lblFramePrestamo = ttk.Labelframe(self.framePrestamo, text = "DATOS: ")
        self.lblFramePrestamo.grid(column =0, row=0, padx=5, pady=5)

        #id, numeroPrestamo, FechaPrestamo, fechaDevolucion, IDLibro, IDAFiliado

        #label
        self.lblIDPrestamo = ttk.Label(self.lblFramePrestamo, text = "ID: ")
        self.lblIDPrestamo.grid(column =0, row=0, padx=5, pady=5)

        self.lblNumeroPrestamo = ttk.Label(self.lblFramePrestamo, text = "Número Préstamo: ")
        self.lblNumeroPrestamo.grid(column =0, row=1, padx=5, pady=5)

        self.lblIDLibro = ttk.Label(self.lblFramePrestamo, text = "ID Libro: ")
        self.lblIDLibro.grid(column =0, row=2, padx=5, pady=5)

        self.lblNombreLibro = ttk.Label(self.lblFramePrestamo, text = "Nombre Libro: ")
        self.lblNombreLibro.grid(column =0, row=3, padx=5, pady=5)

        self.lblIDAfiliado = ttk.Label(self.lblFramePrestamo, text = "ID Afiliado: ")
        self.lblIDAfiliado.grid(column =0, row=4, padx=5, pady=5)

        self.lblNombreAfiliado = ttk.Label(self.lblFramePrestamo, text = "Nombre Afiliado: ")
        self.lblNombreAfiliado.grid(column =0, row=5, padx=5, pady=5)

        self.lblFechaPrestamo = ttk.Label(self.lblFramePrestamo, text = "Fecha Préstamo: ")
        self.lblFechaPrestamo.grid(column =0, row=6, padx=5, pady=5)

        self.lblFechaDevolucion = ttk.Label(self.lblFramePrestamo, text = "Fecha Devolución: ")
        self.lblFechaDevolucion.grid(column =0, row=7, padx=5, pady=5)

        #entry 
        self.datoIDPrestamo=tk.StringVar()
        self.txtIDPrestamo = ttk.Entry(self.lblFramePrestamo, width= 30, textvariable=self.datoIDPrestamo, state="disabled")
        self.txtIDPrestamo.grid(column =1, row=0, padx=5, pady=5)

        self.datoNumeroPrestamo=tk.StringVar()
        self.txtNumeroPrestamo = ttk.Entry(self.lblFramePrestamo, width= 30, textvariable=self.datoNumeroPrestamo, state="disabled")
        self.txtNumeroPrestamo.grid(column =1, row=1, padx=5, pady=5)

        
        self.cmbxIDLibroP = ttk.Combobox(self.lblFramePrestamo, width= 27, state="readonly")
        self.cmbxIDLibroP['values'] = self.con.buscarIDLibro() # se llena el combobox con datos de la DB
        self.cmbxIDLibroP.grid(column =1, row=2, padx=5, pady=5)
        self.cmbxIDLibroP.current()
        self.cmbxIDLibroP.bind('<<ComboboxSelected>>', self.llenarCampoLibros)

        self.datoNombreLibroP=tk.StringVar()
        self.txtNombreLibroP = ttk.Entry(self.lblFramePrestamo, width= 30, textvariable=self.datoNombreLibroP, state="disabled")
        self.txtNombreLibroP.grid(column =1, row=3, padx=5, pady=5)

        self.cmbxIDAfiliadoP=tk.StringVar()
        self.cmbxIDAfiliadoP= ttk.Combobox(self.lblFramePrestamo, width= 27, state="readonly")
        self.cmbxIDAfiliadoP['values'] = self.con.buscarIDAfiliado()# se llena el combobox con datos de la DB
        self.cmbxIDAfiliadoP.grid(column =1, row=4, padx=5, pady=5)
        self.cmbxIDAfiliadoP.current()
        self.cmbxIDAfiliadoP.bind('<<ComboboxSelected>>', self.llenarCampoAfiliado)

        self.datoNombreAfiliadoP=tk.StringVar()
        self.txtNombreAfiliadoP = ttk.Entry(self.lblFramePrestamo, width= 30, textvariable=self.datoNombreAfiliadoP, state="disabled")
        self.txtNombreAfiliadoP.grid(column =1, row=5, padx=5, pady=5)

        self.datoFechaPrestamo=tk.StringVar()
        self.txtFechaPrestamo = ttk.Entry(self.lblFramePrestamo, width= 30, textvariable=self.datoFechaPrestamo)
        self.txtFechaPrestamo.grid(column =1, row=6, padx=5, pady=5)

        self.datoFechaDevolucion=tk.StringVar()
        self.txtFechaDevolucion = ttk.Entry(self.lblFramePrestamo, width= 30, textvariable=self.datoFechaDevolucion)
        self.txtFechaDevolucion.grid(column =1, row=7, padx=5, pady=5)

        #label frame
        self.lblFrameAccionesPrestamo = ttk.Labelframe(self.framePrestamo, text= "PRÉSTAMO")
        self.lblFrameAccionesPrestamo.grid(column =0, row=1, padx=5, pady=5)

        self.btnGenerar = ttk.Button(self.lblFrameAccionesPrestamo, text= "GENERAR", command = self.generarPrestamo)
        self.btnGenerar.grid(column =0, row=1, padx=5, pady=5)

        self.btnFinalizar = ttk.Button(self.lblFrameAccionesPrestamo, text= "FINALIZAR", command = self.finalizarPrestamo)
        self.btnFinalizar.grid(column =1, row=1, padx=5, pady=5)

        self.btnSalir = ttk.Button(self.lblFrameAccionesPrestamo, text= "SALIR", command = self.cancelarPrestamo)
        self.btnSalir.grid(column =2, row=1, padx=5, pady=5)

        #buscar prestamo
        self.datoBuscar = tk.StringVar()
        self.txtBuscarPrestamo = ttk.Entry(self.lblFrameAccionesPrestamo, width=20, textvariable=self.datoBuscar)
        self.txtBuscarPrestamo.grid(column =0, row=0, padx=5, pady=5)

        self.btnBuscarPrestamo=ttk.Button(self.lblFrameAccionesPrestamo, text="BUSCAR PRESTAMO", command = self.insertarPrestamo) 
        self.btnBuscarPrestamo.grid(column =1, row=0, padx=5, pady=5)

        


    def graficosConsulta(self):
        # se crea el label frame de buscar
        self.lblFrameBuscarP = ttk.Labelframe(self.frameConsulta, text = "Ingresar nombre del título: ")
        self.lblFrameBuscarP.grid(column =0, row =0, padx = 5, pady =5)

        self.lblFrameVisor = ttk.Labelframe(self.frameConsulta, text = "Datos de Libros ")
        self.lblFrameVisor.grid(column =0, row =1, padx = 5, pady =5)

        # label buscar
        self.datoBuscarLibroP = tk.StringVar()
        self.txtBuscarLibroP = ttk.Entry(self.lblFrameBuscarP, width = 30, textvariable = self.datoBuscarLibroP)
        self.txtBuscarLibroP.grid(column =0, row =0, padx = 5, pady =5, sticky="e")

        #button Buscar
        self.btnBuscarLibroP = ttk.Button(self.lblFrameBuscarP, text = "BUSCAR", command = self.BuscarLibroConsulta)
        self.btnBuscarLibroP.grid(column =1, row =0, padx = 5, pady =5)

        #button Buscar
        self.btnVerTodos = ttk.Button(self.lblFrameBuscarP, text = "VER TODOS", command = self.listarLibros)
        self.btnVerTodos.grid(column =2, row =0, padx = 5, pady =5)

        self.scrLibros = sc.ScrolledText(self.lblFrameVisor, width= 47, height= 15)
        self.scrLibros.grid(column = 0, row = 0, padx=5, pady=5)




    '''---------------------------------MANEJO DE WIDGETS--------------------------------------------------------'''

    def cerrarVentana(self):
        resp = mb.askokcancel("¡ATENCIÓN!", "Al cerrar el formulario volverá a la pantalla principal.")
        if resp == True:
            self.frmPrestamo.destroy()
            #import Principal as p
            p.Principal()

    def aplicarDatoFecha(self):
    
        hoy = datetime.now() # se guarda la fecha de hoy
        hoyFormateado = hoy.strftime('%d/%m/%Y')
        #print("Hoy: ",hoyFormateado)
        self.datoFechaPrestamo.set(hoyFormateado)

        fechaDevolucion = hoy + timedelta(days=15) # se suman 15 días
        fechaDevolucionFormateada = fechaDevolucion.strftime('%d/%m/%Y')
        #print("Devolución: ", fechaDevolucionFormateada)

        self.datoFechaDevolucion.set(fechaDevolucionFormateada)
    
    def aplicarNroPrestamo(self):
        n = 0
        nroObetenido = self.con.buscarNroPrestamo(n)
        self.datoIDPrestamo.set(nroObetenido)
        self.datoNumeroPrestamo.set(nroObetenido)


    def llenarCampoLibros(self, tituloLibro):
        try:
            buscarIDLibro= self.cmbxIDLibroP.get()
            tituloLibro = self.con.buscarNombreLibro(buscarIDLibro)
            #print(tituloLibro[0])
            self.datoNombreLibroP.set(str(tituloLibro[0]))
        except sqlite3.OperationalError:
            mb.showerror("¡Error!", "Se ha producido un error al buscar el libro.")
    
    def llenarCampoAfiliado(self, nombreAfiliado):
        try:
            buscarIDAfiliado= self.cmbxIDAfiliadoP.get()
            nombreAfiliado = self.con.buscarNombreAfiliado(buscarIDAfiliado)
            #print(nombreAfiliado[0])
            self.datoNombreAfiliadoP.set(str(nombreAfiliado[0]))
        except sqlite3.OperationalError:
            mb.showerror("¡Error!", "Se ha producido un error al buscar el Afiliado.")


    
    '''--------------------------------FUNCIONES Y GUARDADO EN BASE DE DATOS---------------------------------------'''

    def generarPrestamo(self):
        
        gen = (self.datoNumeroPrestamo.get(), self.datoFechaPrestamo.get(), self.datoFechaDevolucion.get(), self.cmbxIDLibroP.get(), self.cmbxIDAfiliadoP.get())
        self.con.nuevoPrestamo(gen)
        
        # agregar try
        mb.showinfo("INFORMACIÓN", 
        f"""-PRÉSTAMO GENERADO CON ÉXITO: \n 
        - Número Préstamo: {self.datoNumeroPrestamo.get()} \n
        - Libro: {self.datoNombreLibroP.get()} \n 
        - Afiliado: {self.datoNombreAfiliadoP.get()} \n 
        - Fecha Préstamo: {self.datoFechaPrestamo.get()}\n 
        - Fecha Devolución: {self.datoFechaDevolucion.get()}""")
        self.cambiarEstadoLibroGen()
        self.limpiarCampos()
 
    def insertarPrestamo(self):
        datoBuscadoPrestamo = (self.datoBuscar.get())
        resp = self.con.controlfinPrestamo(datoBuscadoPrestamo)
        if resp == "":
            mb.showwarning("ATENCIÓN", "No hay ningún préstamo registrado con el número elegido.")
        else:
            self.datoIDPrestamo.set(resp[0][0])
            self.datoNumeroPrestamo.set(resp[0][1])
            self.datoFechaPrestamo.set(resp[0][2])
            self.datoFechaDevolucion.set(resp[0][3])
            self.cmbxIDLibroP.set(resp[0][4])
            #self.datoNombreLibroP.set(resp[0][0])
            self.cmbxIDAfiliadoP.set(resp[0][5])
            #self.datoNombreAfiliadoP.set(resp[0][0]) 

        
    def finalizarPrestamo(self):
        nro = self.datoIDPrestamo.get()
        hoyFin = datetime.now()
        hoyFormat = hoyFin.strftime('%d/%m/%Y') # se guarda la fecha de hoy
        # se muestra el mensaje de prestamo finalizado
        mb.showinfo("INFORMACIÓN", 
        f"""- PRÉSTAMO FINALIZADO: \n 
        - Número Préstamo: {self.datoIDPrestamo.get()} \n
        - Codigo Libro: {self.cmbxIDLibroP.get()} \n 
        - Codigo Afiliado: {self.cmbxIDAfiliadoP.get()} \n 
        - Fecha Préstamo: {self.datoFechaPrestamo.get()}\n 
        - Fecha Devolución: {hoyFormat}""")
        try:
            self.con.guardarFechaFinalizacion(nro)
        except sqlite3.OperationalError:
            mb.showerror("ERROR", "Se ha producido un error al guardar fecha Finalización. ")
        except sqlite3.ProgrammingError:
            mb.showerror("ERROR", "No hay un valor definido para función.")
        self.cambiarEstadoLibroFin()
        self.limpiarCampos()


    def limpiarCampos(self):
        self.datoIDPrestamo.set("")
        self.datoNumeroPrestamo.set("")
        self.cmbxIDLibroP.set("")
        self.datoNombreLibroP.set("")
        self.cmbxIDAfiliadoP.set("")
        self.datoNombreAfiliadoP.set("")  
    
    def cancelarPrestamo(self):
        self.limpiarCampos()
        self.aplicarDatoFecha()
        self.cerrarVentana()
    
    def cambiarEstadoLibroGen(self):
        idL=self.cmbxIDLibroP.get()
        self.con.cambiarEstadoLibro(idL)
    
    def cambiarEstadoLibroFin(self):
        idL=self.cmbxIDLibroP.get()
        self.con.cambiarEstadoLibroFinalizado(idL)

    def listarLibros(self):
        # se limpian el scrolledText
        self.scrLibros.delete("0.0", tk.END)
        # se realiza la consulta a la DB
        lib = self.con.buscarLibrosTodos()
        # se agregan en el scrolledText los datos de la consulta.
        self.scrLibros.insert(tk.END, "ID      TÍTULO       AUTOR    ESTADO")
        self.scrLibros.insert(tk.END, "\n")
        # se recorre 
        for i in range (len(lib)):
            self.scrLibros.insert(tk.END, f"{lib[i][0]}- {lib[i][1]}-{lib[i][2]}-({lib[i][8]})")
            self.scrLibros.insert(tk.END, "\n")
        
    def BuscarLibroConsulta(self):
        # se limpian el scrolledText
        self.scrLibros.delete("0.0", tk.END)
        tituloConsulta = self.datoBuscarLibroP.get()
        # se realiza la consulta a la DB
        lib = self.con.buscarTitulo(tituloConsulta)
        # se agregan en el scrolledText los datos de la consulta.
        self.scrLibros.insert(tk.END, "ID      TÍTULO    AUTOR   ESTADO")
        self.scrLibros.insert(tk.END, "\n")

        for j in range(len(lib)):
            self.scrLibros.insert(tk.END, f"{lib[j][0]}- {lib[j][1]}-{lib[j][2]}-({lib[j][8]})")
            self.scrLibros.insert(tk.END, "\n")

