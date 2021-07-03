from datetime import date
from Persona import Persona
from PuestoDeControl import PuestoControl
from Empresa import Empresa
import os

#registro de empresa y sus actividades
empresa1=Empresa("S.R.L",9-4536-8,"domicilio","localidad","@@@@","telefono3564")
empresa2=Empresa("S.A",9-4536-8,"domicilio","localidad","@@@@","telefono3564")

#Personas
persona1=Persona("Nahuel","Arrieta",38108760,"Domicilio 1111",425789,"@@@@@@@")
persona2=Persona("Lautaro","Arrieta",48108760,"Domicilio 2222",425789,"@@@@@@@")
persona3=Persona("Magali","Arrieta",11711354,"Domicilio 333",425789,"@@@@@@@")

#registrar persona
empresa1._registrar_persona(persona1, date(2021,6,27))
empresa1._registrar_persona(persona2, date(2021,6,29))
empresa2._registrar_persona(persona3, date(2021,5,28))

#pedir ingreso 
persona1.pedir_ingreso(persona1._nombre)
persona2.pedir_ingreso(persona2._nombre)
persona3.pedir_ingreso(persona3._nombre)

#dar de baja empleado
os.system("pause")
os.system ("cls")
def dar_baja(empresa):
    empresa._dar_baja_persona()

print("".center(20," "), empresa1._razonSocial)
condicion= input("Desea dar de baja a un empleado?[s/n]:")
if condicion == "s":
    dar_baja(empresa1)
print("".center(20," "), empresa2._razonSocial)
condicion= input("Desea dar de baja a un empleado?[s/n]:")
if condicion == "s":
    dar_baja(empresa2)

#pedir egreso
persona1.pedir_egreso(persona1._nombre)

#mostrar registros
condicion=input("¿Desea ver el registro del dia?[s/n]:")
if condicion == "s":
    empresa1.mostrar_registros()

#pedir ingreso despues de baja(sacar comentarios)
# persona2.pedir_ingreso(persona2._nombre)
