from character import Character

class Mago(Character):
    def __init__(self, name, attack, defense, mana, maxHeartPoints=100, maxStaminaPoints=100):
        super().__init__(name, attack, defense, maxHeartPoints, maxStaminaPoints)
        self._mana = mana

