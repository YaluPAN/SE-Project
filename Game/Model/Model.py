import Players
from Chess import *
from Exceptions import *


class Model():
    # The model component manages the system data and associated operations on that data.

    def getChessboard():
        return Players

    def addMoveHistory():
        pass

    def getMoveHistory():
        MoveHistory = "..."
        return MoveHistory

    def addCapturedResult():
        pass

    def getCapturedResult():
        CapturedResult = "..."
        return CapturedResult
