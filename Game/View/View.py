import sys
import os

from Game.Model.Model import Model



class View():
    """
    initialization for object of View class.
    This stores the string of default chessboard consists of characters.
    substrings '[xx]' represents the location on board (e.g. '[64]' represents location = (6,4)).
    Traps and nests are marked by texts, and two river pools are marked by slashes.
    strings representing each animal chess and vacant places are stored for generating the chessboard according to players' status.

    return: None
    """

    def __init__(self):
        self.lion_str = "LION"
        self.wolf_str = "WOLF"
        self.rat_str = "RAT "
        self.leopard_str = "LEOP"
        self.cat_str = "CAT "
        self.dog_str = "DOG "
        self.tiger_str = "TIGE"
        self.elephant_str = "ELEP"
        self.vac_str = "    "

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
        |  [01]  |  [11]  |  [21]  |  [31]  |  [41]  |  [51]  |  [61]  |
        |________|________|________|________|________|________|________|
        |        |        | -TRAP- | -NEST- | -TRAP- |        |        |
        |  [00]  |  [10]  |  [20]  |  [30]  |  [40]  |  [50]  |  [60]  |
        |________|________|________|________|________|________|________|

        """

    '''
    This function displays a welcome message in the interface before the game sta
    ts. The welcome message includes a welcome sentence, a system brief introduction
    on, a game rules description, and a brief user manual. 
    
    return: None
    '''

    def printWelcomePage(self):
        print("        WELCOME TO JUNGLE GAME DEVELOPED BY GRP3        ")

    def askPreference(self):
        print()

    '''
    generate the current board regarding to two players' status as the parameter.
    each chess's location will be checked and replace() function will be called to replace the '[xx]' string on copied default chessboard with the chess string.
    finally, relpace all the still-vacant places with vac_str '    ' and print it.
    
    return: None
    '''

    def printChessboard(self, player1: list, player2: list):
        _gameboard = self.gameboard
        for animal_i in player1:
            repl_str = "[" + str(animal_i.position[0]) + str(animal_i.position[1]) + "]"
            #print(repl_str)
            if (animal_i.rank == 7):
                _gameboard = _gameboard.replace(repl_str, '\033[93m' + self.lion_str + '\033[0m')
            elif (animal_i.rank == 8):
                _gameboard = _gameboard.replace(repl_str, '\033[93m' + self.elephant_str + '\033[0m')
            elif (animal_i.rank == 2):
                _gameboard = _gameboard.replace(repl_str, '\033[93m' + self.cat_str + '\033[0m')
            elif (animal_i.rank == 5):
                _gameboard = _gameboard.replace(repl_str, '\033[93m' + self.leopard_str + '\033[0m')
            elif (animal_i.rank == 3):
                _gameboard = _gameboard.replace(repl_str, '\033[93m' + self.dog_str + '\033[0m')
            elif (animal_i.rank == 6):
                _gameboard = _gameboard.replace(repl_str, '\033[93m' + self.tiger_str + '\033[0m')
            elif (animal_i.rank == 4):
                _gameboard = _gameboard.replace(repl_str, '\033[93m' + self.wolf_str + '\033[0m')
            else:
                _gameboard = _gameboard.replace(repl_str, '\033[93m' + self.rat_str + '\033[0m')

        for animal_i in player2:
            repl_str = "[" + str(animal_i.position[0]) + \
                str(animal_i.position[1]) + "]"

            if (animal_i.rank == 7):
                _gameboard = _gameboard.replace(repl_str, '\033[94m' + self.lion_str + '\033[0m')
            elif (animal_i.rank == 8):
                _gameboard = _gameboard.replace(repl_str, '\033[94m' + self.elephant_str + '\033[0m')
            elif (animal_i.rank == 2):
                _gameboard = _gameboard.replace(repl_str, '\033[94m' + self.cat_str + '\033[0m')
            elif (animal_i.rank == 5):
                _gameboard = _gameboard.replace(repl_str, '\033[94m' + self.leopard_str + '\033[0m')
            elif (animal_i.rank == 3):
                _gameboard = _gameboard.replace(repl_str, '\033[94m' + self.dog_str + '\033[0m')
            elif (animal_i.rank == 6):
                _gameboard = _gameboard.replace(repl_str, '\033[94m' + self.tiger_str + '\033[0m')
            elif (animal_i.rank == 4):
                _gameboard = _gameboard.replace(repl_str, '\033[94m' + self.wolf_str + '\033[0m')
            else:
                _gameboard = _gameboard.replace(repl_str, '\033[94m' + self.rat_str + '\033[0m')

        print(_gameboard)

    '''
    handle help request. classify the user's questions for the rules by requesting new inputs and print related instructions.
    return: None
    '''

    def printHelp(self):
        helpMenu = """
                        -SELECT THE GAME INFO YOU WANT TO REFER-
        1. Rank of the chess    2. Square categories    3. 
        Enter your option: 
        """

        rankInfo = """
        _____________________________________________________________________
        |Rank    8       7       6       5       4       3       2       1  |
        |Piece   ELEP    LION    TIGE    LEOP    WOLF    DOG     CAT     RAT|
        ---------------------------------------------------------------------
        """

        squareInfo = """
         ________        ________        ________        ________       
        |        |      |////////|      | -NEST- |      | -TRAP- |
        |        |      |////////|      |        |      |        |
        |________|      |++++++++|      |________|      |________|
         L A N D        W A T E R        N E S T         T R A P
        """
        option = input(helpMenu)
        if (option == 1):
            print(rankInfo)
        elif (option == 2):
            print(squareInfo)

    '''
    This function displays different kinds of hints according to different invalid movements made by players. 
    The hintList stores all the hints in order, and an integer hintNum is required as parameters to determine which hint to print.
    return: None
    '''

    def printHints(self, hintNum):  # hintNum:
        hintsList = [" Can't move to next step since it's out of chessboard range",  # Hint1
                     " Can't move to next step since it's occupied by your side's animals",  # Hint2
                     " Can't move to next step since it's occupied by higher rank enemy",  # Hint3
                     " The rat can't move to next step since the square is occupied by enemy rat",  # Hint4
                     " The elephant can't move to next step since the square is occupied by enemy rat",  # Hint5
                     " Elephant(8), Leopard(5), Wolf(4), Dog(3), Cat(2) can't move into the river", # Hint6
                     " Lion(7), Tiger(6) can't move across the river since there is a rat in the river now",  # Hint7
                     " Can't move to next step since it's your side's den ",  # Hint8
                     " The animal can move to next step (successful hint)"]  # Hint9
        print(hintsList[hintNum])

    '''
    This function displays a real-time countdown second during a player’s movement decision period. 
    The game is designed to be time-limited, as this enhances player focus and improves the sense of involvement in the game.

    return: None

    '''

    def printTiming(self):

        print()

    '''
    This function displays a player’s chess move hist
    ory, including which chess is chosen to move, how it moves,s and its captured results (if it h
    as). The function is used once the player wants to review his/her movement strategy during the 
    game.
    return: None
    '''

    def printMoveHistory(self):

        print()

    '''
    This function displays the current round number in each round of the game. 
    It’s an additional function that aims to provide a better view of chess competitions.
    
    return: None
    '''

    def printCurrentRoundInfo(self, turnflag):

        print("The current turn is for Player ", turnflag % 2 + 1, ".")

    '''
    This function displays a list of captured results in the current round when a player is making a movement decisio
    n. It provides a review so that players can know what his/her has captured instead of spending time observing the chessboard.
    
    return: None
    '''

    def printCapturedResult(self):
        capturedResult = Model.getCapturedResult()
        print(capturedResult)

    '''
    This function displays the game result about which player wins the game at the end of the game. 

    return: None
    '''

    def printGameResult(self, turnflag):

        print("Player ", turnflag % 2 + 1, "wins the game!")
        print("Total number of rounds: ", turnflag)


if __name__ == "__main__":
    view = View()
    view.printChessboard()
