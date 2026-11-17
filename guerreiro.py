from character import Character


class Guerreiro(Character):
    """Classe filha Guerreiro de character.py
    É a classe mais básica de todas"""
    def __init__(self, name, attack, defense, maxStaminaPoints, maxHeartPoints):
        super().__init__(name, attack, defense, maxStaminaPoints, maxHeartPoints)
        self.role = "Guerreiro"

    def __str__(self):
        """Retorna uma descrição do personagem com cada variável"""
        return super().__str__()

    def takeDamage(self, damage):
        """Permite que o personagem tome dano com uma mensagem especial"""
        super().takeDamage(damage)
        print(f"{self.name} foi infligido com {damage} de dano")

    def attack(self, other):
        """Ataca o adversário com uma quantidade de dano estabelecida no arquivo main.py com uma mensagem especial"""
        super().attack(other)
        print(f"{self.name} desferiu diversos golpes de machado em seu oponente")
