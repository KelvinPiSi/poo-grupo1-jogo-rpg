from character import Character

class Mago(Character):
    def __init__(self, name, attack, defense, mana, maxHeartPoints=100, maxStaminaPoints=100):
        super().__init__(name, attack, defense, maxHeartPoints, maxStaminaPoints)
        self._mana = mana
        self.role = "Mago"

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        self._mana = value

    def status_mana(self):
        print(f"Mana atual: {self._mana}")

    def attack(self, other):
        if self._mana >= 10:
            self._mana -= 10
            other.takeDamage(self.getAttack + 25)
        else:
            other.takeDamage(self.getAttack + 5)