from ActividadesAutorizadas import ActividadesAutorizadas
from PersonasAutorizadas import PersonasAutorizadas
import datetime
import os
class Empresa:

    def __init__(self, razonSocial, cuit, domicilio, localidad, email, telefono):
        self.__razonSocial=razonSocial
        self.__cuit=cuit
        self.__domicilio=domicilio
        self.__localidad=localidad
        self.__email=email
        self.__telefono=telefono
        
        print("Empresa".center(30," "),self.__razonSocial)
        self.__crearActividad = ActividadesAutorizadas()
        self._actividades = self.__crearActividad._actividad_empresa()


    def _registrar_persona(self, persona, fechaInicio):
        os.system ("pause")
        os.system ("cls")
        self.persona=persona
        self.fechaFin=fechaInicio + datetime.timedelta(days=30)
        print("Empresa".center(30," "),self.__razonSocial,"\nAsignar actividad a",self.persona._nombre,":")
        __actividad=input("".center(30, " "))
        os.system ("cls")
        
        if __actividad in self._actividades:
            print("Se asigno",__actividad,"correctamente a",persona._nombre,"\nSu autorización caduca:",self.fechaFin)
            autorizar = PersonasAutorizadas()
            self.lista = autorizar._repositorio(self.persona._dni, __actividad, self.fechaFin) 
        else:
            print("La actividad ",__actividad,"no existe en la base de datos")
        

    def _dar_baja_persona(self):
        dni=int(input("Ingresar el dni de la persona para dar de baja:"))

        if dni in self.lista:
            borrar = PersonasAutorizadas()
            borrar._borrar_persona(dni,self.persona._nombre)
        else:
            print("El documento no existe en la base de datos")
    