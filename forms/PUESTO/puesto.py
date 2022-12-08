class Puesto:
    
    def __init__(self, identificador, nombre, correo, edad, telefono, tipo_puesto, password, activo):
        self.identificador = identificador
        self.nombre = nombre
        self.correo = correo
        self.edad = edad
        self.telefono=telefono
        self.tipo_puesto = tipo_puesto
        self.password = password
        self.activo = activo
    
    def datoPuestoJson(self):
        return{
            "identificador": self.identificador,
            "nombre": self.nombre,
            "correo": self.correo,
            "edad": self.edad,
            "telefono":self.telefono,
            "tipo_puesto": self.tipo_puesto,
            "password": self.password,
            "activo": self.activo
        }    
