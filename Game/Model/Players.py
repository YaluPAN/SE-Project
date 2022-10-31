import Chess


class Players():
    def __init__(self, chessList: Chess = [], riverPos: tuple = [], trapPos: tuple = [], denPos: tuple = []) -> None:
        self.chessList = chessList
        self.riverPos = riverPos
        self.trapPos = trapPos
        self.denPos = denPos

    riverpos: list = [(x, y) for x in [1, 2, 4, 5] for y in range(3, 6)]
    trappos: list = [(2, 0), (3, 1), (4, 0), (2, 8), (3, 7), (4, 8)]
    denpos: list = [(3, 0), (3, 8)]

    # receiver[0] = player.Players(chessList=[], riverPos=riverpos, trapPos=trappos[0:3], denPos=denpos[0])
    # receiver[1] = player.Players(chessList=[], riverPos=riverpos, trapPos=trappos[3:6], denPos=denpos[1])