class Administrador:
    def __init__(self,identificador, nombre, correo, password):
        self.identificador = identificador
        self.nombre = nombre
        self.correo = correo
        self.password = password

    def datosAdministradorJson(self):
        return {
            'identificador': self.identificador,
            'nombre': self.nombre,
            'correo': self.correo,
            'password': self.password
        }    