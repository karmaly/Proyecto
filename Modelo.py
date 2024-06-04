import mysql.connector
import pandas as pd
import scipy.io as sio

class BaseMySQL:
    def __init__(self):
        self.__host = 'localhost'
        self.__username = 'admin123'
        self.__password = 'contrasena123'
        self.__database = 'database'
        self.__connection = None
#nea n

    def validarIngreso(self, username:str, password:str):
        if username == self.__username and password == self.__password:
            return True
        return False
    
    def conectar(self, username:str , password:str):
        if self.validarIngreso(username, password):
            self.__connection = mysql.connector.connect(
                host = self.__host,
                user = self.__username,
                password = self.__password,
                database = self.__database
            )
            return True
        return False
    
    def desconectar(self):
        if self.__connection:
            self.__connection.close()
            self.__connection = None
            return True
        return False
    


    def validarPac(self, identificacion:str):
        query = 'SELECT * FROM pacientes WHERE identificacion = %s'
        cursor = self.__connection.cursor()
        cursor.execute(query, (identificacion,))
        results = cursor.fetchall()
        cursor.close()
        return len(results) == 0
            
    def ingresarPac(self, nombre:str, apellido:str, edad:str, identificacion:str):
        if self.validarPac(identificacion):
            query = 'INSERT INTO pacientes (nombre, apellido, edad, identificacion) VALUES (%s, %s, %s, %s)'
            values = (nombre, apellido, edad, identificacion)
            cursor = self.__connection.cursor()
            cursor.execute(query, values)
            self.__connection.commit()
            cursor.close()
            return True
        return False
        
    def eliminarPac(self, identificacion:str):
        if not self.validarPac(identificacion):
            query = 'DELETE FROM pacientes WHERE identificacion = %s'
            cursor = self.__connection.cursor()
            cursor.execute(query, (identificacion,))
            self.__connection.commit()
            cursor.close()
        return False
    
    def buscar(self, nombre):
        query = 'SELECT nombre, apellido, edad, identificacion FROM pacientes'
        cursor = self.__connection.cursor()
        cursor.execute(query)
        valores_columna = cursor.fetchall()
        cursor.close()
        if nombre:
            pacientes = [fila for fila in valores_columna if fila[0].startswith(nombre)]
        else:
            pacientes = valores_columna
        return pacientes

    def insertarArchivo(self, clave, tipo, ruta):
        query = 'INSERT INTO archivos (clave, tipo, ruta) VALUES (%s, %s, %s)'
        values = (clave, tipo, ruta)
        cursor = self.__connection.cursor()
        cursor.execute(query, values)
        self.__connection.commit()
        archivo_id = cursor.lastrowid
        cursor.close()
        return archivo_id

    def obtenerArchivos(self, tipo=None):
        query = 'SELECT id, clave, tipo, ruta FROM archivos'
        if tipo:
            query += ' WHERE tipo = %s'
            cursor = self.__connection.cursor()
            cursor.execute(query, (tipo,))
        else:
            cursor = self.__connection.cursor()
            cursor.execute(query)
        archivos = cursor.fetchall()
        cursor.close()
        return archivos

    def insertarDatosMat(self, archivo_id, nombre_matriz):
        query = 'INSERT INTO datos_mat (archivo_id, nombre_matriz) VALUES (%s, %s)'
        values = (archivo_id, nombre_matriz)
        cursor = self.__connection.cursor()
        cursor.execute(query, values)
        self.__connection.commit()
        cursor.close()

    def insertarDatosCsv(self, archivo_id, nombre_columna):
        query = 'INSERT INTO datos_csv (archivo_id, nombre_columna) VALUES (%s, %s)'
        values = (archivo_id, nombre_columna)
        cursor = self.__connection.cursor()
        cursor.execute(query, values)
        self.__connection.commit()
        cursor.close()

    def cargarMat(self, ruta):
        try:
            data = sio.loadmat(ruta)
            return data
        except Exception as e:
            print(f"Error al cargar archivo MAT: {e}")
            return None

    
    def cargarCsv(self, ruta, delimiter=','): #el código solo recibe delimitaciones por comas ',' 
        try:
            data = pd.read_csv(ruta, delimiter=delimiter)
            return data
        except Exception as e:
            print(f"Error al cargar archivo CSV: {e}")
            return None
        
