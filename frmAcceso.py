# interfaz de acceso

import tkinter as tk
import sys
import os
from tkinter import ttk
from tkinter import messagebox as mb
import ConexionDB
import Principal as p


class frmAcceso:
    def __init__(self):
        
        self.cnn = ConexionDB.Conectarse()

        #ventana principal
        self.ventanaAcceso = tk.Tk()
        self.ventanaAcceso.title("Bienvenido")
        self.ventanaAcceso.geometry("290x140")
        self.ventanaAcceso.resizable(0,0)
        #mostramos la interfaz
        self.graficos()

        self.txtUsuario.focus()
        self.ventanaAcceso.mainloop()
    
    
    def graficos(self):
        #label frame
        self.lblFrameAcceso = ttk.LabelFrame(self.ventanaAcceso, text = "Acceso")
        self.lblFrameAcceso.grid(column =0, row=0, padx = 10, pady=2)

        # label
        self.lblUsuario = ttk.Label(self.lblFrameAcceso, text = "Usuario: ")
        self.lblUsuario.grid(column =0, row=0, padx = 2, pady=2, sticky="e")

        self.lblContrasenia = ttk.Label(self.lblFrameAcceso, text = "Contraseña: ")
        self.lblContrasenia.grid(column =0, row=1, padx = 2, pady=2, sticky="e")

        # entry
        self.datoUser = tk.StringVar()
        self.txtUsuario = ttk.Entry(self.lblFrameAcceso, width = 30, textvariable = self.datoUser)
        self.txtUsuario.grid(column =1, row=0, padx = 2, pady=2)

        self.datoPwd = tk.StringVar()
        self.txtContrasenia = ttk.Entry(self.lblFrameAcceso, width = 30, textvariable = self.datoPwd, show="*")
        self.txtContrasenia.grid(column =1, row=1, padx = 2, pady=2)

        #labelFrame Operacion
        self.lblFrameBotonEntrar = ttk.LabelFrame(self.ventanaAcceso)
        self.lblFrameBotonEntrar.grid(column =0, row=1, padx = 2, pady=2)

        #button
        self.btnEntrar = ttk.Button(self.lblFrameBotonEntrar, text = "ENTRAR", command = self.ingresar) # falta el command
        self.btnEntrar.grid(column = 0, row = 0, padx = 5, pady= 5)

        self.btnSalir = ttk.Button(self.lblFrameBotonEntrar, text = "SALIR", command = self.salir)
        self.btnSalir.grid(column = 1, row = 0, padx = 5, pady= 5)
    
    def salir(self):
        resp = mb.askyesno("ATENCIÓN", "¿Realmente desea Salir?")
        #print(resp)
        if resp == True:
            sys.exit()
        else:
            mb.showerror("ERROR", "Ups! Ha ocurrido un error al salir")


    #función conectarse a BD y entrar
    def ingresar(self):
        usuario = self.datoUser.get()
        contrasena = self.datoPwd.get()
        self.conec = self.cnn.accesoUsuarios(usuario, contrasena)
        #print("conec: ", self.conec)
        if self.conec == True:
            # se cierra la ventana de acceso
            self.ventanaAcceso.destroy()
            # se abre la pantalla principal
            p.Principal()






