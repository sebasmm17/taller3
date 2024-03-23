class calcular_IMC():
    def __init__(self,altura,peso):
        self.altura = altura
        self.peso = peso
    def calculoIMC(self):
        imc = self.peso/(self.altura**2)
        print("Calculando IMC...")
        if imc < 20:
            print("\n-1")
            print("\nestas por debajo del peso ideal.")
            return ""
        elif imc > 25:
            print ("\n1")
            print ("\nestas por encima del peso ideal.")
            return ""
        else:
            print("\n0")
            print("\nestas en tu peso ideal.")
            return ""

class edades():
    def __init__(self,edad):
        self.edad = edad
    def mayor_de_edad(self):
        print("\nVerificando si es mayor de edad...")
        if self.edad > 18:
            self.edad = True
            print("\neres mayor de edad.")
            return ""
        else:
            self.edad = False
            print("\neres menor de edad.")
            return ""

class genero():
    def __init__(self,sexo):
        self.sexo = sexo
    def identificador(self):
        print("\nIdentificando su genero...")
        if self.sexo != "Hombre" or self.sexo != "Mujer":
            self.sexo = "h"
            print (self.sexo)
            return""
        elif self.sexo == "Hombre":
            self.sexo = "h"
            print (self.sexo)
            return""
        elif self.sexo == "Mujer":
            self.sexo = "m"
            print (self.sexo)
            return""
        
class string():
    def __init__(self,nombre,edad,DNI,sexo,peso,altura):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
    def mostrar(self):
        print("\nMostrando todos los datos ingresados...")
        print (f"\n{self.nombre}\n{edad}\n{self.DNI}\n{self.sexo}\n{self.peso}\n{self.altura}")
        return ""
class persona(calcular_IMC,edades,genero,string):
    def __init__(self,nombre,edad,DNI,sexo,peso,altura):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

nombre = input("ingrese su nombre completo: ")
edad = int(input("ingrese su edad: "))
DNI = int(input("ingrese su DNI: "))
sexo = input("ingrese su genero: ")
peso = float(input("ingrese su peso: "))
altura = float(input("ingrese su altura: "))

persona1 = persona(nombre,edad,DNI,sexo,peso,altura)
print(persona1.calculoIMC(),persona1.mayor_de_edad(),persona1.identificador())
print(persona1.mostrar())