from character import Character

class Arqueiro(Character):

    def __init__(self, name, attack, defense, maxHeartPoints=100, maxStaminaPoints=100, qtdFlecha = 0):
        super().__init__(name, attack, defense, maxHeartPoints, maxStaminaPoints)

        self.role = "Arqueiro"
        self.__qtdFlecha = qtdFlecha

    @property
    def qtdFlecha(self):
        return self.__qtdFlecha

    def atirar(self) -> bool:
        if self.__qtdFlecha - 1 < 0:
            print(f"{self.name} não possui mais flechas!")
            return False

        self.__qtdFlecha -= 1

        print(f"{self.name} atirou!")
        return True

    def dar(self, qtd):
        if qtd < 1:
            print("Quantidade inválida")
            return

        self.__qtdFlecha += qtd

        print(f"{self.name} recebeu {qtd} flechas!")

    def tirar(self, qtd):
        if self.__qtdFlecha - qtd < 0:
            self.__qtdFlecha = 0

            print(f"{self.name} perdeu todas as flechas!")
            return

        self.__qtdFlecha -= qtd

        print(f"{self.name} perdeu {qtd} flecha(s)!")

    def __str__(self):
        return super().__str__() + f"\n\tQtd. de Flechas: {self.__qtdFlecha}"

    def attack(self, other):
        if not self.atirar():
            return

        self.tirar(1)
        super().attack(other)