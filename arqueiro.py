from character import Character
import time

class Arqueiro(Character):
    """A classe arqueiro contém uma variável chamada qtdFlecha
    Está variavel possibilita a classe de utilizar a função def attack"""
    def __init__(self, name, attack, defense, maxHeartPoints=100, maxStaminaPoints=100, qtdFlecha = 0):
        super().__init__(name, attack, defense, maxHeartPoints, maxStaminaPoints)

        self.role = "Arqueiro"
        self.__qtdFlecha = qtdFlecha

    @property
    def qtdFlecha(self):
        return self.__qtdFlecha

    def atirar(self) -> bool:
        """Retorna se o personagem possui ou não flechas.
        Se possuir, printa (Atirou)
        Se não possuir, questiona conceder mais"""
        if self.__qtdFlecha - 1 < 0:
            print(f"{self.name} não possui mais flechas! ", end="")

            for i in range(3):
                time.sleep(.5)
                print(".", end="")

            time.sleep(.5)

            mais = int(input("\n\tVocê deseja conceder mais flechas? Se sim, quantas? (0 p/ nenhuma) "))

            if not self.dar(mais):
                return False

        self.__qtdFlecha -= 1

        print(f"{self.name} atirou!")
        return True

    def dar(self, qtd) -> bool:
        """Adiciona uma quantidade lida de flechas a variavel qtdFlechas do personagem"""
        if qtd < 1:
            print("Quantidade inválida")
            return False

        if qtd == 0:
            print(f"{self.name} ficou sem flechas mesmo :(")
            return False

        self.__qtdFlecha += qtd

        print(f"{self.name} recebeu {qtd} flechas!")
        return True

    def tirar(self, qtd):
        """Retira uma quantidade de flechas do personagem"""
        if self.__qtdFlecha - qtd < 0:
            self.__qtdFlecha = 0

            print(f"{self.name} perdeu todas as flechas!")
            return

        self.__qtdFlecha -= qtd

        print(f"{self.name} perdeu {qtd} flecha(s)!")

    def __str__(self):
        """Retorna uma descrição do personagem + a variavel qtdFlechas para este personagem"""
        return super().__str__() + f"\n\tQtd. de Flechas: {self.__qtdFlecha}"

    def attack(self, other):
        """Ataca o adversário com uma quantidade de dano estabelecida no arquivo main.py"""
        if not self.atirar():
            return

        self.tirar(1)
        super().attack(other)
