from ActividadesPermitidas import ActividadesPermitidas
from Persona import Persona
from PuestoDeControl import PuestoControl

#Actividades Autorizadas
actividad1=ActividadesPermitidas("Asistencia publica")
actividad2=ActividadesPermitidas("Medico")
actividad3=ActividadesPermitidas("Obra")

#Personas
persona1=Persona("Nahuel","Arrieta",38108760,"Domicilio 1111",425789,"@@@@@@@")
persona2=Persona("Lautaro","Arrieta",48108760,"Domicilio 2222",425789,"@@@@@@@")
persona3=Persona("Magali","Arrieta",11711354,"Domicilio 333",425789,"@@@@@@@")

#registrar persona
registrar=PuestoControl()
registrar.registrarPersona(persona1,actividad1)
registrar.registrarPersona(persona3,actividad2)

#pedir ingreso
persona1.pedirIngreso(persona1.dni)
persona2.pedirIngreso(persona2.dni)
persona3.pedirIngreso(persona3.dni)