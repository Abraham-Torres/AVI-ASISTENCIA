class Operativo:
    def __init__(self,identificador,PuestoOperativo):
        self.identificador = identificador
        self.PuestoOperativo = PuestoOperativo
    def datosOperativoJson(self):
        return{
            "identificador": self.identificador,
            "PuestoOperativo": self.PuestoOperativo
                }    