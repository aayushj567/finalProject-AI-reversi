# AI project to build a Reversi game board and play against a human player

# Import statements
import sys
import copy
import random
import time
import math
import numpy as np

# Class to represent a Reversi game board
class Reversi:
    def __init__(self):
        self.board = np.zeros((8,8), dtype=np.int)

        # Filling the board's start stae. 1 = white, -1 = black
        self.board[3][3] = 1
        self.board[3][4] = -1
        self.board[4][3] = -1
        self.board[4][4] = 1

        # setting the current player to black
        self.currentPlayer = -1

        # setting the game over flag to false
        self.gameOver = False
    
    # Function to print the board
    def printBoard(self):
        print("  0 1 2 3 4 5 6 7")
        for i in range(8):
            print(i, end=" ")
            for j in range(8):
                if self.board[i][j] == 1:
                    print("W", end=" ")
                elif self.board[i][j] == -1:
                    print("B", end=" ")
                else:
                    print("-", end=" ")
            print()