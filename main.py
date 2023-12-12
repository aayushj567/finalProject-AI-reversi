# entrypoint for the reversi board game
from reversiGameBoard import *

def main():
    gameInstance = Reversi()
    gameInstance.printBoard()
    while not gameInstance.gameOver:
        print("Enter your move below")
        row = int(input("Enter row :"))
        column = int(input("Enter column :"))
        gameInstance.makeMove(row, column)
        gameInstance.printBoard()

if __name__ == "__main__":
    main()