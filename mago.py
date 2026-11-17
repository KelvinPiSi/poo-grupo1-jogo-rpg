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
        """Retorna a quantidade de mana atual restante do personagem"""
        print(f"Mana atual: {self._mana}")

    def takeDamage(self, damage):
        """Permite que o personagem tome dano com uma mensagem especial"""
        super().takeDamage(damage)
        print("Nosso querido mago foi atingido em ", damage, " de dano")

    def attack(self, other):
        """Ataca o adversário com uma quantidade de dano estabelecida no arquivo main.py
        Se mana estiver abaixo do valor estabelecido, o dano é reduzido"""
        print(f"{self.name} usou magiazinha!")
        if self._mana >= 10:
            self._mana -= 10
            other.takeDamage(self.getAttack + 25)
        else:
            other.takeDamage(self.getAttack + 5)