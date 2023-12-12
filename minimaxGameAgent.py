# A minimax agent to play Reversi

from reversiGameBoard import *
import random

class MinimaxGameAgent:
    def __init__(self, gameInstance, player):
        self.gameInstance = gameInstance
        self.player = player
        self.opponent = self.gameInstance.getOpponent(player)
        self.maxDepth = 3

    def getMove(self):
        bestMove = None
        bestScore = -1000000
        for move in self.gameInstance.getValidMoves(self.player):
            self.gameInstance.makeMove(move[0], move[1])
            score = self.minimax(self.maxDepth, False)
            self.gameInstance.undoMove(move[0], move[1])
            if score > bestScore:
                bestScore = score
                bestMove = move