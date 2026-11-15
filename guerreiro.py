from personagem import Personagem


class Guerreiro(Personagem):
    def __init__(self, nome, hp, energia, lv, forca=5):
        super().__init__(self, nome, lv, hp, energia)

        self.forca = forca
        self.ataque = self.forca + 10

    def atacar(self):
        if self.energia > 5:
            print(f"{self.nome} atacou e causou {self.ataque} de dano")
            self.energia -= 10
        else:
            print(f"{self.nome} tentou atacar...\nFalhou pois faltou energia")
    def auto_cura(self):
        if self.energia > 50 and self.hp > 0:
            print(f"{self.name} usou auto cura!\nRegenerou 20 pontos de vida")
            self.hp += 20
            self.energia -= 50
        else:
            print(f"{self.name} tentou recuperar vida...\nFalhou pois faltou energia")
    def resistencia(self):
        if self.hp > 0 and self.energia > 30:
            print(f"{self.name} se preparou para o proxímo ataque...")







