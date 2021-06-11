class ActividadesAutorizadas:
    _actividades=[]
        
    def _actividad_empresa(self):
        condicion=input("¿Desea ingresar una actidad para la empresa? - [s/n]: ")
        while condicion == "s":    
            actividad=input("Nombre de la actividad: ")
            self._actividades.append(actividad)
            print("\nLa actividad ",actividad,"se agrego correctamente \n")
            condicion=input("¿Desea ingresar otra actividad? - [s/n]: ")

        return self._actividades