#clase Agenda
class Agenda:
    def __init__(self):
        
        self.contacto = []
        
    # -----------------Metodo Agendar------------------
    def agendar(self):
            print("Para agendar un contacto, por favor ingrese un nombre, telefono y email")
            
            nombre = input("Ingrese el nombre")
            while nombre=="":
                nombre = input("El nombre no puede estar vacio")
                
            try:
                telefono = int(input("Ingrese un numero de telefono"))
            except:
                input("Error: El dato ingresado no es correcto. Recuerde que el telefono no puede estar vacio, debe ser numeros y sin espacios. Presione una tecla para volver a cargar los datos")
                self.agendar()
            
            email = input("Ingrese un email")
            while email =="":
                email = input("Por favor ingrese un email")
                
            contacto = Contacto(nombre,telefono,email)
            self.contacto.append(contacto)
            input("Contacto cargado con exito. Presione una tecla para voler al menú principal")
            self.menu()
            
    #----------Metodo para mostrar contactos----------------    
    def mostrar_contactos(self):
        contador = 0
        for C in self.contacto:
            
            print("""
Nombre: {}
Telefono: {}
Email: {}
---------------------            """.format(C.nombre,C.telefono,C.email))
            contador+=1
        if contador == 0:
            input("No hay ningun contacto agendado. Presione una tecla para volver al menú principal")
        else:
            
            input("Presione una tecla para volver al menú principal")
        self.menu()
        

    #------Metodo para buscar contacto---------    
    def buscar_contacto(self,nombre):
        contador = 0
        for C in self.contacto:
            if C.nombre == nombre:
                print(""" 
Nombre: {}
Telefono: {}
Email: {}
--------------------""".format(C.nombre,C.telefono,C.email))
                contador+=1
        
        if contador ==0:
            input("No se encontro registro con ese nombre. Presione una tecla para volver al menú principal")
        else:
            input("Presione una tecla para voler al menú principal")
        
        self.menu()
    

    #---------Metodo para editar contacto----------------    
    def editar_contacto(self):
        contador=0
        for C in self.contacto:
            contador+=1
            print("{}) {}".format(contador,C.nombre))
        if contador > 0:
            
            L=int(input("Elija la opcion del contacto que desea modificar"))
            validar = input("Si desea cambiar el nombre {} presione la tecla Y de lo contrario presione N".format(self.contacto[L-1].nombre)).lower()
            if validar == "y":
                self.contacto[L-1].nombre = input("Por favor ingrese el nombre nuevo")
            validar = input("Si desea cambiar el Telefono {} presione la tecla Y de lo contrario presione N".format(self.contacto[L-1].telefono)).lower()
            if validar == "y":
                self.contacto[L-1].telefono = int(input("Por favor ingrese el telefono nuevo"))
            validar = input("Si desea cambiar el email {} presione la tecla Y de lo contrario presione N".format(self.contacto[L-1].email)).lower()
            if validar == "y":
                self.contacto[L-1].email = input("Por favor ingrese el email nuevo")
            print("""
    Los nuevos valos son:
        Nombre: {}
        Telefono: {}
        Email: {}
    --------------------""".format(self.contacto[L-1].nombre,self.contacto[L-1].telefono,self.contacto[L-1].email))
            input("Presione una tecla para volver a menú principal")
        else:
            input("No hay contactos agendados. Presione una tecla para volver al menú principal")
        self.menu()

    #--------Metodo menú--------------
    def menu(self):
        print("""
1) Añadir contacto
2) Lista de contactos
3) Buscar contacto
4) Editar contacto
5) Cerrar agenda
        """)
        try:
            opcion = int(input("Ingese una opcion"))
    
        except:
            input("Debe ingresa una opcion. Presione una tecla para volver al menú principal")
            self.menu()
        
        if opcion > 0 and opcion < 6:
            if opcion == 1:
                self.agendar()
            elif opcion ==2:
                self.mostrar_contactos()
            elif opcion ==3:
                self.buscar_contacto(input("Ingrese el nombre que desee buscar"))
            elif opcion == 4:
                self.editar_contacto()
            elif opcion == 5:
                print("Agenda Cerrada")
                
        else:
            input("Debe ser un numero valido...")
            self.menu()

#clase Contacto
class Contacto:
    def __init__(self,nombre,telefono,email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email


agenda = Agenda()
agenda.menu()


