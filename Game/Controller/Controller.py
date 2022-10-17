from Model import Model
from View import View
import time


class Controller:

    def __init__(self, game_model: Model, game_view: View):
        self.game_model = game_model
        self.game_view = game_view

    def chooseLanguage(self):
        inputs: str = input(
            "Please choose your language preference(Chinese or English), and color (Green or Blue): ")

        if inputs == "chinese":
            pass

        elif inputs == "english":
            pass

    def chooseSide(self):
        inputs: str = input("Please choose your preferred side: ")

        if inputs == "down":
            pass

        elif inputs == "up":
            pass

    def executeInput(self, turnFlag):

        inputs: list = input(
            "Please input your commands: ").split()

        if inputs[0] == "move":
            self.checkMove()
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

    def checkMove():
        pass

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
            print('you have %d seconds' % (available_second-i))
            if available_second-i == 10:
                print("10 seconds left.")
        print("Time expired, your turn finished.")
        time.sleep(1)  # 时间倒计时
