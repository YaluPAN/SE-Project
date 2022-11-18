from Game.View.View import View
from Game.Model.Model import Model
from Game.Controller.Controller import Controller

"""
    Initialization for the Jungle object which includes all the essential objects for the whole game.
    This class includes two players defined in Model, a view and a model object, and a controller as the kernel part to 
    conduct the game.
    A boolean variable inturn is defined.
"""


class Jungle:
    def __init__(self):

        self.game_view = View()
        self.game_model = Model()
        self.game_controller = Controller(
            self.game_model, self.game_view)
        # self.inturn = False

    """
        Turnflag counts the number of rounds for a started game. Taking it modulo 2 will we obtain the boolean input for
        parameter in executeInput().
        Call the ifEnd() function to judge whether the game ends in every round.
    """

    def start(self):
        self.game_view.printWelcomePage()
        self.game_controller.chooseSide()
        self.game_controller.executeInput()


# main function, executes once jungle.py executes.


def main():
    sys = Jungle()
    sys.start()


if __name__ == "__main__":
    main()