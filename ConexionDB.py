
import sqlite3
import os
from tkinter import messagebox as mb

# se crea la clase conexión
class Conectarse:
    def __init__(self):
        self.AccesoCon = False
        #self.conectar()
        #self.accesoUsuarios()
    
    def conectar(self):
        try:
            # se crea el objeto de la conexión
            con = sqlite3.connect("C:\DataBase\Biblioteca.db")
            # retorna conexión
            return con

            #print("Conexión Exitosa")
        except sqlite3.OperationalError:
            print("Error al conectar")

    def accesoUsuarios(self, usuario, contrasena):
        # se reciben por parámetro los datos cargados en los enty
        self.usr = usuario 
        self.pwd = contrasena
        # se intenta conectar y ejecutar la consulta a la base de datos.
        try:
            cc = self.conectar()
            cursor = cc.cursor()
            sql = "SELECT Usuario, Contrasena FROM tblUsuario"
            cursor.execute(sql)
            for linea in cursor.fetchall():
                #print(f"{linea[0]}  {linea[1]}")
                # se crea una bandera para validar datos recibidos de la base de datos y los cargados.
                banderaAcceso = False
                # la condición siempre es que se controlen los datos. 
                if banderaAcceso == False:
                    if linea[0] == self.usr:
                        if linea[1] == self.pwd:
                            # si se cumple esta condición es porque el usuario coincide con la DB. Se devuelve
                            # un mensaje de bienvenida.
                            #mb.showinfo("Acceso", f"Bienvenido {linea[0]}")
                            # se setea la variable de acceso para que se pueda abrir el formulario principal.
                            self.AccesoCon = True
                            #se devuelve el acceso
                            return self.AccesoCon

                            banderaAcceso = True
                        else:
                            banderaAcceso = False
            # se valida la bandera.
            if banderaAcceso == False:
                # en caso de no coincidir en todas las comparaciones, se devuelve un mensaje tipo warning.
                mb.showwarning("ATENCIÓN", "El Usuario y/o Contraseña son incorrectos")
            # se cierra la conexión de la DB.
            cursor.close()
             
        except sqlite3.OperationalError:
            mb.showerror("¡ATENCIÓN!", "Ha ocurrido un error al intentar ingresar")
    
    """----------------------------------Constultas a la tblLibro----------------------------------------------"""
    # buscar libro
    def buscarTitulo(self, datoBuscado):
        #se crea la conexión
        try:
            cc = self.conectar()
            cursor = cc.cursor()
            #print("Dato buscado: ", datoBuscado)
            sql = "SELECT ID, Titulo, Autor, Edicion, LugarImpresion, Editorial, Traduccion, Paginas, Estado FROM tblLibros WHERE Titulo LIKE '%"+datoBuscado+"%'"
            #sql = "SELECT ID, Titulo, Autor, Edicion, LugarImpresion, Editorial, Traduccion, Paginas, Estado FROM tblLibros WHERE ID = ?"

            #print("sql: ", sql)
            cursor.execute(sql)
            
            # se devuelven los datos encontrados    
            return cursor.fetchall()

        finally:
            #print("se cierra conexión")
            cc.close()

    
    # se crean las consultas para los libros
    def nuevoLibro(self, datoN):
        # se crea la conexión
        try:
            # objeto conectar
            cc = self.conectar()
            cursor = cc.cursor()
            sql = "INSERT INTO tblLibros (Titulo, Autor, Edicion, LugarImpresion, Editorial, Traduccion, Paginas, Estado) VALUES (?,?,?,?,?,?,?,?)"
            cursor.execute(sql, (datoN), )
            #print("sql", sql)
            #print("dato: ", dato)
            # grabamos en la base datos
            cc.commit()
            # cerramos la conexión
            cc.close()
        except sqlite3.OperationalError:
            mb.showerror("HA OCURRIDO UN ERROR!", "Error al ejecutar la consulta de INSERT INTO")

    def modificarLibro(self, datoM):
        # se crea la conexión
        try:
            cc = self.conectar()
            cursor = cc.cursor()
            sql = "UPDATE tblLibros SET Titulo=?, Autor=?, Edicion=?, LugarImpresion=?, Editorial=?, Traduccion=?, Paginas=?, Estado=? WHERE ID=?"
            cursor.execute(sql, datoM)
            #guardamos los cambios en la DB
            cc.commit()
            #cerramos la conexión
            cc.close()
        except sqlite3.OperationalError:
            mb.showerror("HA OCURRIDO UN ERROR!", "Error al ejecutar la consulta de UPDATE")
        
    def eliminarLibro(self, datoE):
        try:
            cc = self.conectar()
            cursor = cc.cursor()
            sql = "DELETE FROM tblLibros WHERE ID = ?"
            cursor.execute(sql, datoE)

            cc.commit()
        except:
            mb.showerror("HA OCURRIDO UN ERROR!", "Error al ejecutar la consulta DELETE")
        
        finally:
            cc.close()



    """----------------------------------Constultas a la tblAfiliado----------------------------------------------"""
    
    def buscarAfiliado(self, datoBuscadoA):
        #se crea la conexión
        try:
            cc = self.conectar()
            cursor = cc.cursor()
            #print("Nombre buscado: ", datoBuscadoA)
            sql = "SELECT ID, Nombre, Apellido, Telefono, Mail, Activo FROM tblAfiliado WHERE Nombre LIKE '%"+datoBuscadoA+"%'"

            #print("sql: ", sql)
            cursor.execute(sql)
            
            # se devuelven los datos encontrados    
            return cursor.fetchall()

        finally:
            #print("se cierra conexión")
            cc.close()

    def nuevoAfiliado(self, nuevoAfil):
        # se crea la conexión
        try:
            # objeto conectar
            cc = self.conectar()
            cursor = cc.cursor()
            sql = "INSERT INTO tblAfiliado (Nombre, Apellido, Telefono, Mail, Activo) VALUES (?,?,?,?,?)"
            cursor.execute(sql, (nuevoAfil), )
            #print("sql", sql)
            #print("nuevoAfil: ", nuevoAfil)
            # grabamos en la base datos
            cc.commit()
            # cerramos la conexión
            cc.close()
        except sqlite3.OperationalError:
            mb.showerror("HA OCURRIDO UN ERROR!", "Error al ejecutar la consulta de INSERT INTO")


    def modificarAfiliado(self, datoAfilM):
        # se crea la conexión
        try:
            cc = self.conectar()
            cursor = cc.cursor()
            sql = "UPDATE tblAfiliado SET Nombre=?, Apellido=?, Telefono=?, Mail=?, Activo=? WHERE ID=?"
            cursor.execute(sql, datoAfilM)
            #guardamos los cambios en la DB
            cc.commit()
            #cerramos la conexión
            cc.close()
        except sqlite3.OperationalError:
            mb.showerror("HA OCURRIDO UN ERROR!", "Error al ejecutar la consulta de UPDATE")
    
    def eliminarAfiliado(self, datoAfilE):
        try:
            cc = self.conectar()
            cursor = cc.cursor()
            sql = "DELETE FROM tblAfiliado WHERE ID = ?"
            cursor.execute(sql, datoAfilE)

            cc.commit()
        except:
            mb.showerror("HA OCURRIDO UN ERROR!", "Error al ejecutar la consulta DELETE")
        
        finally:
            cc.close()
    
    """----------------------------------Constultas a la tblPrestamo----------------------------------------------"""

    def buscarIDPrestamo(self, datoID):
        #se crea la conexión
        try:
            cc = self.conectar()
            cursor = cc.cursor()
            #print("ID buscado: ", datoID)
            sql = "SELECT max(ID) FROM tblPrestamo"

            cursor.execute(sql)
            res = cursor.fetchall()
            #print("res: ", res)
            
            # se devuelven los datos encontrados    
            return res

        finally:
            #print("se cierra conexión")
            cc.close()

    def buscarNroPrestamo(self, datoNro):
        #se crea la conexión
        try:
            cc = self.conectar()
            cursor = cc.cursor()
            #print("Nro buscado: ", datoNro)
            sql = "SELECT max(ID) + 1 FROM tblPrestamo"
            
            
            cursor.execute(sql)
            
            # se devuelven los datos encontrados    
            return cursor.fetchall()

        finally:
            #print("se cierra conexión")
            cc.close()
    
    def nuevoPrestamo(self, nuevoPrest):
        # se crea la conexión
        try:
            # objeto conectar
            cc = self.conectar()
            cursor = cc.cursor()
            sql = "INSERT INTO tblPrestamo (NroPrestamo, FechaPrestamo, FechaDevolucion, IDLibro,IDAfiliado) VALUES (?,?,?,?,?)"
            cursor.execute(sql, (nuevoPrest), )
            
            # grabamos en la base datos
            cc.commit()
            # cerramos la conexión
            cc.close()
        except sqlite3.OperationalError:
            mb.showerror("HA OCURRIDO UN ERROR!", "Error al ejecutar la consulta de INSERT INTO")

    def cambiarEstadoLibro(self, idL):
        # se crea la conexión
        try:
            cc = self.conectar()
            cursor = cc.cursor()
            
            sql = "UPDATE tblLibros SET Estado='Prestado' WHERE ID=?"
            cursor.execute(sql, idL)
            #guardamos los cambios en la DB
            cc.commit()
            #cerramos la conexión
            cc.close()
        except sqlite3.OperationalError:
            mb.showerror("HA OCURRIDO UN ERROR!", "Error al ejecutar la consulta de UPDATE")

    def cambiarEstadoLibroFinalizado(self, idL):
        # se crea la conexión
        try:
            cc = self.conectar()
            cursor = cc.cursor()
            
            sql = "UPDATE tblLibros SET Estado='Disponible' WHERE ID=?"
            cursor.execute(sql, idL)
            #guardamos los cambios en la DB
            cc.commit()
            #cerramos la conexión
            cc.close()
        except sqlite3.OperationalError:
            mb.showerror("HA OCURRIDO UN ERROR!", "Error al ejecutar la consulta de UPDATE")
    
    def controlfinPrestamo(self, nro):
        #se crea la conexión
        try:
            cc = self.conectar()
            cursor = cc.cursor()
            sql = "SELECT * FROM tblPrestamo WHERE ID = ?"
            
            #print("sql: ", sql)
            cursor.execute(sql, nro)
            
            # se devuelven los datos encontrados    
            return cursor.fetchall()

        finally:
            #print("se cierra conexión")
            cc.close()

    def guardarFechaFinalizacion(self, nroPrest):
        from datetime import datetime
        hoyFin = datetime.now()
        hoyFormat = hoyFin.strftime('%d/%m/%Y') # se guarda la fecha de hoy
        
        # se crea la conexión
        try:
            cc = self.conectar()
            cursor = cc.cursor()
            
            sql = f"UPDATE tblPrestamo SET FechaDevolucion='{hoyFormat}' WHERE ID=?"
            cursor.execute(sql, nroPrest)
            #guardamos los cambios en la DB
            cc.commit()
            #cerramos la conexión
            cc.close()
        except sqlite3.OperationalError:
            mb.showerror("HA OCURRIDO UN ERROR!", "Error al ejecutar la consulta de UPDATE")


    
    """----------------------------------Constultas para llenar Combobox-----------------------------------------"""
    def buscarIDLibro(self):
        #se crea la conexión
        try:
            cc = self.conectar()
            cursor = cc.cursor()
            sql = "SELECT ID FROM tblLibros WHERE Estado = 'Disponible'"
            
            #print("sql: ", sql)
            cursor.execute(sql)
            result = []
            for i in cursor.fetchall():
                result.append(i[0])
            
            # se devuelven los datos encontrados    
            return result

        finally:
            #print("se cierra conexión")
            cc.close()
    
    # buscar libro
    def buscarNombreLibro(self, idLibro):
        #se crea la conexión
        try:
            cc = self.conectar()
            cursor = cc.cursor()
            sql = "SELECT Titulo FROM tblLibros WHERE ID = ?"
            
            #print("sql: ", sql)
            cursor.execute(sql, idLibro)
            
            # se devuelven los datos encontrados    
            return cursor.fetchall()

        finally:
            #print("se cierra conexión")
            cc.close()
    
    # buscar libro
    def buscarLibrosTodos(self):
        #se crea la conexión
        try:
            cc = self.conectar()
            cursor = cc.cursor()
            sql = "SELECT * FROM tblLibros"
            #print("sql: ", sql)
            cursor.execute(sql)  
            # se devuelven los datos encontrados    
            return cursor.fetchall()
        finally:
            #print("se cierra conexión")
            cc.close()

    
    def buscarIDAfiliado(self):
        #se crea la conexión
        try:
            cc = self.conectar()
            cursor = cc.cursor()
            sql = "SELECT ID FROM tblAfiliado WHERE Activo = 'SI'"
            
            #print("sql: ", sql)
            cursor.execute(sql)
            resultA = []
            for j in cursor.fetchall():
                resultA.append(j[0])
            
            # se devuelven los datos encontrados    
            return resultA

        finally:
            #print("se cierra conexión")
            cc.close()
    
    # buscar Afiliado
    def buscarNombreAfiliado(self, idAfiliado):
        #se crea la conexión
        try:
            cc = self.conectar()
            cursor = cc.cursor()
            sql = "SELECT Nombre FROM tblAfiliado WHERE ID = ?"
            
            #print("sql: ", sql)
            cursor.execute(sql, idAfiliado)
            
            # se devuelven los datos encontrados    
            return cursor.fetchall()

        finally:
            #print("se cierra conexión")
            cc.close()
    