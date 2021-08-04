class Vehículo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def mostrarColor(self):
        print(f"Mi color es: {self.color}")

    def mostrarRuedas(self):
        print(f"Tengo {self.ruedas} ruedas")

class Coche(Vehículo):
    def __init__(self,color,ruedas,velocidad,cilindrada):
        Vehículo.__init__(self, color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def mostrarVelocidad(self):
        print(f"Mi velocidad es: {self.velocidad} KM/H")

    def mostrarCilindrada(self):
        print(f"Tengo {self.cilindrada} cilindradas ")

#Programa

color=input("Ingrese el color del coche:\t")
ruedas = int(input("Ingrese cantidad de ruedas:\t"))
velocidad = int(input("Ingrese velocidad: \t"))
cilindrada = int(input("Ingrese la cilindrada: \t"))

auto = Coche(color,ruedas,velocidad,cilindrada)

auto.mostrarColor()
auto.mostrarRuedas()
auto.mostrarVelocidad()
auto.mostrarCilindrada()