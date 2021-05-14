class PuestoControl:
    personasAutorizadas={}
    
    def registrarPersona(self,cliente,actividad):
        self.cliente=cliente
        self.actividad=actividad
        self.personasAutorizadas[self.cliente.dni]=self.actividad
        return self.personasAutorizadas

    def autorizarPersona(self,dni):
        self.documento=dni

        if self.documento in self.personasAutorizadas:
            return True
        else:
            return False
    