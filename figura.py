class Figura:
    def __init__(self):
        pass
    
    def dame_perimetro(self):
        print("Esta figura no tiene perímetro")
    def dame_area(self):
        print("Esta figura no tiene area")
        
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
        super().__init__()

    def dame_perimetro(self):
        perimetro = 4 * self.lado
        return perimetro
    def dame_area(self):
        area = self.lado**2
        return area

c1 = Cuadrado(3)
print(c1.dame_area())
print(c1.dame_perimetro())
