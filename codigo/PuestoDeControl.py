from os import truncate
from PersonasAutorizadas import PersonasAutorizadas
from generadorQR import RegistroQR
from datetime import date, datetime

class PuestoControl:
    registroIngreso={}
    registroEgreso={}

    def verificar_QR(self, nombre):
        verificar=RegistroQR()
        self.dni = verificar.leer_QR(nombre)
        return self.dni
        

    def _autorizar_persona(self, nombre):
        self.dni = self.verificar_QR(nombre)
        diccionario = PersonasAutorizadas()
        autorizaciones = diccionario._personas()
        if self.dni in autorizaciones:
            fecha = date.today()
            hora = datetime.now().time()
            print("Verificar temperatura de ",autorizaciones[self.dni][0])
            temperatura=float(input(""))
            if temperatura < 37:
                if autorizaciones[self.dni][2] > fecha:
                    fechastr=fecha.strftime('%d/%m/%Y')
                    self.registro_ingreso(fechastr, hora, temperatura, autorizaciones[self.dni][1])                
                    return True
                else:
                    print("-Autorizacion vencida-")
                    return False
            else:
                fechastr=fecha.strftime('%d/%m/%Y')
                self.registro_ingreso(fecha, hora, temperatura)
                print("La persona registra una temperatura mayor a 37°")
                return False
        else:
            print("La persona no esta registrada")
            return False


    def registro_ingreso(self, fecha, hora, temperatura, lugar="", patente=""):
        self.fecha=fecha
        self.lugar=lugar
        self.patente=patente
        self.horastr = hora.strftime('%H:%M:%S')

        if temperatura < 37:
            condicion=input("¿La persona tiene vehiculo?[s/n]")
            if condicion =="s":
                self.patente=input("Registrar patente:")
                self.registroIngreso[self.dni]=[self.fecha, self.horastr, temperatura, self.lugar, self.patente]
            else:
                self.registroIngreso[self.dni]=[self.fecha, self.horastr, temperatura, self.lugar,self.patente]
        else:
            self.registroIngreso[self.dni]=[self.fecha, self.horastr, temperatura, self.lugar, self.patente]
            

    def registrar_salida(self, nombre):
        hora = datetime.now().time()
        horastr = hora.strftime('%H:%M:%S')
        self.dni = self.verificar_QR(nombre)
        self.registroEgreso[self.dni]=[horastr]

    def registros(self):
        return self.registroIngreso, self.registroEgreso