import sys
import os

from Model import Model
import Chess

class View():
    def __init__(self):
        self.lion_str = "LION"
        self.wolf_str = "WOLF"
        self.mice_str = "MICE"
        self.puma_str = "PUMA"
        self.cat_str  = "CAT "
        self.dog_str  = "DOG "
        self.vac_str  = "    "

        self.gameboard = """
                                    -ROUND NN-
        ________________________________________________________________
        |        |        | -TRAP- | -NEST- | -TRAP- |        |        |
        |  [08]  |  [18]  |  [28]  |  [38]  |  [48]  |  [58]  |  [68]  |
        |________|________|________|________|________|________|________|
        |        |        |        | -TRAP- |        |        |        |
        |  [07]  |  [17]  |  [27]  |  [37]  |  [47]  |  [57]  |  [67]  |
        |________|________|________|________|________|________|________|
        |        |        |        |        |        |        |        |
        |  [06]  |  [16]  |  [26]  |  [36]  |  [46]  |  [56]  |  [66]  |
        |________|________|________|________|________|________|________|
        |        |////////|////////|        |////////|////////|        |
        |  [05]  |//[15]//|//[25]//|  [35]  |//[45]//|//[55]//|  [65]  |
        |________|++++++++|++++++++|________|++++++++|++++++++|________|
        |        |////////|////////|        |////////|////////|        |
        |  [04]  |//[14]//|//[24]//|  [34]  |//[44]//|//[54]//|  [64]  |
        |________|++++++++|++++++++|________|++++++++|++++++++|________|
        |        |////////|////////|        |////////|////////|        |
        |  [03]  |//[13]//|//[23]//|  [33]  |//[43]//|//[53]//|  [63]  |
        |________|++++++++|++++++++|________|++++++++|++++++++|________|
        |        |        |        |        |        |        |        |
        |  [02]  |  [12]  |  [22]  |  [32]  |  [42]  |  [52]  |  [62]  |
        |________|________|________|________|________|________|________|
        |        |        |        | -TRAP- |        |        |        |
        |  [01]  |  [11]  |  [21]  |  [31}  |  [41]  |  [51]  |  [61]  |
        |________|________|________|________|________|________|________|
        |        |        | -TRAP- | -NEST- | -TRAP- |        |        |
        |  [00]  |  [10]  |  [20]  |  [30]  |  [40]  |  [50]  |  [60]  |
        |________|________|________|________|________|________|________|

        """

    def printWelcomePage():
        print("        WELCOME TO JUNGLE GAME DEVELOPED BY GRP3        ")

    def askPreference():
        print()
#
    def printChessboard(player1: Model.Players, player2: Model.Players):
        _gameboard = self.gameboard
        for animal_i in player1:
            repl_str = "[" + str(animal_i.position[0]) + str(animal_i.position[1]) + "]"
            if(isinstance(animal_i, Lion)): 
                _gameboard.replace(repl_str, self.lion_str)
            elif(isinstance(animal_i, )): 
                _gameboard.replace(repl_str, self.lion_str)
            elif(isinstance(animal_i, Lion)): 
                _gameboard.replace(repl_str, self.lion_str)
            elif(isinstance(animal_i, Lion)): 
                _gameboard.replace(repl_str, self.lion_str)
            elif(isinstance(animal_i, Lion)): 
                _gameboard.replace(repl_str, self.lion_str)
            elif(isinstance(animal_i, Lion)): 
                _gameboard.replace(repl_str, self.lion_str)
            
        print(_gameboard)

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
