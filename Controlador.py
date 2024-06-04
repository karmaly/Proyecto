from Modelo import *

class controlador:
    def __init__(self, controlador = BaseMySQL(), acceso = manejoUsuarios()):
        self.__controlador = controlador
        self.__acceso = acceso
    
    def conectarCont(self, username:str, password:str):
        bool = self.__controlador.conectar(username, password)         
        return bool
    
    def ingresarPacCont(self, nombre:str, apellido:str, edad:str, identificacion:str):
        bool = self.__controlador.ingresarPac(nombre, apellido, edad, identificacion)
        return bool
    
    def listaPacCont(self, nombre):
        return self.__controlador.buscar(nombre)
    
    def eliminarPacCont(self, identificacion:str):
        return self.__controlador.eliminarPac(identificacion)

        ####################################

    def insertarArchivoCont(self, clave, tipo, ruta):
        return self.__controlador.insertarArchivo(clave, tipo, ruta)
    
    def obtenerArchivosCont(self, tipo=None):
        return self.__controlador.obtenerArchivos(tipo)
    
    def cargarMatCont(self, ruta):
        return self.__controlador.cargarMat(ruta)
    
    def cargarCsvCont(self, ruta):
        return self.__controlador.cargarCsv(ruta)

    def insertarDatosMatCont(self, archivo_id, nombre_matriz):
        return self.__controlador.insertarDatosMat(archivo_id, nombre_matriz)

    def insertarDatosCsvCont(self, archivo_id, nombre_columna):
        return self.__controlador.insertarDatosCsv(archivo_id, nombre_columna)

        ####################################
        
    def ingresoCont(self, username:str, password:str):
        return self.__acceso.ingreso(username, password)
    
    def nuevousuarioCont(self, username:str, password:str):
        return self.__acceso.nuevousuario(username, password)
    
    def modificarCont(self, usernameviejo:str, passwordviejo:str, username:str, password:str):
        return self.__acceso.modificar(usernameviejo, passwordviejo, username, password)
        
    
        
    
        