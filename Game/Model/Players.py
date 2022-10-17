import Chess


class Players():
    def __init__(self, chessList: Chess = [], riverPos: tuple = [], trapPos: tuple = [], denPos: tuple = []) -> None:
        self.chessList = chessList
        self.riverPos = riverPos
        self.trapPos = trapPos
        self.denPos = denPos
