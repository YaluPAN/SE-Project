import sys

import Game.Model.Model as model
from Game.View.View import View
from Game.Model.Squares import Animals as anim

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
            self.game_view.printChessboard(self.game_model.upAnimalList, self.game_model.downAnimalList, self.turnFlag)
            print("Now is", "down side" if not self.turnFlag % 2 else "up side", "player turn")
            self.processing()
            self.turnFlag += 1
        self.finalPrint(False, False)

    def wordProcess(self, inputs: list) -> bool:
        if inputs[1].lower() not in matchers.keys() or inputs[2].lower() not in ["left", "right", "up", "down"]:
            return False
        return True

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
        if inputs[0] == "move" or inputs[0] == "jump":
            if not self.wordProcess(inputs):
                print("Please correctly spell the words.")
                return self.processing()
            direction, action = inputs[2], inputs[0]
            moving = self.gamer[matchers[inputs[1].lower()] - 1]
            if self.ifEnd(moving, direction, action): self.finalPrint(False, False)
            potential = self.game_model.ifCanMove(moving, direction, action)
            if not potential[0]:
                self.game_view.printHints(potential[1] - 1)
                return self.processing()

            if inputs[0] == "move":
                self.game_model.move(moving, direction)
            elif inputs[0] == "jump":
                self.game_model.jumpOver(moving, direction)
            if self.game_model.if_new_position_has_enemy_that_can_be_eaten(moving, direction, action):
                opponent: anim = self.game_model.get_same_position_enemy(moving)
                self.game_model.die(opponent)
        elif inputs[0] == "help":
            self.game_view.printHelp()
        elif inputs[0].lower() == "defeat":
            self.AdmitDefeat()
        elif inputs[0].lower() == "exit":
            self.Exit()
            print("Bye~")
        else:
            print("Hey player, please do not arbitrarily input, OK? you are playing game. please input again!")
            return self.processing()

    def finalPrint(self, defeat: bool, exit: bool):
        self.game_view.printGameResult(self.turnFlag, defeat, exit)
        sys.exit()

    def AdmitDefeat(self):
        """
        function to handle the user's surrender request.
        return: a boolean variable.
        """
        if input("\nyou will admit your defeat and surrender to your opponent, please confirm again:\n ").lower() in [
            "y", "yes"]:
            self.turnFlag += 1
            self.finalPrint(True, False)
        return

    def Exit(self):
        """
        Function to exit the game after having the players' final confirmation.
        return: None
        """
        print("""
        WARNING!!!
        Be aware that the whole system will immediately shut down and stopping recording,
        Game won't reserve your current status or any records except those has been written in history.txt file.
        """)
        if input("Confirm exit?[yes or no]\n").lower() in ["y", "yes"]:
            print("\nHave a good day and see you next time! :)")
            self.finalPrint(False, True)
        return

    def returnOpponent(self, oneSide: anim) -> list:
        """
        return: a boolean variable judging whether the game ends.
        """
        if oneSide.name[0:2].lower() == "up":
            return self.game_model.downAnimalList
        elif oneSide.name[0:2].lower() == "do":
            return self.game_model.upAnimalList

    def all_dead(self, moving) -> bool:
        """
        Check whether one side of animals are dead
        """

        opponent = self.returnOpponent(moving)
        aside: int = 0
        for val in opponent:
            aside += 1 if not val.status else 0
        return False if aside != 8 else True

    def ifEnd(self, moving: anim, direction: str, action: str) -> None:
        """
        1. in den
        2. in side all dead
        """
        if self.game_model.if_in_opposite_den(moving, direction, action):
            self.exit = True
        elif self.all_dead(moving):
            self.exit = True
