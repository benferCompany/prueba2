#clase Cafetera
class Cafetera:
    def __init__(self):
        self.capacidadMaxima = 1000
        self.capacidadActual = 0
    
    def llenarCafetera(self):
        self.capacidadActual = 1000
    
    def servirTaza(self,solicitud):
        try:
            taza= int(solicitud)
            
            if taza > self.capacidadActual and self.capacidadActual > 0:
                print("debido a que no hay la cantidad de cafe solicitada, su taza  se cargó con {}cc ya que es la cantidad total en la cafetera . Por favor trate de llenarno nuevamente".format(self.capacidadActual))
                self.capacidadActual=0
            elif self.capacidadActual==0:
                print("No hay cafe. Por favor vuelva a llenarlo")
            elif taza<0:
                print("Por favor ingrese un numero entero positivo")
            else:
                self.capacidadActual = self.capacidadActual-taza
                print("la taza se lleno con la cantidad solicitada. La capacidad actual es de: {}cc".format(self.capacidadActual))
    
        except ValueError:
            print("Por favor ingrese un numero entero")
    
    def vaciarCafetera(self):
        self.capacidadActual=0
    
    def agregarCafe(self,cantidad):
        if cantidad <= self.capacidadMaxima-self.capacidadActual:
            self.capacidadActual+=cantidad
            print("se agregó con exito, la capacidad actual es de {}cc".format(self.capacidadActual))
        else:
            print("La cafetera no soporta esa cantidad, la capacidad actual es de {}cc y su capacidad maxima es de {}cc no puede agregar mas de {}cc".format(self.capacidadActual, self.capacidadMaxima, self.capacidadMaxima - self.capacidadActual))

#instanciar Cafetera - crear objeto cafetera
cafetera = Cafetera()

#Llenar cafetera
cafetera.llenarCafetera()
print("Cafetera actual cuenta con {}cc".format(cafetera.capacidadActual))

#Servir taza
cafetera.servirTaza(400)

#Agregar a la cafetera
cafetera.agregarCafe(501)
cafetera.agregarCafe(300)

