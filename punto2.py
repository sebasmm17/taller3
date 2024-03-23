class electrodomestico():
    def __init__(self,precio_base,color,consumo_energetico,peso):
        self.precio_base = precio_base
        self.color = color
        self.consumo_energetico = consumo_energetico
        self.peso = peso
    
    def precios_bases(self):
        if self.precio_base == 0:
            self.precio_base = 100
            return self.precio_base
        else:
            return self.precio_base
       
    def comprobar_consumo_energetico(self):
        if self.consumo_energetico == "":
            self.consumo_energetico = "f"
            return self.consumo_energetico
        elif self.consumo_energetico == "f":
            return self.consumo_energetico
        elif self.consumo_energetico == "e":
            return self.consumo_energetico
        elif self.consumo_energetico == "d":
            return self.consumo_energetico
        elif self.consumo_energetico == "c":
            return self.consumo_energetico
        elif self.consumo_energetico == "b":
            return self.consumo_energetico
        elif self.consumo_energetico == "a":
            return self.consumo_energetico
    
    def colores(self):

        if self.color == "":
            self.color = "blanco"
            return self.color
        elif self.color == "blanco":
                return self.color
        elif self.color == "negro":
            return self.color
        elif self.color == "rojo":
                return self.color
        elif self.color == "azul":
            return self.color
        elif self.color == "gris":
            return self.color
    
    def pesos (self):
        if self.peso >= 0 and self.peso <= 19:
            return self.peso
        if self.peso >= 20 and self.peso <= 49:
            return self.peso
    def precio_final1(self):
        if self.consumo_energetico == "" and self.peso >= 0 and self.peso <= 19:
            self.precio_base = self.precio_base + 10 + 10
            return self.precio_base
        elif self.consumo_energetico == "" and self.peso >= 20 and self.peso <= 49:
            self.precio_base = self.precio_base + 10 + 50
            return self.precio_base
        elif self.consumo_energetico == "f" and self.peso >= 0 and self.peso <= 19:
            self.precio_base = self.precio_base + 10 + 10
            return self.precio_base
        elif self.consumo_energetico == "f" and self.peso >= 20 and self.peso <= 49:
            self.precio_base = self.precio_base + 10 + 50
            return self.precio_base
        elif self.consumo_energetico == "e" and self.peso >= 0 and self.peso <= 19:
            self.precio_base = self.precio_base + 30 + 10
            return self.precio_base
        elif self.consumo_energetico == "e" and self.peso >= 20 and self.peso <= 49:
            self.precio_base = self.precio_base + 30 + 50
            return self.precio_base
        elif self.consumo_energetico == "d" and self.peso >= 0 and self.peso <= 19:
            self.precio_base = self.precio_base + 50 + 10
            return self.precio_base
        elif self.consumo_energetico == "d" and self.peso >= 20 and self.peso <= 49:
            self.precio_base = self.precio_base + 50 + 50
            return self.precio_base
        elif self.consumo_energetico == "c" and self.peso >= 0 and self.peso <= 19:
            self.precio_base = self.precio_base + 60 + 10
            return self.precio_base
        elif self.consumo_energetico == "c" and self.peso >= 20 and self.peso <= 49:
            self.precio_base = self.precio_base + 60 + 50
            return self.precio_base
        elif self.consumo_energetico == "b" and self.peso >= 0 and self.peso <= 19:
            self.precio_base = self.precio_base + 80 + 10
            return self.precio_base
        elif self.consumo_energetico == "b" and self.peso >= 20 and self.peso <= 49:
            self.precio_base = self.precio_base + 80 + 50
            return self.precio_base
        elif self.consumo_energetico == "a" and self.peso >= 0 and self.peso <= 19:
            self.precio_base = self.precio_base + 100 + 10
            return self.precio_base
        elif self.consumo_energetico == "a" and self.peso >= 20 and self.peso <= 49:
            self.precio_base = self.precio_base + 100 + 50
            return self.precio_base
    

class lavadora(electrodomestico):
    def __init__(self, precio_base, color, consumo_energetico, peso, carga):
        self.carga = carga
        super().__init__(precio_base, color, consumo_energetico, peso)

    def precio_final2(self):
        if self.carga > 30:
            self.precio_base  = self.precio_base + 50
            return self.precio_base
        else:
            self.precio_base = self.precio_base
            return self.precio_base

class televisor(electrodomestico):
    def __init__(self, precio_base, color, consumo_energetico, peso,resolucion,sintonizador_TDT):
        self.resolucion = resolucion
        self.sintonizador_TDT = sintonizador_TDT
        super().__init__(precio_base, color, consumo_energetico, peso)
    
    def precio_final3(self):

        if self.sintonizador_TDT == "si":
            self.sintonizador_TDT = True
            if self.resolucion > 40:
                self.precio_base = ((self.precio_base*30)/100)+50
                return self.precio_base
        elif self.sintonizador_TDT == "no":
            self.sintonizador_TDT = False
            self.precio_base = self.precio_base
            return self.precio_base

electrodomesticos = str(input("ingrese que electrodomestico quiere comprar: ")).lower()
if electrodomesticos == "lavadora":
    precio_base = float(input("ingrese el precio base: "))
    color = str(input("ingrese el color del electrodomestico: "))
    consumo_energetico = str(input("ingrese la letra del consumo energetico (A;B;C;D;E;F): "))
    peso = float(input("ingrese el peso: "))

    lavadora1 = lavadora(precio_base,color,consumo_energetico,peso,carga=int(input("ingrese la carga: ")))
    print(lavadora1.precios_bases(),lavadora1.comprobar_consumo_energetico(),lavadora1.colores(),lavadora1.pesos(),lavadora1.precio_final1(),lavadora1.precio_final2())
elif electrodomesticos == "televisor":
    precio_base = float(input("ingrese el precio base: "))
    color = str(input("ingrese el color del electrodomestico: "))
    consumo_energetico = str(input("ingrese la letra del consumo energetico (A;B;C;D;E;F): "))
    peso = float(input("ingrese el peso: "))
    resolucion = int(input("ingrese la resolucion del televisor: "))
    sintonizador_TDT = str(input("ingrese si tiene sintonizador TDT (si o no): ")).lower()
    
    televisor1 = televisor(precio_base,color,consumo_energetico,peso,resolucion,sintonizador_TDT)
    print(televisor1.precios_bases(),televisor1.comprobar_consumo_energetico(),televisor1.colores(),televisor1.pesos(),televisor1.precio_final1(),televisor1.precio_final3())
