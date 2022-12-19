class Auxiliar:

    def __init__(self, identificador, nombre, correo, edad, telefono):
        self.identificador = identificador
        self.nombre = nombre
        self.correo = correo
        self.edad = edad
        self.telefono = telefono
        

    def datoAuxiliarJson(self):
        return {
            "identificador": self.identificador,
            "nombre": self.nombre,
            "correo": self.correo,
            "edad": self.edad,
            "telefono": self.telefono,
            
        }    
