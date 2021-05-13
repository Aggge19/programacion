import os
class Agenda():

    def __init__(self):
        self.contactos=[]

    def menu(self):
        opcio=int(input("\n1-Añadir contacto \n2-Lista de contactos \n3-Buscar contacto \n4-Editar contacto \n5-Cerrar agenda : "))
        r=1

        while r==1:
            if opcio==1:
                self.anyadir()
                opcio=int(input("\n1-Añadir contacto \n2-Lista de contactos \n3-Buscar contacto \n4-Editar contacto \n5-Cerrar agenda\n"))
            elif opcio==2:
                self.lista()
                opcio=int(input("\n1-Añadir contacto \n2-Lista de contactos \n3-Buscar contacto \n4-Editar contacto \n5-Cerrar agenda\n"))
            elif opcio==3:
                self.buscar()
                opcio=int(input("\n1-Añadir contacto \n2-Lista de contactos \n3-Buscar contacto \n4-Editar contacto \n5-Cerrar agenda\n"))
            elif opcio==4:
                self.editar()
                opcio=int(input("\n1-Añadir contacto \n2-Lista de contactos \n3-Buscar contacto \n4-Editar contacto \n5-Cerrar agenda\n"))
            elif opcio==5:
                r+=1
            else:
                opcio=int(input("Número incorrecto(1,2,3,4,5): "))


    def anyadir(self):
        #os.system("clear")
        nom=str(input("Nombre: "))
        telf=str(input("Telefono: "))
        email=str(input("Email: "))

        self.contactos.append({'nombre':nom,'telefono':telf,'email':email})



    def lista(self):
        for i in self.contactos:
            print(i)

    def buscar(self):
        selec=int(input("Que quieres buscar(introduce el numero):\n1-Nombre\n2-Teléfono\n3-Email\n"))
        q=1
        cont=0
        while q==1:   
            if selec==1:
                q+=1
                busq=str(input("Nombre: "))
                for i in self.contactos:
                    if busq==self.contactos[cont]['nombre']:
                        print(i)                
                    cont+=1
            elif selec==2:
                q+=1
                busq=str(input("Teléfono: "))
                for i in self.contactos:
                    if busq==self.contactos[cont]['telefono']:
                        print(i)                
                    cont+=1
            elif selec==3:
                q+=1
                busq=str(input("Email: "))
                for i in self.contactos:
                    if busq==self.contactos[cont]['email']:
                        print(i)                
                    cont+=1
            else:
                print("Del 1 al 3!!!!!!!")
                selec=int(input("Que quieres buscar(introduce el numero):\n1-Nombre\n2-Teléfono\n3-Email\n"))
      

    def editar(self):
        w=1
        for i in self.contactos:
            print(w,"-",i)
            w+=1
        editcont=int(input("Que contacto quieres editar: "))
        rer=int(input("Que apartado quieres editar?\n1-Nombre\n2-Teléfono\n3-Email\n"))
        z=1
        while z==1:           
            if rer==1:
                newname=str(input("Introduce un nuevo nombre: "))
                self.contactos[editcont-1]['nombre']=newname
                z+=1
            elif rer==2:
                newtelf=str(input("Introduce un nuevo teléfono"))
                self.contactos[editcont-1]['telefono']=newtelf
                z+=1
            elif rer==3:
                nweemail=str(input("Introduce un nuevo email"))
                self.contactos[editcont-1]['email']=newemail
                z+=1
            else:
                rer=int(input("Introduce un número correcto(1,2,3)\n1-Nombre\n2-Teléfono\n3-Email\n"))

a1=Agenda()
a1.menu()
