class Mate:
    def __init__(self,cantidad_de_cebada):
        
        try:
            cantidad_maxima_cebadas = int(cantidad_de_cebada)
            self.cantidad_maxima_cebadas = int(cantidad_maxima_cebadas)
            self.cantidad_de_yerba = cantidad_maxima_cebadas*10
        except:
            print("{} No es un valor valido. Por favor ingrese un dato de valor numerico, de lo contrario se pondra su valor por defecto que es 0".format(yerba))
            self.cantidad_maxima_cebadas = 0
            self.cantidad_de_yerba = 0
        self.estado = "vacio"
        
    
    def cebar(self):
        if self.estado == "vacio":
            self.estado = "lleno"
            print("El mate se llenó con exito")
        elif self.estado == "lleno":
            print("¡Cuidado! ¡Te quemaste!")
    
    def beber(self):
        if self.estado == "vacio":
           print("El mate está vacío!")
           
        elif self.estado == "lleno" and self.cantidad_maxima_cebadas == 0:
            self.estado="vacio"
            self.cantidad_de_yerba ="Yerba lavada"
            print("Advertencia: el mate está lavado")
        else:
            self.cantidad_maxima_cebadas-=1
            self.estado="vacio"
            print("El mate fue bebido. El estado actual del mate es: {}".format(self.estado))
            
#instanciar clase Mate 
#La cantidad de yerba equivale a 10grs por cebada.

mate = Mate(2)

#imprime cantidad_maxima_cebadas
print(mate.cantidad_maxima_cebadas)

#imprime cantidad de yerba
print("Hay {}grs de yerba en el recipiente".format(mate.cantidad_de_yerba))

#cebar mate
mate.cebar()
mate.cebar()

#beber
mate.beber()

#beber y cebar
mate.cebar()
mate.beber()

mate.cebar()
mate.beber()

print("{}. Por favor cambiela.".format(mate.cantidad_de_yerba))