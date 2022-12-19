class Puesto:
    
    def __init__(self, identificador, nombre, correo, edad, telefono, auxiliar, password, activo):
        self.identificador = identificador
        self.nombre = nombre
        self.correo = correo
        self.edad = edad
        self.telefono=telefono
        self.auxiliar = auxiliar
        self.password = password
        self.activo = activo
    
    def datoPuestoJson(self):
        return{
            "identificador": self.identificador,
            "nombre": self.nombre,
            "correo": self.correo,
            "edad": self.edad,
            "telefono":self.telefono,
            "auxiliar": self.auxiliar,
            "password": self.password,
            "activo": self.activo
        }    
