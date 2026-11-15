from character import Character


class Guerreiro(Character):
    def __init__(self, nome, attack, defense,maxStaminaPoints,maxHeratPoints, rage=0):
        super().__init__(self, nome, attack, defense, maxStaminaPoints,maxHeratPoints)
        self.__rage = rage
        self.strenght = 15

    def takeDamage(self, damage):
        self.__heartPoints -= damage - self.__defense
        self.__rage =+ 5

    def specialAttack(self, other):
        if self.__rage > 25:
            other.takeDamage(self.__attack + self.strenght)
        else:
            print(f"{self.name} lacked the rage...")
    def attack(self, other):
        other.takeDamage(self.__attack + (self.strenght/3))










