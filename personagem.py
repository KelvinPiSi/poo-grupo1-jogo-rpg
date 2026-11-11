from __future__ import annotations

class Character :
    def __init__(self, name, heartPoints, staminaPoints, attack, defense, level=1):
        self.name = name
        self.__heartPoints = heartPoints
        self.__maximumHP = heartPoints
        self.__staminaPoints = staminaPoints
        self.__maximumSP = staminaPoints
        self.__attack = attack
        self.__defense = defense
        self.__level = level

    def description(self, role: str):
        return (f"{self.name} o {role} - Lv {self.__level}:\n\tHP: {self.__heartPoints}/100\n\t"
                f"SP: {self.__staminaPoints}/100\n\tATK: {self.__attack}\n\tDEF: {self.__defense}")

    @property
    def getHeartPoints(self):
        return self.__heartPoints

    @property
    def getStaminaPoints(self):
        return self.__staminaPoints

    @property
    def getLevel(self):
        return self.__level