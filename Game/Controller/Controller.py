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
        if inputs == "down":
            receiver[0] = player.Players(chessList=[], riverPos=riverpos, trapPos=trappos[0:3], denPos=denpos[0])
            receiver[1] = player.Players(chessList=[], riverPos=riverpos, trapPos=trappos[3:6], denPos=denpos[1])
        elif inputs == "up":
            receiver[1] = player.Players(chessList=[], riverPos=riverpos, trapPos=trappos[0:3], denPos=denpos[0])
            receiver[0] = player.Players(chessList=[], riverPos=riverpos, trapPos=trappos[3:6], denPos=denpos[1])
        return receiver

    def executeInput(self, turnFlag):

        inputs: list = input(
            "Please input your commands: ").split()

        if inputs[0] == "move":
            self.checkMove(turnFlag)
            pass
        elif inputs[0] == "help":
            self.game_view.printHelp()
        elif inputs[0].lower() == "undo":
            self.Undo()
        elif inputs[0].lower() == "defeat":
            self.AdmitDefeat()
        elif inputs[0].lower() == "exit":
            self.Exit()
            print("Bye~")
        else:
            Exception("Input wrong, system will stop")

    def checkMove(self, turnFlag):

        ...

    def getHelp():
        pass

    def Undo():
        pass

    def AdmitDefeat():
        pass

    def Exit():
        pass

    def ifEnd():
        pass

    def whichTurn(turnFlag: int):
        if (turnFlag == 0):
            pass
        else:
            pass

    def time_spire():
        available_second = 60
        for i in range(1, available_second):
            print('you have %d seconds' % (available_second - i))
            if available_second - i == 10:
                print("10 seconds left.")
        print("Time expired, your turn finished.")
        time.sleep(1)  # 时间倒计时
