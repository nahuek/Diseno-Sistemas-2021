from ActividadesAutorizadas import ActividadesAutorizadas
from PersonasAutorizadas import PersonasAutorizadas
from generadorQR import RegistroQR
from PuestoDeControl import PuestoControl
import datetime
import os
class Empresa:

    def __init__(self, razonSocial, cuit, domicilio, localidad, email, telefono):
        self._razonSocial=razonSocial
        self.__cuit=cuit
        self.__domicilio=domicilio
        self.__localidad=localidad
        self.__email=email
        self.__telefono=telefono
        print("Empresa".center(30," "),self._razonSocial)
        self.__crearActividad = ActividadesAutorizadas()
        self._actividades = self.__crearActividad._actividad_empresa()


    def _registrar_persona(self, persona, fechaInicio):
        os.system ("pause")
        os.system ("cls")
        self.persona=persona
        self.fechaFin=fechaInicio + datetime.timedelta(days=30)
        print("Empresa".center(30," "),self._razonSocial,"\nAsignar actividad a",self.persona._nombre,":")
        __actividad=input("".center(30, " "))
        os.system ("cls")
        
        if __actividad in self._actividades:
            print("Se asigno",__actividad,"correctamente a",persona._nombre,"\nSu autorización caduca:",self.fechaFin)
            autorizar = PersonasAutorizadas()
            self.dicc = autorizar._repositorio(self.persona._dni, self.persona._nombre, __actividad, self.fechaFin) 
            qr= RegistroQR()
            qr.crear_QR(persona._nombre, persona._dni)
        else:
            print("La actividad ",__actividad,"no existe en la base de datos")
        

    def _dar_baja_persona(self):
        dni=int(input("Ingresar el dni de la persona para dar de baja:"))
        if dni in self.dicc:
            borrar = PersonasAutorizadas()
            borrar._borrar_persona(dni,self.dicc[dni][0])
        else:
            print("El documento no existe en la base de datos")
    

    def mostrar_registros(self):
        registro = PuestoControl()
        ingreso, egreso = registro.registros()
        os.system ("cls")
        print("Registro de ingreso de empleados\n")
        for ingresos in ingreso:
            print("DNI:",ingresos,"Fecha:",ingreso[ingresos][0],"Hora:",ingreso[ingresos][1],
                "Temperatura:",ingreso[ingresos][2],"Lugar:",ingreso[ingresos][3],"Patente:",ingreso[ingresos][4])
        os.system ("pause")
        os.system ("cls")
        print("Registro de egreso de empleados\n")
        for egresos in egreso:
            print("DNI:",egresos, "Hora:",egreso[egresos][0])