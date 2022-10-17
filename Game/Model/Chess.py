class Chess():
    def _init_(self, name, rank, position, status):
        self.position = position
        self.rank = rank
        status = True
        self.status = status
        self.name = name

    def upMove(self):
        (x, y) = self.position
        self.position = (x, y+1)

    def downMove(self):
        (x, y) = self.position
        self.position = (x, y-1)

    def leftMove(self):
        (x, y) = self.position
        self.position = (x-1, y)

    def rightMove(self):
        (x, y) = self.position
        self.position = (x+1, y)

    def ifInTrap(self):
        if self.position == trap_position:
            self.trap = True
        else:
            self.trap = False

    def changeStatus(self):
        self.status = False


class Lion(Chess):
    def _init_(self, water):
        water = False
        self.water = water
        self.rank = 7

    def jumpOverRiverUp(self):
        (x, y) = self.position
        self.position = (x, y+3)

    def jumpOverRiverDown(self):
        (x, y) = self.position
        self.position = (x, y-3)

    def jumpOverRiverLeft(self):
        (x, y) = self.position
        self.position = (x-3, y)

    def jumpOverRiverRight(self):
        (x, y) = self.position
        self.position = (x+3, y)


class Tiger(Chess):
    def _init_(self, water):
        water = False
        self.water = water
        self.rank = 6

    def jumpOverRiverUp(self):
        (x, y) = self.position
        self.position = (x, y+3)

    def jumpOverRiverDown(self):
        (x, y) = self.position
        self.position = (x, y-3)

    def jumpOverRiverLeft(self):
        (x, y) = self.position
        self.position = (x-3, y)

    def jumpOverRiverRight(self):
        (x, y) = self.position
        self.position = (x+3, y)


class Rat(Chess):
    def _init_(self, water):
        water = False
        self.water = water
        self.rank = 1
