import random

from game import Player, Move


selection = {
    "a": Move(1, "Attack"),
    "b": Move(2, "Block"),
    "g": Move(4, "Grab"),
    "dp": Move(8, "Dragon Punch")
}

class ManualPlayer(Player):
    name = ""
    def __init__(self, name: str = "Manuel"):
        self.name = name
    
    def act(self, own_blocks: int, other_blocks: int, own_has_attack: bool, other_has_attack: bool, rounds_left: int) -> Move:
        print(f"Your turn, {self.name}!{f' {rounds_left} rounds left.' if rounds_left > -1 else ''}")
        print(f"You have {own_blocks} blocks left{' and have landed an attack' if own_has_attack else ''}.")
        print(f"Your opponent has {other_blocks} blocks left{' and has landed an attack' if other_has_attack else ''}.")
        
        move_str = ""
        while move_str not in selection:
            move_str = input("Choose your move: ")

        return selection[move_str]
    
class RandomPlayer(Player):
    name = "Random"

    def act(self, own_blocks: int, other_blocks: int, own_has_attack: bool, other_has_attack: bool, rounds_left: int) -> Move:
        return random.choice(list(selection.values()))