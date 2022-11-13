import sys

import Game.Model.Model as model
from Game.View.View import View
from Game.Model.Squares import Animals as anim
import time

matchers = {
    "rat": 1,
    "cat": 2,
    "dog": 3,
    "wolf": 4,
    "leopard": 5,
    "tiger": 6,
    "lion": 7,
    "elephant": 8
}

"""
    1. Exception in program Processing
    2. how to define the ifEnd()
    3. call view
    4. change turnFlag to local variable
"""

class Controller:
    """
    initialization for objects of controller class
    return: None
    """

    def __init__(self, game_model: model.Model, game_view: View):
        self.gamer = None
        self.game_model = game_model
        self.game_view = game_view
        self.turnFlag: int = 0
        self.exit: bool = False

    def chooseSide(self) -> None:
        """
        since the upside and downside layer were already be initialized, so we directly
        modify turnFlag to decide who starts first
        """
        inputs: str = input("Please choose your preferred side: ")
        if inputs.lower() == "up":
            self.turnFlag = 1
        elif inputs.lower() == "down":
            self.turnFlag = 0
        else:
            print("You input the wrong command, please input 'up' or 'down'. ")
            return self.chooseSide()
        return

    def executeInput(self) -> None:
        while not self.exit:
            self.game_view.printChessboard(self.game_model.upAnimalList, self.game_model.downAnimalList)
            self.processing()
            self.turnFlag += 1

    def processing(self) -> int:
        """
        processor for commands (user input). A boolean flag of a player's turn will be received to judge whether it
        was the player's round. if move is selected, the function will check whether that was a legal move calling
        checkMove() and process the command; if help is selected, printHelp() from view.py will be called, printing out
        the rules and instructions for the game; if defeat is selected, admitDefeat() will be called, ending the game as
        the played claimed; if exit is selected, print and call Exit() to exit Jungle.py.
        return: None
        """
        self.gamer: list
        if not self.turnFlag % 2:
            self.gamer = self.game_model.downAnimalList
        else:
            self.gamer = self.game_model.upAnimalList

        inputs: list = input(
            "Please input your commands: ").split()
        if inputs[0] == "move" or inputs[0] == "jumpOver":
            moving = self.gamer[matchers[inputs[1].lower()]]
            if self.ifEnd(moving, inputs[1:]): self.finalPrint()
            potential = self.game_model.ifCanMove(moving, inputs[2], inputs[0])
            if not potential[0]:
                self.game_view.printHints(potential[1])
                return self.processing()

            if inputs == "move":
                self.game_model.move(moving, inputs[2])
            elif inputs == "jumpOver":
                self.game_model.jumpOver(moving, inputs[2])
            if self.game_model.if_new_position_has_enemy_that_can_be_eaten(moving):
                opponent: anim = self.game_model.get_same_position_enemy(moving)
                self.game_model.die(opponent)
            self.commandRecord(" ".join(inputs))
        elif inputs[0] == "help":
            self.game_view.printHelp()
        elif inputs[0].lower() == "defeat":
            self.AdmitDefeat()
        elif inputs[0].lower() == "exit":
            self.Exit()
            print("Bye~")
        else:
            Exception("Input wrong, system will stop")

    '''
    checkMove() checks whether a move of the chess has exceeded the border of the chessboard.
    the parameter cmd stores player's move command with 4 possible directions: l, r, down, up.
    The size of the board is 9*7 thus the vertical range should be [0, 8] and the horizontal should be [0, 6].
    return: A boolean variable identifying the move is legal or not
    '''

    def getHelp(self):
        """do we still need this?"""
        pass

    '''
    Function handling undo processes.
    If an undo request is confirmed by input "y", check the number of previous undos. If already done 3 times then the request will not be granted.
    If less than 3 times, ask for the other player's permission. If agreed, withdraw the player's move.
    return: a boolean variable for checking the an withdrawal was made.
    '''

    def commandRecord(self, inputs: str) -> None:
        with open(r"/History.txt", "a+") as file:
            file.write(inputs + "\n")
        return

    def finalPrint(self):
        self.game_view.printGameResult(self.turnFlag)
        self.game_view.printCapturedResult()
        sys.exit()

    '''
    function to handle the user's surrender request.
    return: a boolean variable.
    '''

    def AdmitDefeat(self):
        if input("you will admit your defeat and surrender to your opponent, please confirm again: ").lower() in ["y",
                                                                                                                  "yes"]:
            print("player ", 2 - (self.turnFlag % 2), " win this game! ")
            self.finalPrint()
        return

    '''
    Function to exit the game after having the players' final confirmation.
    return: None
    '''

    def Exit(self):
        print("""
        WARNING!!!
        Be aware that the whole system will immediately shut down and stopping recording, \n
        Game won't reserve your current status or any records except those has been written in history.txt file.
        """)
        if input("Confirm exit?").lower() in ["y", "yes"]:
            print("Have a good day and see you next time! :)")
            self.finalPrint()
        return

    '''
    return: a boolean variable judging whether the game ends.
    '''

    def returnOpponent(self, oneSide: anim) -> list:
        if oneSide.name[0:2].lower() == "up":
            return self.game_model.downAnimalList
        elif oneSide.name[0:2].lower() == "do":
            return self.game_model.upAnimalList

    '''
    Check whether one side of animals are dead
    '''

    def all_dead(self, moving) -> bool:
        opponent = self.returnOpponent(moving)
        aside: int = 0
        for val in opponent:
            aside += 1 if not val.status else 0
        return False if aside != 8 else True

    def ifEnd(self, moving: anim, inputs: list) -> None:
        """
        1. in den
        2. in side all dead
        """
        if self.game_model.if_in_opposite_den(moving, inputs[0], inputs[1]):
            self.exit = True
        elif self.all_dead(moving):
            self.exit = True

    '''
    Count the time for current user's round with the limit of 60 seconds.
    return type: None
    '''

    def time_spire(self):
        available_second = 60
        for i in range(1, available_second):
            print('you have %d seconds' % (available_second - i))
            if available_second - i == 10:
                print("10 seconds left.")
        print("Time expired, your turn finished.")
        time.sleep(1)  # 时间倒计时
