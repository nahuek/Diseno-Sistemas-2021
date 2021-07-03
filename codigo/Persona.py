from PuestoDeControl import PuestoControl
import os
class Persona:

    def __init__(self, nom, apell, dni, domi, tel, email):
        self._nombre=nom
        self.__apellido=apell
        self._dni=dni
        self.__domicilio=domi
        self.__telefono=tel
        self.__email=email


    def mostrar(self):
        print("Nombre:",self._nombre,self.__apellido,"\nDNI:",self._dni)


    def pedir_ingreso(self, nombre):
        os.system("pause")
        os.system ("cls")
        verificar = PuestoControl()
        condicion=verificar._autorizar_persona(nombre)
        if condicion == True:
            self.mostrar()
            print("-Tiene el acceso permitido")
        elif condicion == False:
            self.mostrar()
            print("-Tiene el acceso denegado")


    def pedir_egreso(self, nombre):
        verificar = PuestoControl()
        verificar.registrar_salida(nombre)   
