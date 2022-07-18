""" Queremos mantener una lista de los libros que hemos ido leyendo, calificando según nos haya gustado más o menos al leerlo. 

Para ello, crear la clase Libro, cuyos atributos son el titulo, el autor, el número de páginas
y la calificación que le damos entre 0 y 10. 

Crear los métodos para poder modificar y obtener los atributos si tienen sentido. 

Posteriormente, crear una clase ConjuntoLibros, que almacena un conjunto de libros.
Se pueden añadir libros que no existan (siempre que haya espacio),
eliminar libros por título o autor, mostrar por pantalla los libros con la mayor y menor calificación dada y,
por último, mostrar un contenido de todo el conjunto. """

#Clase Libro

class Libro:
    def __init__(self,titulo,autor,nP, calificacion):
        self.titulo = titulo
        self.autor = autor
        self.nP = nP
        self.calificacion = calificacion
        
    def modificar_titulo(self,titulo):
        self.titulo = titulo
    
    def modificar_autor(self,autor):
        self.titulo = autor
    
    def modificar_nP(self,nP):
        self.titulo = nP
    
    def modificar_calificacion(self,calificacion):
        self.titulo = calificacion

#Clase Conjunto de libros
class ConjuntoDeLibros:
    def __init__(self):
        self.listaLibro = []
    def agregar(self,libro):
        contador = 0
        if self.listaLibro ==[]:
            self.listaLibro.append(libro)
        elif libro.titulo != self.listaLibro[contador].titulo:
            self.listaLibro.append(libro)
        contador=contador +1
    
    def mostrar_libros(self):
        for L in self.listaLibro:
            print("\nTitulo: {}\nAutor: {}\nNumero de paginas: {}\nCalificación: {} \n----------------------- ".format(L.titulo,L.autor,L.nP,L.calificacion))
        
    def eliminar_libro(self,autorTitulo):
        contador=0
        for L in self.listaLibro:
            if L.titulo.lower() == autorTitulo.lower() or L.autor.lower() == autorTitulo.lower():
                self.listaLibro.pop(contador)
            contador+=1
    
    def mayor_calificacion(self):
        mayor_valor = None
        calificacion= ""
        for L in self.listaLibro:
            if mayor_valor is None or L.calificacion > mayor_valor:
                mayor_valor = L.calificacion
                calificacion= L
        return 'El libro con mayor calificación es "{}" que cuenta con una calificación de {}'.format(calificacion.titulo,calificacion.calificacion)

    def menor_calificacion(self):
        mayor_menor = None
        calificacion= ""
        for L in self.listaLibro:
            if mayor_menor is None or L.calificacion < mayor_menor:
                mayor_menor = L.calificacion
                calificacion= L
        return 'El libro con menor calificacion es "{}" con una calificación de  {}'.format(calificacion.titulo,calificacion.calificacion)

#Crear Objetos de la clase Libro
libro = Libro("biblia","desconicido", 700, 8)
libro2 = Libro("biblia","desconicido", 700, 10)
libro3 = Libro("Tora","desconicido", 700, 3)
libro4 = Libro("Talmud","desconicido", 700, 4)

#Modificar Objeto de la clase Libro
libro4.modificar_autor("Talmud tomo 1")

#Instanciar la clase ConjuntoDeLibros
conjuntoDeLibros = ConjuntoDeLibros()

#Agendar Objetos de Libro al objeto de conjuntoDeLibros
conjuntoDeLibros.agregar(libro)
conjuntoDeLibros.agregar(libro2)
conjuntoDeLibros.agregar(libro3)
conjuntoDeLibros.agregar(libro4)

#Eliminar un objeto 
conjuntoDeLibros.eliminar_libro("biblia")

#Mostrar Calificaciones
print(conjuntoDeLibros.menor_calificacion())
print(conjuntoDeLibros.mayor_calificacion())

#Motrar Libros
conjuntoDeLibros.mostrar_libros()
    