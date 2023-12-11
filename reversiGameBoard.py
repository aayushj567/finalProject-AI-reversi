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
        self.ROWS = 8
        self.COLUMNS = 8
        self.board = np.zeros((self.COLUMNS, self.ROWS), dtype=int)

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
        for i in range(self.ROWS):
            print(i, end=" ")
            for j in range(self.COLUMNS):
                if self.board[i][j] == 0:
                    print(".", end=" ")
                elif self.board[i][j] == 1:
                    print("W", end=" ")
                else:
                    print("B", end=" ")
            print()

    # Function to check if a move is valid
    def isValid(self, row, column):
        # check if row column specified is within the board
        if row < 0 or row > 7 or column < 0 or column > 7:
            return False

        # if cell is ioccupied, return false as move is invalid
        if self.board[row][column] != 0:
            return False