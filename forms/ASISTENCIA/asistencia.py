class Asistencia:
    def __init__(self, identificador,nombre,edad,telefono,auxiliar,placas,estado,fecha,inicio,fin):
        self.identificador = identificador
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.auxiliar = auxiliar
        self.placas = placas
        self.estado = estado
        self.fecha = fecha
        self.inicio = inicio
        self.fin = fin


    def datosAsistenciaJson(self):
        return {
            'identificador': self.identificador,
            'nombre': self.nombre,
            'edad': self.edad,
            'telefono': self.telefono,
            'auxiliar': self.auxiliar,
            'placas': self.placas,
            'estado': self.estado,
            'fecha': self.fecha,
            'inicio': self.inicio,
            'fin': self.fin
        }
