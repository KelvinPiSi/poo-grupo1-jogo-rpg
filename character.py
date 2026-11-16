from __future__ import annotations

class Character :
    def __init__(self, name, attack, defense, maxHeartPoints=100, maxStaminaPoints=100):
        self.name = name
        self.role = "none"
        self.__heartPoints = maxHeartPoints
        self.__maxHeartPoints = maxHeartPoints
        self.__staminaPoints = maxStaminaPoints
        self.__maxStaminaPoints = maxStaminaPoints
        self.__attack = attack
        self.__defense = defense
        self.__level = 1

    def __str__(self) -> str:
        return f"{self.name} o {self.role} - Level {self.__level}:\n\t{self.__heartPoints}/{self.__maxHeartPoints}HP\n\t{self.__staminaPoints}/{self.__staminaPoints}SP\n\tAtaque: {self.__attack}\n\tDefesa: {self.__defense}"

    def takeDamage(self, damage):
        if damage < self.__defense:
            self.__heartPoints -= 1
        else:
            self.__heartPoints -= damage - self.__defense
        
    def heal(self, value):
        self.__heartPoints += value

    def attack(self, other):
        other.takeDamage(self.__attack)
        
    def levelUp(self):
        self.__level += 1 #++ n funca
        self.__maxHeartPoints *= 1.05
        self.__heartPoints = self.__maxHeartPoints
        self.__maxStaminaPoints *= 1.05
        self.__staminaPoints = self.__maxStaminaPoints
        self.__attack *= 1.1
        self.__defense *= 1.1
    
    @property
    def getHeartPoints(self):
        return self.__heartPoints

    @property
    def getStaminaPoints(self):
        return self.__staminaPoints

    @property
    def getAttack(self):
        return self.__attack

    @property
    def level(self):
        return self.__level