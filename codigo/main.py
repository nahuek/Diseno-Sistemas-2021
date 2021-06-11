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
empresa1._registrar_persona(persona1, date(2021,5,15))
empresa1._registrar_persona(persona2, date(2021,5,2))
empresa2._registrar_persona(persona3, date(2021,5,20))

#pedir ingreso
persona1.pedir_ingreso(persona1._dni)
persona2.pedir_ingreso(persona2._dni)
persona3.pedir_ingreso(persona3._dni)

#dar de baja
empresa1._dar_baja_persona()

#pedir ingreso despues de baja
persona2.pedir_ingreso(persona2._dni)
