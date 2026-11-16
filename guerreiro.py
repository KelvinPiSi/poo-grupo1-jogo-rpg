from character import Character


class Guerreiro(Character):
    def __init__(self, name, attack, defense, maxStaminaPoints, maxHeartPoints):
        super().__init__(name, attack, defense, maxStaminaPoints, maxHeartPoints)
        self.role = "Guerreiro"

    def __str__(self):
        return super().__str__()

    def takeDamage(self, damage):
        super().takeDamage(damage)
        print(f"{self.name} foi infligido com {damage} de dano")

    def attack(self, other):
        super().attack(other)
        print(f"{self.name} desferiu diversos golpes de machado em seu oponente")
