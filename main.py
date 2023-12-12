# entrypoint for the reversi board game
from reversiGameBoard import *

def main():
    gameInstance = Reversi()
    gameInstance.printBoard()
    while not gameInstance.isGameOver():
        print(f"---------------------------------{gameInstance.getCurentPlayerString()}'s turn---------------------------------")
        print("Enter your move below")
        row = int(input("Enter row :"))
        column = int(input("Enter column :"))
        gameInstance.makeMove(row, column)
        gameInstance.printBoard()

def testDiagonalMoves():
    gameInstance = Reversi()
    gameInstance.printBoard()
    gameInstance.makeMove(3,2)
    gameInstance.printBoard()
    gameInstance.makeMove(2,4)
    gameInstance.printBoard()
    gameInstance.makeMove(4,5)
    gameInstance.printBoard()
    gameInstance.makeMove(5,2)
    gameInstance.printBoard()
    gameInstance.makeMove(5,4)
    gameInstance.printBoard()
    gameInstance.makeMove(4,2)
    gameInstance.printBoard()
    gameInstance.makeMove(1,4)
    gameInstance.printBoard()
    gameInstance.makeMove(2,5)
    gameInstance.printBoard()
    gameInstance.makeMove(6,2)
    gameInstance.printBoard()
    gameInstance.makeMove(5,5)
    gameInstance.printBoard()
    gameInstance.makeMove(1,6)
    gameInstance.printBoard()
    gameInstance.makeMove(4,1)
    gameInstance.printBoard()
    gameInstance.makeMove(5,1)
    gameInstance.printBoard()
    gameInstance.makeMove(0,4)
    gameInstance.printBoard()
    gameInstance.makeMove(5,6)
    gameInstance.printBoard()
    gameInstance.makeMove(6,7)
    gameInstance.printBoard()
    gameInstance.makeMove(4,6)
    gameInstance.printBoard()
    gameInstance.makeMove(6,1)
    gameInstance.printBoard()

if __name__ == "__main__":
    #main()
    testDiagonalMoves()