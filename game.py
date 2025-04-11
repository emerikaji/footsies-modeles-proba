from abc import ABC,abstractmethod
from dataclasses import dataclass

class Move:
    def __init__(self, value: int, name: str):
        self.value = value
        self.name = name

@dataclass
class State:
    other_previous_move: Move
    own_blocks: int
    other_blocks: int
    own_has_attack: bool
    other_has_attack: bool
    turns_left: int

MoveSelection = {
    "a": Move(1, "Attack"),
    "b": Move(2, "Block"),
    "g": Move(4, "Grab"),
    "dp": Move(8, "Dragon Punch")
}

class Player(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def act(self, game_state: State) -> Move:
        pass

class Footsies:
    def __init__(self, player1: Player, player2: Player, rounds: int = 3, blocks: int = 3, attackstowin: int = 2, timeout: int = 0):
        self.p1 = player1
        self.p2 = player2
        self.rounds = rounds
        self.attacks = attackstowin

        self.p1_blocks = blocks
        self.p2_blocks = blocks
        self.p1_has_attack = False
        self.p2_has_attack = False
        self.p1_victories = 0
        self.p2_victories = 0
        self.p1_previous: Move = None
        self.p2_previous: Move = None

        self.timeout = False
        self.timeout_turns = 0
        self.current_round = 1
        if timeout > 0:
            self.timeout = True
            self.timeout_turns = timeout
            self.current_round = 0

    def start(self) -> int:
        '''Starts the game loop until all rounds are over. Returns the number of the player that won or 0. '''
        
        def no_timeout():
            return True

        def timeout():
            self.current_round += 1
            print(f"Turn {self.current_round}/{self.timeout_turns}")
            return self.current_round <= self.timeout_turns

        condition = None
        if self.timeout:
            condition = timeout
        else:
            condition = no_timeout

        for _ in range(self.rounds):
            while condition():
                turns_left = self.timeout_turns - self.current_round
                p1_state = State(self.p2_previous, self.p1_blocks, self.p2_blocks, self.p1_has_attack, self.p2_has_attack, turns_left)
                p2_state = State(self.p1_previous, self.p2_blocks, self.p1_blocks, self.p2_has_attack, self.p1_has_attack, turns_left)
                move1 = self.p1.act(p1_state)
                move2 = self.p2.act(p2_state)
                self.p1_previous = move1
                self.p2_previous = move2

                print(f"{self.p1.name} chose {move1.name}. {self.p2.name} chose {move2.name}.")

                p1_hit_attack = False
                p2_hit_attack = False
                p1_win = False
                p2_win = False

                match (move1.value - move2.value):
                    case 0:
                        print("Same option chosen!")
                    case 1:
                        print("Player 1 blocks a hit!")
                        self.p1_blocks -= 1
                    case -1:
                        print("Player 2 blocks a hit!")
                        self.p2_blocks -= 1
                    case 2:
                        print("Player 2 gets thrown!")
                        p1_win = True
                    case -2:
                        print("Player 1 gets thrown!")
                        p2_win = True
                    case 3:
                        print("Player 2 lands a hit!")
                        if self.p2_has_attack:
                            p2_win = True
                        p2_hit_attack = True
                    case -3:
                        print("Player 1 lands a hit!")
                        if self.p1_has_attack:
                            p1_win = True
                        p1_hit_attack = True
                    case 6:
                        print("Player 2 blocks the Dragon Punch and counters!")
                        p2_win = True
                    case -6:
                        print("Player 1 blocks the Dragon Punch and counters!")
                        p1_win = True
                    case _:
                        if move1.value > move2.value:
                            print("Player 1 lands a Dragon Punch!")
                            p1_win = True
                        else:
                            print("Player 2 lands a Dragon Punch!")
                            p2_win = True

                self.p1_has_attack = p1_hit_attack
                self.p2_has_attack = p2_hit_attack

                if p2_win:
                    print("Player 2 wins the round.")
                    self.p2_victories += 1
                    break

                if p1_win:
                    print("Player 1 wins the round.")
                    self.p1_victories += 1
                    break
                
        if self.p1_victories > self.p2_victories:
            return 1
        elif self.p2_victories > self.p1_victories:
            return 2
        
        return 0