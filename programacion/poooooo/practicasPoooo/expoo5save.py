import os
class Agenda():

    def __init__(self):
        self.contactos=[]

    def menu(self):
        letra=str(input("\n·Añadir contacto \n·Lista de contactos \n·Buscar contacto \n·Editar contacto \n·Cerrar agenda \n(introducir la primera letra en minuscula): "))
        r=1
        while r==1:
            if letra=="a" or letra =="A":
                self.anyadir()
                letra=str(input("\n·Añadir contacto \n·Lista de contactos \n·Buscar contacto \n·Editar contacto \n·Cerrar agenda \n(introducir la primera letra en minuscula): "))
            elif letra=="l" or letra=="L":
                self.lista()
                letra=str(input("\n·Añadir contacto \n·Lista de contactos \n·Buscar contacto \n·Editar contacto \n·Cerrar agenda \n(introducir la primera letra en minuscula): "))
            elif letra=="b" or letra=="B":
                self.buscar()
                letra=str(input("\n·Añadir contacto \n·Lista de contactos \n·Buscar contacto \n·Editar contacto \n·Cerrar agenda \n(introducir la primera letra en minuscula): "))
            elif letra=="e" or letra=="E":
                self.editar()
                letra=str(input("\n·Añadir contacto \n·Lista de contactos \n·Buscar contacto \n·Editar contacto \n·Cerrar agenda \n(introducir la primera letra en minuscula): "))
            elif letra=="c" or letra=="C":
                r+=1
            else:
                letra=str(input("Letra incorrecta(a,l,b,e,c): "))


    def anyadir(self):
        #os.system("clear")
        nom=str(input("Nombre: "))
        telf=str(input("Telefono: "))
        email=str(input("Email: "))

        self.contactos.append({'nombre':nom,'telef':telf,'email':email})



    def lista(self):
        for i in self.contactos:
            print(i)

    def buscar(self):
        selec=int(input("Que quieres buscar(introduce el numero):\n1-Nombre\n2-Teléfono\n3-Email\n"))
        q=1
        cont=0
        # for i in self.contactos:
        #     cont+=1
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
                print("telf")
            elif selec==3:
                q+=1
                print("email")
            else:
                print("Del 1 al 3!!!!!!!")
                selec=int(input("Que quieres buscar(introduce el numero):\n1-Nombre\n2-Teléfono\n3-Email\n"))

       

    def editar(self):
        print("e")


a1=Agenda()
a1.menu()
