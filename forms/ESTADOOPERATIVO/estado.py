class EstadosCat:
    def __init__(self,identificador,EstadoOperativo):
        self.identificador=identificador
        self.EstadoOperativo=EstadoOperativo

    def datosEstadoOperativoJson(self):
            return {
            "identificador":self.identificador,
            "EstadoOperativo":self.EstadoOperativo
        }