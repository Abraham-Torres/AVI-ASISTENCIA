class Asistencia:
    def __init__(self, identificador, nombre, fecha, inicio, operativo, puesto, fin):
        self.identificador = identificador
        self.nombre = nombre
        self.fecha = fecha
        self.inicio = inicio
        self.operativo = operativo
        self.puesto = puesto
        self.fin = fin

    def datosAsistenciaJson(self):
        return {
            'identificador': self.identificador,
            'Nombre': self.nombre,
            'Fecha': self.fecha,
            'Inicio': self.inicio,
            'Estado': self.operativo,
            'Puesto': self.puesto,
            'fin': self.fin
        }
