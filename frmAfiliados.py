import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import ConexionDB
import Principal as p

class Afiliado:
    def __init__(self):
        # se crea la conexión
        self.con = ConexionDB.Conectarse()
        self.con.conectar()

        self.frmAfiliado = tk.Tk()
        self.frmAfiliado.title("Gestor de Afiliados")
        self.frmAfiliado.geometry("420x380")
        self.frmAfiliado.resizable(0,0)
        #self.frmAfiliado.configure(background = "#BBD1F0")

        

        # mostramos las pestañas
        self.graficosAfiliados()
        
        self.habilitarCampos()
        self.bloquearBotones()

        
        self.frmAfiliado.protocol("WM_DELETE_WINDOW", self.cerrarVentana)

        self.frmAfiliado.mainloop()
    


    '''-----------------------------WIDGETS-----------------------------------------------------------'''

    def graficosAfiliados(self):
        # se crea el label frame de buscar afiliado
        self.lblFrameBuscarAfiliado = ttk.Labelframe(self.frmAfiliado, text = "Ingresar nombre del Afiliado: ")
        self.lblFrameBuscarAfiliado.grid(column =0, row =0, padx = 5, pady =5)

        # label buscar
        self.datoBuscarAfiliado = tk.StringVar()
        self.txtBuscarAfiliado = ttk.Entry(self.lblFrameBuscarAfiliado, width = 30, textvariable = self.datoBuscarAfiliado)
        self.txtBuscarAfiliado.grid(column =0, row =0, padx = 5, pady =5, sticky="e")

        #button Buscar
        self.btnBuscarAfiliado = ttk.Button(self.lblFrameBuscarAfiliado, text = "BUSCAR", command = self.buscarAfil)
        self.btnBuscarAfiliado.grid(column =1, row =0, padx = 5, pady =5)

        # label frame Datos

        self.lblFrameDatosAfiliado = ttk.Labelframe(self.frmAfiliado, text = "Datos Afiliados: ")
        self.lblFrameDatosAfiliado.grid(column =0, row =1, padx = 5, pady =5)
        
        # label
        self.lblIDAfiliado = ttk.Label(self.lblFrameDatosAfiliado, text = "ID: ")
        self.lblIDAfiliado.grid(column =0, row =0, padx = 5, pady =5, sticky="w")

        self.lblNombreAfiliado = ttk.Label(self.lblFrameDatosAfiliado, text = "Nombre: ")
        self.lblNombreAfiliado.grid(column =0, row =1, padx = 5, pady =5, sticky="w")

        self.lblApellidoAfiliado = ttk.Label(self.lblFrameDatosAfiliado, text = "Apellido: ")
        self.lblApellidoAfiliado.grid(column =0, row =2, padx = 5, pady =5, sticky="w")

        self.lblTelefonoAfiliado = ttk.Label(self.lblFrameDatosAfiliado, text = "Telefono: ")
        self.lblTelefonoAfiliado.grid(column =0, row =3, padx = 5, pady =5, sticky="w")

        self.lblMailAfiliado = ttk.Label(self.lblFrameDatosAfiliado, text = "Mail: ")
        self.lblMailAfiliado.grid(column =0, row =4, padx = 5, pady =5, sticky="w")

        self.lblActivoAfiliado = ttk.Label(self.lblFrameDatosAfiliado, text = "Activo: ")
        self.lblActivoAfiliado.grid(column =0, row =5, padx = 5, pady =5, sticky="w")

        #ID, Nombre, Apellido, Telefono, Mail, Activo (combobox)
        
        # entry
        self.datoIDAfiliado = tk.StringVar()
        self.txtIDAfiliado = ttk.Entry(self.lblFrameDatosAfiliado, width = 30, textvariable = self.datoIDAfiliado, state ="disabled")
        self.txtIDAfiliado.grid(column =1, row = 0, padx = 5, pady = 5)

        self.datoNombreAfiliado = tk.StringVar()
        self.txtNombreAfiliado = ttk.Entry(self.lblFrameDatosAfiliado, width = 30, textvariable = self.datoNombreAfiliado, state="normal")
        self.txtNombreAfiliado.grid(column =1, row = 1, padx = 5, pady = 5)

        self.datoApellidoAfiliado = tk.StringVar()
        self.txtApellidoAfiliado = ttk.Entry(self.lblFrameDatosAfiliado, width = 30, textvariable = self.datoApellidoAfiliado, state="normal")
        self.txtApellidoAfiliado.grid(column =1, row = 2, padx = 5, pady = 5)

        self.datoTelefonoAfiliado = tk.StringVar()
        self.txtTelefonoAfiliado = ttk.Entry(self.lblFrameDatosAfiliado, width = 30, textvariable = self.datoTelefonoAfiliado, state="normal")
        self.txtTelefonoAfiliado.grid(column =1, row = 3, padx = 5, pady = 5)

        self.datoMailAfiliado = tk.StringVar()
        self.txtMailAfiliado = ttk.Entry(self.lblFrameDatosAfiliado, width = 30, textvariable = self.datoMailAfiliado, state="normal")
        self.txtMailAfiliado.grid(column =1, row = 4, padx = 5, pady = 5)

        self.cmbxActivoAfiliado = ttk.Combobox(self.lblFrameDatosAfiliado, width = 28, state="readonly")
        self.cmbxActivoAfiliado.grid(column =1, row = 5, padx = 5, pady =5)
        self.cmbxActivoAfiliado["values"] = ["SI", "NO"]
        self.datoActivoAfiliado = self.cmbxActivoAfiliado.get()
        self.indexcmbxActivoAfiliado = self.cmbxActivoAfiliado.current() # se obtiene el valor de índice
        self.cmbxActivoAfiliado.set("SI")

        self.lblFrameCRUDAfiliado = ttk.Labelframe(self.frmAfiliado, text = "GUARDAR: ")
        self.lblFrameCRUDAfiliado.grid(column =1, row =1, padx = 5, pady =5)

         #botones de CRUD
        self.btnNuevofiliado= ttk.Button(self.lblFrameCRUDAfiliado, text="NUEVO", command = self.altaAfiliado)
        self.btnNuevofiliado.grid(column=0, row=0, padx=2, pady=0)

        self.btnModificarAfiliado= ttk.Button(self.lblFrameCRUDAfiliado, text="MODIFICAR", command = self.modificarAfiliado)
        self.btnModificarAfiliado.grid(column=0, row=1, padx=2, pady=0)
        
        self.btnEliminarAfiliado= ttk.Button(self.lblFrameCRUDAfiliado, text="ELIMINAR", command = self.eliminarAfiliado)
        self.btnEliminarAfiliado.grid(column=0, row=2, padx=2, pady=0)
        

        # buttons volver salir
        self.lblFrameAcciones = ttk.Labelframe(self.frmAfiliado, text="Acciones: ")
        self.lblFrameAcciones.grid(column =0, row =3, padx = 5, pady =5)

        self.btnVolverPrincipal=ttk.Button(self.lblFrameAcciones, text="VOLVER A PRINCIPAL", command = self.volverPrincipal)
        self.btnVolverPrincipal.grid(column=0, row=0, padx=2, pady=0)

        self.btnLimpiarAfiliado=ttk.Button(self.lblFrameAcciones, text="LIMPIAR", command = self.limpiar)
        self.btnLimpiarAfiliado.grid(column=1, row=0, padx=2, pady=0)

       


    '''---------------------------------MANEJO DE WIDGETS--------------------------------------------------------'''

    def cerrarVentana(self):
        resp = mb.askokcancel("¡ATENCIÓN!", "Al cerrar el formulario volverá a la pantalla principal.")
        if resp == True:
            self.frmAfiliado.destroy()
            #import Principal as p
            p.Principal()

    def limpiarCamposAfiliado(self):
        self.datoIDAfiliado.set("")
        self.datoNombreAfiliado.set("")
        self.datoApellidoAfiliado.set("")
        self.datoTelefonoAfiliado.set("")
        self.datoMailAfiliado.set("")
        self.cmbxActivoAfiliado.set("")

    def habilitarCampos(self):
        self.txtIDAfiliado.configure(state="disabled")
        self.txtNombreAfiliado.configure(state="normal")
        self.txtApellidoAfiliado.configure(state="normal")
        self.txtTelefonoAfiliado.configure(state="normal")
        self.txtMailAfiliado.configure(state="normal")
        self.cmbxActivoAfiliado.configure(state="readonly")
    
    def bloquearBotones(self):
        self.btnBuscarAfiliado.configure(state="normal")
        self.btnNuevofiliado.configure(state="normal")
        self.btnModificarAfiliado.configure(state="disabled")
        self.btnEliminarAfiliado.configure(state="disabled")

    def desbloquearBotones(self):
        self.btnBuscarAfiliado.configure(state="normal")
        self.btnNuevofiliado.configure(state="disabled")
        self.btnModificarAfiliado.configure(state="normal")
        self.btnEliminarAfiliado.configure(state="normal")
    
    def limpiar(self):
        respA = mb.askyesnocancel("Limpiar", "¿Desea limpiar los campos? \n Se borrarán todos los campos y los cambios no se guardaran.")
        #print(resp)
        if respA == True:
            self.limpiarCamposAfiliado()
            self.bloquearBotones()

    def volverPrincipal(self):
        self.limpiarCamposAfiliado()
        self.bloquearBotones()
        self.frmAfiliado.destroy()
        p.Principal()

    '''--------------------INTERACCION CON BASE DE DATOS-----------------------------------------------------------'''

    def buscarAfil(self): 
        try:
            nomAfiliado = (self.txtBuscarAfiliado.get())
            #print("NomAfiliado: ", nomAfiliado)
            respA = self.con.buscarAfiliado(nomAfiliado)
            #print("res: ", respA)
            if len(respA) > 1:
                mb.showwarning("¡ATENCIÓN!", "Puede haber más de un registro buscado, se tomará el primero.")
            
            self.habilitarCampos()

            if len(respA) > 0:
                self.desbloquearBotones()

                self.datoIDAfiliado.set(respA[0][0])
                self.datoNombreAfiliado.set(respA[0][1])
                self.datoApellidoAfiliado.set(respA[0][2])
                self.datoTelefonoAfiliado.set(respA[0][3])
                self.datoMailAfiliado.set(respA[0][4])
                self.cmbxActivoAfiliado.set(respA[0][5])
                
            else:
                mb.showinfo("INFORMACIÓN", f"No existen datos que contengan: {nomAfiliado}.")
        except:
            mb.showerror("¡Error!", "Se ha encontrado un error al buscar el nombre del afiliado.")
    # nuevo
    def altaAfiliado(self):
        try:

            nuevoAfil = (self.txtNombreAfiliado.get(), self.txtApellidoAfiliado.get(), self.txtTelefonoAfiliado.get(), self.txtMailAfiliado.get(), self.cmbxActivoAfiliado.get())
            
            #print(nuevoAfil)
            self.con.nuevoAfiliado(nuevoAfil)
            mb.showinfo("INFORMACIÓN", "Datos guardados con éxito")
            
            self.limpiarCamposAfiliado()
            self.bloquearBotones()

        
            self.txtNombreAfiliado.focus()
            
        except:
            mb.showwarning("¡ATENCIÓN!", "Los datos no se guardaron correctamente.")

    # modificar
    def modificarAfiliado(self):
        try:
            # buscamos este campo que es vital para la consulta a la base de datos.
            if self.datoIDAfiliado == "":
                mb.showwarning("¡ATENCIÓN!", "El Afiliado no existe o bien, no se ha buscado ninguno.")
            else:
                datoAfilM = (self.txtNombreAfiliado.get(), self.txtApellidoAfiliado.get(), self.txtTelefonoAfiliado.get(), self.txtMailAfiliado.get(), self.cmbxActivoAfiliado.get(), self.txtIDAfiliado.get())
                self.con.modificarAfiliado(datoAfilM)
                mb.showinfo("INFORMACIÓN", "El Afiliado fue modificado con éxito." )
                self.limpiarCamposAfiliado()
                self.bloquearBotones()
        except:
            mb.showinfo("ATENCIÓN", "El Afiliado no fue modificado." )  
    
    # eliminar Afiliado
    def eliminarAfiliado(self):
        try:
            datoAfilE = (self.txtIDAfiliado.get(), )
            if datoAfilE == "":
                mb.showwarning("¡ATENCIÓN!", "El Afiliado no existe o bien, no se ha buscado ninguno.")
            else:
                r = mb.askokcancel("¡ATENCIÓN!", "Está por eliminar definitivamente el registro.")
                if r == True:
                    self.con.eliminarAfiliado(datoAfilE)
                    self.limpiarCamposAfiliado()
        except:
            mb.showinfo("ATENCIÓN", "El Afiliado no fue Eliminado." )

