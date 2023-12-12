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

        self.captured = False

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

    # function to switch the current player
    def switchPlayer(self):
        self.currentPlayer = self.currentPlayer * -1

    # Function to check if a move is valid
    def isValid(self, row, column):
        # check if row column specified is within the board
        if row < 0 or row > 7 or column < 0 or column > 7:
            return False

        # if cell is ioccupied, return false as move is invalid
        if self.board[row][column] != 0:
            return False

    # function to capture and flip flanked pieces to the left/west of the placed piece
    def captureWest(self, row, column):
        try:
            if (self.board[row][column - 1] == self.currentPlayer * -1) and (column > 1):
                for i in range(column - 2, -1, -1): # start at two cells left, go down to 0, step count -1
                    try:
                        if self.board[row][i] == self.currentPlayer:
                            for j in range(i+1, column):
                                self.board[row][j] = self.board[row][j] * -1
                            self.captured = True
                            break
                        elif self.board[row][i] == 0:
                            break
                    except Exception as f:
                        print(f)
        except Exception as e:
            print(e)

        
    # function to capture and flip flanked pieces to the right/east of the placed piece
    def captureEast(self, row, column):
        try:
            if (self.board[row][column + 1] == self.currentPlayer * -1) and (column < 6):
                for i in range(column + 2, 8):
                    try:
                        if self.board[row][i] == self.currentPlayer:
                            for j in range(column + 1, i):
                                self.board[row][j] = self.board[row][j] * -1
                            self.captured = True
                            break
                        elif self.board[row][i] == 0:
                            break
                    except Exception as f:
                        print(f)
        except Exception as e:
            print(e)


    # function to capture and flip flanked pieces to the top/north of the placed piece
    def captureNorth(self, row, column):
        try:
            if (self.board[row - 1][column] == self.currentPlayer * -1) and (row > 1):
                for i in range(row - 2, -1, -1):
                    try:
                        if self.board[i][column] == self.currentPlayer:
                            for j in range(i+1, row):
                                self.board[j][column] = self.board[j][column] * -1
                            self.captured = True
                            break
                        elif self.board[i][column] == 0:
                            break
                    except Exception as f:
                        print(f)
        except Exception as e:
            print(e)
        
    
    # function to capture and flip flanked pieces to the bottom/south of the placed piece
    def captureSouth(self, row, column):
        try:
            if (self.board[row + 1][column] == self.currentPlayer * -1) and (row < 6):
                for i in range(row + 2, 8):
                    try:
                        if self.board[i][column] == self.currentPlayer:
                            for j in range(row + 1, i):
                                self.board[j][column] = self.board[j][column] * -1
                            self.captured = True
                            break
                        elif self.board[i][column] == 0:
                            break
                    except Exception as f:
                        print(f)
        except Exception as e:
            print(e)


    # function to keep count of number of pieces for each player
    def countPieces(self):
        whiteCount = 0
        blackCount = 0
        for i in range(self.ROWS):
            for j in range(self.COLUMNS):
                if self.board[i][j] == 1:
                    whiteCount += 1
                elif self.board[i][j] == -1:
                    blackCount += 1
        return (whiteCount, blackCount)


    # function to make a valid move on the board
    def makeMove(self, row, column):
        # check if move is valid
        if not self.isValid(row, column):
            print("Invalid move")
            return False

        whiteCountBefore, blackCountBefore = self.countPieces()
        self.captureEast(row, column)
        self.captureWest(row, column)
        self.captureNorth(row, column)
        self.captureSouth(row, column)

        if self.captured:
            self.board[row][column] = self.currentPlayer
            self.captured = False
            self.switchPlayer()

        # check if game is over
        self.checkGameOver()

        return True