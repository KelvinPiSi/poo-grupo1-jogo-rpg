from __future__ import annotation

class Personagem :
    def __init__(self, nome, attack, defense, maxHeratPoints=100, maxStaminaPoints=100, ):
        self.nome = nome
        self.__heartPoints = maxHeratPoints
        self.__maxHeartPoints = maxHeratPoints
        self.__staminaPoints = maxStaminaPoints
        self.__maxStaminaPoints = maxStaminaPoints
        self.__attack = attack
        self.__defense = defense
        self.__level = 1

    def takeDamage(self, damage):
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
    def level(self):
        return self.__level