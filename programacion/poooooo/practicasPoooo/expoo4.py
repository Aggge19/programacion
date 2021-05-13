class Calculadora:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    def suma(self):
        resultado=self.n1+self.n2
        print(resultado)

    def resta(self):
        resultado=self.n1-self.n2
        print(resultado)

    def multiplicacion(self):
        resultado=self.n1*self.n2
        print(resultado)

    def division(self):
        resultado=self.n1/self.n2
        print(resultado)

c1=Calculadora(float(input("Numero 1:")),float(input("Numero 2:")),)    

c1.suma()
c1.resta()
c1.multiplicacion()
c1.division()