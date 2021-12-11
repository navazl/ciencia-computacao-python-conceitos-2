class Treino():
    def __init__(self, maxPeso, rep):
        self.maxPeso = maxPeso
        self.rep = rep

    def pegar_peso(self, peso):
        if peso > self.maxPeso:
            print("Você não vai aguentar, é muito peso!")
        else:
            print("Pode treinar!")


treino_braço = Treino(15, 10)
treino_braço.pegar_peso(16)
