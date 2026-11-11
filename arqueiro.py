from personagem import Personagem

class Arqueiro(Personagem):

    def __init__(self, nome, lv = 1, hp = 100, energia = 100, qtdFlecha = 0):
        super().__init__(nome, lv, hp, energia)

        self.__qtdFlecha = qtdFlecha

    @property
    def qtdFlecha(self):
        return self.__qtdFlecha

    def atirar(self):
        if self.__qtdFlecha - 1 < 0:
            print(f"{self.nome} não possui mais flechas!")
            return

        self.__qtdFlecha -= 1

        print(f"{self.nome} atirou!")

    def dar(self, qtd):
        if qtd < 1:
            print("Quantidade inválida")
            return

        self.__qtdFlecha += qtd

        print(f"{self.nome} recebeu {qtd} flechas!")

    def tirar(self, qtd):
        if self.__qtdFlecha - qtd < 0:
            self.__qtdFlecha = 0

            print(f"{self.nome} perdeu todas as flechas!")
            return

        self.__qtdFlecha -= qtd

        print(f"{self.nome} perdeu {qtd} flecha(s)!")