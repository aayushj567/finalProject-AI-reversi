# entrypoint for the reversi board game
from reversiGameBoard import *

def main():
    gameInstance = Reversi()
    gameInstance.printBoard()

if __name__ == "__main__":
    main()