from game import Footsies
from players import *

def main():
	player1 = ManualPlayer()
	player2 = RandomPlayer()
	game = Footsies(player1, player2)
	print(game.start())

if __name__ == "__main__":
	main()