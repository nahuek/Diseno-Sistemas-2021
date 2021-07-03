class PersonasAutorizadas:
    _autorizaciones={}
   
    def _repositorio(self, dni,nombre, actividad, fecha):
        self._autorizaciones[dni]=(nombre, actividad, fecha)
        return self._autorizaciones

    def _personas(self):
        return self._autorizaciones

    
    def _borrar_persona(self, dni, nombre):
        print("¿Desea dar de baja a ",nombre,"?[s/n]")
        condicion=input("")

        if condicion == "s":
            del self._autorizaciones[dni]
            print("Se le dio de baja correctamente")

        
