from PuestoDeControl import PuestoControl
class Persona:

    def __init__(self,nom,apell,dni,domi,tel,email):
        self.nombre=nom
        self.apellido=apell
        self.dni=dni
        self.domicilio=domi
        self.telefono=tel
        self.email=email

    def mostrar(self):
        print("Nombre:",self.nombre,self.apellido,"DNI:",self.dni)

    def pedirIngreso(self,dni):
        self.documento=dni
        verificar=PuestoControl()
        condicion=verificar.autorizarPersona(self.dni)

        if condicion == True:
            self.mostrar()
            print("-Tiene el acceso permitido")
        elif condicion == False:
            self.mostrar()
            print("-Tiene el acceso denegado")
