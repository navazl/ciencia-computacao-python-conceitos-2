class Triangulo():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b and self.a == self.c:
            return 'equilátero'
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return 'isósceles'
        elif self.a != self.b and self.a != self.c and self.b != self.c:
            return 'escaleno'

    def retangulo(self):
        lados = [self.a, self.b, self.c]
        posicao_maior = lados.index(max(lados))
        lados[0], lados[2] = lados[2], lados[0]

        h = lados[0]**2
        c = lados[1]**2 + lados[2]**2
        if h == c:
            return True
        elif h != c:
            return False

    def semelhantes(self, triangulo):
        if
        pass


if __name__ == "__main__":
    t1 = Triangulo(2, 3, 5)
    t2 = Triangulo(4, 6, 10)
    print(t1, t2)
