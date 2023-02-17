
class View:
    """
    initialization for object of View class.
    This stores the string of default chessboard consists of characters.
    substrings '[xx]' represents the location on board (e.g. '[64]' represents location = (6,4)).
    Traps and nests are marked by texts, and two river pools are marked by slashes.
    strings representing each animal chess and vacant places are stored for generating the chessboard according
    to players' status.

    return: None
    """

    def __init__(self):
        self.turn: int = 1

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
        |        |        | -TRAP- | -DEN-  | -TRAP- |        |        |
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
        |        |        | -TRAP- | -DEN-  | -TRAP- |        |        |
        |  [00]  |  [10]  |  [20]  |  [30]  |  [40]  |  [50]  |  [60]  |
        |________|________|________|________|________|________|________|

        """

    def printWelcomePage(self):
        """
            This function displays a welcome message in the interface before the game starts.
            The welcome message includes a welcome message, a brief introduction of the game
            information including version and developers.

            return: None
        """
        print("""
                  ____________________________________________
                  |\033[1;95m-WELCOME TO JUNGLE GAME DEVELOPED BY GRP3-\033[0m| 
                  |Type "help" if you need instructions anyt-|
                  |-ime during the game. Cheers and ENJOY!   |
                  |                                          |
                  |\033[37mGame Version: V22.11                      \033[0m|
                  |\033[37m(Last updated on Nov 17, 2022)            \033[0m|
                  |\033[37mDeveloper list:                           \033[0m|
                  |\033[37mPan Yalu, Qi Shihao, Wang Ming, Yu Fengkai\033[0m|
                  |\033[37m          (All rights reserved)           \033[0m|
                  --------------------------------------------    
        """)
    def printChessboard(self, player1: list, player2: list, turnflag):
        """
            generate the current board regarding two players' status as the parameter.
            each chess's location will be checked and replace() function will be called to replace the '[xx]' string on
            copied default chessboard with the chess string.
            finally, replace all the still-vacant places with vac_str '    ' and print it.

            return: None
        """
        if not turnflag:
            self.turn = 0
        _gameboard = self.gameboard
        for animal_i in player1:
            if not animal_i.status: continue
            repl_str = "[" + str(animal_i.position[0]) + str(animal_i.position[1]) + "]"
            # print(repl_str)
            if animal_i.rank == 7:
                _gameboard = _gameboard.replace(repl_str, '\033[1;93m' + self.lion_str + '\033[0m')
            elif animal_i.rank == 8:
                _gameboard = _gameboard.replace(repl_str, '\033[1;93m' + self.elephant_str + '\033[0m')
            elif animal_i.rank == 2:
                _gameboard = _gameboard.replace(repl_str, '\033[1;93m' + self.cat_str + '\033[0m')
            elif animal_i.rank == 5:
                _gameboard = _gameboard.replace(repl_str, '\033[1;93m' + self.leopard_str + '\033[0m')
            elif animal_i.rank == 3:
                _gameboard = _gameboard.replace(repl_str, '\033[1;93m' + self.dog_str + '\033[0m')
            elif animal_i.rank == 6:
                _gameboard = _gameboard.replace(repl_str, '\033[1;93m' + self.tiger_str + '\033[0m')
            elif animal_i.rank == 4:
                _gameboard = _gameboard.replace(repl_str, '\033[1;93m' + self.wolf_str + '\033[0m')
            else:
                _gameboard = _gameboard.replace(repl_str, '\033[1;93m' + self.rat_str + '\033[0m')

        for animal_i in player2:
            if not animal_i.status: continue
            repl_str = "[" + str(animal_i.position[0]) + \
                       str(animal_i.position[1]) + "]"

            if animal_i.rank == 7:
                _gameboard = _gameboard.replace(repl_str, '\033[1;94m' + self.lion_str + '\033[0m')
            elif animal_i.rank == 8:
                _gameboard = _gameboard.replace(repl_str, '\033[1;94m' + self.elephant_str + '\033[0m')
            elif animal_i.rank == 2:
                _gameboard = _gameboard.replace(repl_str, '\033[1;94m' + self.cat_str + '\033[0m')
            elif animal_i.rank == 5:
                _gameboard = _gameboard.replace(repl_str, '\033[1;94m' + self.leopard_str + '\033[0m')
            elif animal_i.rank == 3:
                _gameboard = _gameboard.replace(repl_str, '\033[1;94m' + self.dog_str + '\033[0m')
            elif animal_i.rank == 6:
                _gameboard = _gameboard.replace(repl_str, '\033[1;94m' + self.tiger_str + '\033[0m')
            elif animal_i.rank == 4:
                _gameboard = _gameboard.replace(repl_str, '\033[1;94m' + self.wolf_str + '\033[0m')
            else:
                _gameboard = _gameboard.replace(repl_str, '\033[1;94m' + self.rat_str + '\033[0m')
        _gameboard = _gameboard.replace("NN", str(turnflag if self.turn else turnflag + 1))
        print(_gameboard)

    def printHelp(self):
        """
            handle help request. classify the user's questions for the rules by requesting new inputs and print related
            instructions.
            return: None
        """
        helpMenu = """
                    -SELECT THE GAME INFO YOU WANT TO REFER-
        1. Rank of the chess    2. Square categories    3. Command guides
        4. JungleGame rule guide
        
        Enter your option: 
        """

        rankInfo = """
        _________________________________________________________________________
        |Name    Elephant  Lion    Tiger   Leopard   Wolf    Dog     Cat     Rat|
        |Rank    8         7       6       5         4       3       2       1  |
        |Chess   ELEP      LION    TIGE    LEOP      WOLF    DOG     CAT     RAT|
        -------------------------------------------------------------------------
        """

        squareInfo = """
         ________        ________        ________        ________       
        |        |      |////////|      | -DEN-  |      | -TRAP- |
        |        |      |////////|      |        |      |        |
        |________|      |++++++++|      |________|      |________|
         L A N D         W A T E R       D E N           T R A P
        """

        commandInfo = """
        -"move"
            You should match your input with the following format:
                \033[32mmove <animal_name> <direction>\033[0m (e.g. move lion left)
        -"jump"
            You should match your input with the following format:
                \033[32mjump <animal_name> <direction>\033[0m (e.g. jump wolf up)
        -"help"
            Obtain help information. Just type "help".
        -"defeat"
            Surrender to your opponent.
        -"exit"
            End the game.
        """

        ruleA = """
        \033[95m-Game rules for 8 kinds of animals-\033[0m
        1. Elephant(rank 8): 
            1) it can't move into the river;
            2) it can capture same/lower rank enemy except rat;
            3) it will be attacked by enemy rat if they are both in land;
            4) it will not be attacked by enemy rat if the Rat just came from the river.
        2. Lion(rank 7) or Tiger(rank 6):
            1) they can't move into the river, but can jump over the river (by "jump" command) ;
            when there is no rat in that river;
            2) they can capture same/lower rank enemy.
        3. Rat(rank 1):
            1) it can move into the river;
            2) it can capture enemy rat if they are both in land or river;
            3) it can capture enemy elephant if the rat original position is in land;
            It can't capture enemy elephant from river.
        4. Leopard(rank 5), Wolf(rank 4), Dog(rank 3) and Cat(rank 2):
            1) they can't move into the river;
            2) they can capture same/lower rank enemy.
        """

        ruleB = """
        \033[95m-Games rules for special positions-\033[0m
        1. Trap: An animal may capture any enemy in one of the player's trap squares regardless of rank.     
        2. Den: Any animal steps into the enemy's den first will declare their victory.
        3. Water: Only rats are allowed to step into the water zone. 
                  Animals except lions/tigers cannot jump across the water.
        4. Land: All animals are allowed to step by.
        """

        ruleC = """
        \033[95m-Games rules for winner-\033[0m
        1.  You win if your animal steps into the enemy's den!
        2.  Also, you win if all the enemy's animals are eliminated.
        """
        option = int(input(helpMenu))
        if option == 1:
            print(rankInfo)
        elif option == 2:
            print(squareInfo)
        elif option == 3:
            print(commandInfo)
        elif option == 4:
            option1 = str.lower(input("""
            a. What are the rules for each animal?
            b. What are the rules for each positions?
            c. How to win the game?
            
            Enter your option (a/b/c):
            """))
            if option1 == "a":
                print(ruleA)
            elif option1 == "b":
                print(ruleB)
            elif option1 == "c":
                print(ruleC)
            else:
                print("\033[31mInvalid help option.\033[0m")
        else:
            print("\033[31mInvalid help option.\033[0m")

    def printHints(self, hintNum):  # hintNum:
        """
            This function displays different kinds of hints according to different invalid movements made by players.
            The hintList stores all the hints in order, and an integer hintNum is required as parameters to determine
            which hint to print.
            return: None
        """
        hintsList = ["\033[31mCan't move to next step! The position is occupied by other animals.\033[0m",  # Hint1
                     "\033[31mCan't move to next step! You can't move to your side's den.\033[0m",  # Hint2
                     "\033[31mCan't jump over the river because a rat is blocking the way.\033[0m",  # Hint3
                     "\033[31mCan't jump! Only Tiger and Lion can jump.\033[0m",  # Hint4
                     "\033[31mCan't move into the river! Only rat can move into the river.\033[0m",  # Hint5
                     "\033[31mCan't move to next step since it's out of chessboard range.\033[0m",  # Hint6
                     "\033[31mCan't move! The piece is eliminated.\033[0m"  # hint 7
                     ]
        print(hintsList[hintNum])

    def printCurrentRoundInfo(self, turnflag):

        print("The current turn is for Player ", turnflag % 2 + 1, ".")


    def printGameResult(self, turnflag, defeat: bool, Exit: bool):
        """
            This function displays the game result after the game ends. It will print out a message declaring who is the
            winner, the total number of rounds and a goodbye message.

            return: None
        """
        if not Exit:
            print("\n", "Downside" if not turnflag % 2 else "Upside", "player wins the game!\n")
        if defeat:
            turnflag -= 1
        print("(Total number of rounds: ", turnflag + (1 - self.turn), ")")
        print("Have a good day and see you next time!:)")


if __name__ == "__main__":
    view = View()
