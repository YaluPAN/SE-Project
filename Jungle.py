import os
import sys
from View import View
from Model import Model
from Controller import Controller


class Jungle:
    def __init__(self):
        self.initPlayer1 = Model.Players
        self.initPlayer2 = Model.Players
        self.game_view = View.View()
        self.game_model = Model.Model()
        self.game_controller = Controller.Controller(
            self.game_model, self.game_view)
        self.inturn = False

    def start(self):
        turnFlag = 0
        self.game_controller.chooseLanguage()
        self.game_controller.chooseSide()
        self.game_view.printWelcomePage()
        self.game_view.printChessboard(self.initPlayer1, self.initPlayer2)
        while (Controller.ifEnd() == False):
            turnFlag += 1
            Controller.executeInput(turnFlag % 2)


def main():
    sys = Jungle()
    sys.start()


if __name__ == "__main__":
    main()
