class Vehiculos:
    def __init__(self,ruedas, color):
        self.color = color
        self.ruedas = ruedas
    def mostrar_detalles(self):
        print(
                """
Clase: Vehiculo
Cantidad de ruedas: {}
Color: {}

---------------------
                """.format(self.ruedas,self.color))

class Coche(Vehiculos):
    def __init__(self,color,ruedas,velocidad, cilindrada):
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        Vehiculos.__init__(self,color,ruedas)
     
    def mostrar_detalles(self):
        print(
                """
Clase: Coche
Cantidad de ruedas: {}
Color: {}
Cilindrada: {}
Velocidad: {}
---------------------
                """.format(self.ruedas,self.color,self.cilindrada,self.velocidad))    
class Camioneta(Coche):
    def __init__(self,velocidad,cilindrada,color,ruedas,carga):
        self.carga=carga
        Coche.__init__(self,velocidad,cilindrada,color,ruedas)
        
    def mostrar_detalles(self):
        print(
                """
Clase: Camioneta
Cantidad de ruedas: {}
Color: {}
Carga: {}
Cilindrada: {}
Velocidad: {}
---------------------
                """.format(self.ruedas,self.color,self.carga,self.cilindrada,self.velocidad))
class Bicicleta(Vehiculos):
    def __init__(self,ruedas,color,tipo):
        self.tipo= tipo
        Vehiculos.__init__(self,ruedas,color)
    
    def mostrar_detalles(self):
        print(
        """
Cantidad de ruedas: {}
Color: {}
Tipo: {}
        """.format(self.ruedas,self.color,self.tipo))
        
class Motocicleta(Bicicleta):
    def __init__(self,ruedas,color,tipo,velocidad,cilindrada):
        Bicicleta.__init__(self,ruedas,color,tipo)
        self.velocidad= velocidad
        self.cilindrada=cilindrada
        

    def mostrar_detalles(self):
        print(
                """
Clase: Motocicleta
Cantidad de ruedas: {}
Color: {}
Tipo: {}
Velocidad: {}
Cilindrada: {}
---------------------
                """.format(self.ruedas,self.color,self.tipo,self.cilindrada,self.velocidad))
#Instanciar la clase Vehiculos y mostrar detalles
vehiculos = Vehiculos(None,"A definir")
vehiculos.mostrar_detalles()

#Instanciar las clase Coche y mostrar detalles
coche = Coche(4,"A definir",None,None)
coche.mostrar_detalles()

#Instanciar las clase Camioneta y mostrar detalles
camioneta = Camioneta(4,"Negro",150,3000,3500)
camioneta.mostrar_detalles()

#Instanciar la clase Bicicleta y mostrar detalles
bicicleta = Bicicleta(2,"Azul","urbano")
bicicleta.mostrar_detalles()

#Instanciar la clase Motocicleta y mostrar detalles
motocicleta = Motocicleta(2,"Gris","Deportiva",600,230)
motocicleta.mostrar_detalles()