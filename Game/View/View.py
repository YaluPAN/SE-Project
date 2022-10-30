import sys
import os
from Game.Model import Model


class View():
    def printWelcomePage():
        print()

    def askPreference():
        print()

    def printChessboard(player1: Model.Players, player2: Model.Players):
        print()

    def printHelp():
        print()

    def printHints():
        print()

    def printTiming():
        print()

    def printMoveHistory():
        print()

    def printCurrentRoundInfo():
        print()

    def printCapturedResult():
        capturedResult = Model.getCapturedResult()
        print(capturedResult)

    def printGameResult():
        print()


if __name__ == "__main__":
    view = View()
    view.printChessboard()
