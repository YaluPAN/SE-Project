import sys

from Game.Model import Players as player
import Game.Model.Model as model
from Game.View import View
import time


class Controller:

    def __init__(self, game_model: model.Model, game_view: View):
        self.game_model = game_model
        self.game_view = game_view

    def chooseLanguage(self):
        inputs: str = input(
            "Please choose your language preference(Chinese or English), and color (Green or Blue): ")
        if inputs == "chinese":
            pass

        elif inputs == "english":
            pass

    def chooseSide(self) -> list:
        """
        so after choosing the side, two player list should with a signature to be pointed and able
        to be recognized.
        Major related function should get from Model.Model
        :return: None
        """
        inputs: str = input("Please choose your preferred side: ")  # how is choosing?
        receiver: list = model.Model.getChessboard()
        riverpos: list = [(x, y) for x in [1, 2, 4, 5] for y in range(3, 6)]
        trappos: list = [(2, 0), (3, 1), (4, 0), (2, 8), (3, 7), (4, 8)]
        denpos: list = [(3, 0), (3, 8)]
        if inputs == "down":  # {"down" : Player1}
            receiver[0] = player.Players(chessList=[], riverPos=riverpos, trapPos=trappos[0:3], denPos=denpos[0])
            receiver[1] = player.Players(chessList=[], riverPos=riverpos, trapPos=trappos[3:6], denPos=denpos[1])
        elif inputs == "up":
            receiver[1] = player.Players(chessList=[], riverPos=riverpos, trapPos=trappos[0:3], denPos=denpos[0])
            receiver[0] = player.Players(chessList=[], riverPos=riverpos, trapPos=trappos[3:6], denPos=denpos[1])
        return receiver

    def executeInput(self, turnFlag: int):
        self.gamer: player
        if not turnFlag:
            ...
        else:
            ...
        inputs: list = input(
            "Please input your commands: ").split()

        if inputs[0] == "move":
            while not self.checkMove(inputs[1:]):
                inputs = input("Wrong input, please input again: ").split()

            if not self.Undo(turnFlag):
                # chess.move?
                with open(r"./History.txt", "w") as fp:
                    fp.write(" ".join(inputs))
        elif inputs[0] == "help":
            self.game_view.printHelp()
        elif inputs[0].lower() == "defeat":
            self.AdmitDefeat()
        elif inputs[0].lower() == "exit":
            self.Exit()
            print("Bye~")
        else:
            Exception("Input wrong, system will stop")

    def checkMove(self, cmd: list) -> bool:
        # add check jump river
        val: tuple = self.gamer.position
        if cmd[0].lower() == "l":
            if val[0] - int(cmd[1]) < 0: return False
        elif cmd[0].lower() == "r":
            if val[0] + int(cmd[1]) > 6: return False
        elif cmd[0].lower() == "down":
            if val[1] - int(cmd[1]) < 0: return False
        elif cmd[0].lower() == "up":
            if val[1] + int(cmd[1]) > 8: return False
        return True

    def getHelp(self):
        """do we still need this?"""
        pass

    def Undo(self, turnFlag):
        if self.players.undoNum > 3: return False
        undo = input("do you wanna undo your option?")
        if undo.lower() in ["yes", "y"]:
            print("for player ", 2 - turnFlag, " do you agree to allow your opponent undo his/her optional?")
            permission = input().lower()
            if permission in ["no", "n"]:
                print("you are not allowed to do this, player ", turnFlag + 1)
            elif permission in ["yes", "y"]:
                self.players.undoNum += 1
                self.executeInput(turnFlag)
                return True
        return False

    def finalPrint(self):
        ...

    def AdmitDefeat(self, turnFlag: int):
        if input("you will admit you are defeated by your opponent, pls confirm again: ").lower() in ["y", "yes"]:
            print("player ", 2-turnFlag, " win this game! ")
            self.finalPrint()
        pass

    def Exit(self):
        print("""
        Be aware that the whole system will immediately shut down and stopping recording, \n
        Game wont record your current status or any history except those has been writen in history.txt
        """)
        if input("You sure you wanna exit?").lower() in ["y", "yes"]:
            print("Have a good day, hope meet you next time.")
            sys.exit(0)
        return

    def ifEnd(self):

        pass

    def whichTurn(turnFlag: int):
        if (turnFlag == 0):
            pass
        else:
            pass

    def time_spire(self):
        available_second = 60
        for i in range(1, available_second):
            print('you have %d seconds' % (available_second - i))
            if available_second - i == 10:
                print("10 seconds left.")
        print("Time expired, your turn finished.")
        time.sleep(1)  # 时间倒计时
