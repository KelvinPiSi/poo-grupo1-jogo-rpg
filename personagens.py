class Personagem :
    def __init__(self,nome,lv=1,hp=100,energia=100):
        self.nome = nome
        self.__hp = hp
        self.__energia = energia
        self.__lv = lv

    @property
    def hp(self):
        return self.hp

    @property
    def energia(self):
        return self.energia

    @property
    def lv(self):
        return self.lv