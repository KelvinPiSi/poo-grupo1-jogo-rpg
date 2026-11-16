from character import Character

class Mago(Character):
    def __init__(self, name, attack, defense, mana, maxHeartPoints=100, maxStaminaPoints=100):
        super().__init__(name, attack, defense, maxHeartPoints, maxStaminaPoints)
        self._mana = mana

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        self._mana = value

    def status_mana(self):
        print(f"Mana atual: {self._mana}")
