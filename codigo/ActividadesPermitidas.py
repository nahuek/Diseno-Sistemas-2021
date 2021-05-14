class ActividadesPermitidas:
    actividadesAutorizadas=[]
    def __init__(self,actividad):
        self.actividad=actividad
        self.actividadesAutorizadas.append(self.actividad)
        