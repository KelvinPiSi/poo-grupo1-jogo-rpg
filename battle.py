from time import sleep

from character import Character

def battle(char1: Character, char2: Character):
    """Inicia a batalha entre personagens escolhidos na main.py
    Cada turno realiza uma sequência de ações determinadas
    char 1 ataca primeiro, char 2 ataca após char 1.
    Repete esse loop até que um deles morra, então declara o vencedor"""
    print(f"Vamos começar a batalha!\n\t{char1.name} vs {char2.name}:")
    sleep(5)
    turn = 1
    while char1.getHeartPoints > 0 and char2.getHeartPoints > 0:
        print(f"-=-=-=-=-={turn}º turno=-=-=-=-=-\n{char1.__str__()}\n{char2.__str__()}")
        sleep(3)
        print(f"{char1.name} ataca:")
        char1.attack(char2)
        sleep(2)
        print(f"{char2.name} ataca:")
        char2.attack(char1)
        sleep(2)
        turn += 1
    if char1.getHeartPoints > 0:
        print(f"{char1.name} o {char1.role} venceu!")
    else:
        print(f"{char2.name} o {char2.role} venceu!")