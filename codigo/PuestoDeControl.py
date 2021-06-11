from os import truncate
from PersonasAutorizadas import PersonasAutorizadas
from datetime import date

class PuestoControl:

    def _autorizar_ingreso(self, dni):
        self.DNI=dni
        
        lista = PersonasAutorizadas()
        autorizaciones = lista._personas()
        
        if self.DNI in autorizaciones:
            today = date.today()
            
            if autorizaciones[self.DNI][1] > today:
                return True
            else:
                print("-Autorizacion vencida-")
                return False
        else:
            print("La persona no esta registrada")
            return False
