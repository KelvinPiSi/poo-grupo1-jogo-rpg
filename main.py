from character import Character
from guerreiro import Guerreiro
from arqueiro import Arqueiro
from mago import Mago
from battle import battle

def choseCharacter() -> Character:
    option = input("1 - Guerreiro\n2 - Arqueiro\n3 - Mago\n-> ")
    name = input("Qual será o nome dele? ")
    match option:
        case "1":
            return Guerreiro(name, 50, 25, 200, 100)
        case "2":
            return Arqueiro(name, 30, 20, 100, 150, 100)
        case "3":
            return Mago(name, 25, 15, 80, 80, 120)
        case "_":
            print("Escolha um valor válido na próxima")
            return Character(name, 0, 0, 1, 1)



print("Jogador 1, escolha seu personagem:\n")
player1 = choseCharacter()
print("Jogador 2, escolha seu personagem:\n")
player2 = choseCharacter()

battle(player1, player2)