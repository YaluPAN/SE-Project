import Model
from operator import truediv
from pickle import TRUE


class Squares():
    def _init(self):
        self.den = [(3, 0), (3, 8)]
        self.trap_position = [(2, 0), (4, 0), (3, 1), (2, 8), (3, 7), (4, 8)]
        self.river_position = [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4),
                               (2, 5), (4, 3), (4, 4), (4, 5)(5, 3), (5, 4), (5, 5)]

    def getRiverSide(square_position) -> str:
        # return 'left' or 'right'. Indicating which river the square position belonged to
        pass

    def if_rat_in_that_river(side_of_river) -> bool:
        pass


class Animals(Squares):
    def _init_(self, name, rank, position, inTrap, nearRiver, status):
        self.name = name
        self.rank = rank
        self.position = position
        inTrap = False
        self.inTrap = inTrap
        nearRiver = False
        self.nearRiver = nearRiver
        status = True
        self.status = status

    def getRank(self) -> int:
        return self.rank

    # def ifInTrap(self) -> bool:
    #     for position in self.trap_position:
    #         if self.position == position:
    #             self.inTrap = True
    #         else:
    #             self.inTrap = False

    # def ifNearRiver(self) -> bool:
    #     return self.nearRiver

    def ifCanMove(self, direction) -> tuple(bool, str):
        noHint = ...
        Hint1 = ...
        Hint2 = ...
        Hint3 = ...
        Hint4 = ...
        Hint5 = ...
        '''
        There are totally 5 situations when an Animal Chess is moved:
        1. The animal's next step in out of chessboard range
        2. The animal's next step is on land
        3. The animal's next step is in River
        4. The animal's next step is in Trap
        5. The animal's next step is in Den
        For the first 3 situations, we consider 
        '''
        # 1 If the animal's next step in out of chessboard range
        new_position = self.get_estimated_new_position(self, direction)

        if (self.if_move_out_of_range(new_position) == False):
            return (False, Hint1)

        # 2 If the animal's next step is in land:j
        elif (self.if_next_step_in_land(new_position) == True):
            # For all Animals, they're not allowed to move to:
            # 2.1 a land square that already occupied by its side's animals
            if (self.if_occupied_by_same_side_animal(self, new_position) == False):
                return (False, Hint2)

        # 2.2 For all Animals except Elephant(8): a square that already occupied by enemies that have a higher rank. For Elephant(8): a square that already occupied by enemy Rat(1)
            elif (self.if_occupied_by_higher_rank_enemy(self, new_position) == False):
                return (False, Hint3)

        # 3 If the animal's next step is in river:
        elif (self.if_next_step_in_river(new_position) == True):
            # 3.1 For Elephant(8), Leopard(5), Wolf(4), Dog(3), Cat(2): can't move across the river
            if (self.getRank() == '8' or self.getRank() == '5' or self.getRank() == '4' or self.getRank() == '3' or self.getRank() == '2'):
                return (False, Hint4)
        # 3.2 For Lion(7), Tiger(6): can move across the river  when there is NOT a Rat(1) in the river
            elif (self.getRank() == '7' or self.getRank() == '6'):
                side_of_river = Squares.getRiverSide(new_position)
                return (not Squares.if_rat_in_that_river(side_of_river), Hint5)

        # 3.3 For Rat(1): can randomly go into the river
        elif (self.getRank() == '1'):
            return (True, noHint)

        # 4 If the animal's next step is in trap: it's always allowed that an animal want to move to a trap
        # 5 If the animal's next step is in den: it's always allowed that an animal want to move to a den

    def get_estimated_new_position(self, direction) -> tuple:
        pass

    def if_move_out_of_range(new_position) -> bool:
        pass

    def if_next_step_in_land(new_position) -> bool:
        pass

    def if_occupied_by_same_side_animal(self, new_position) -> bool:
        pass

    def if_occupied_by_higher_rank_enemy(self, new_position) -> bool:
        pass

    def if_next_step_in_river(new_position) -> bool:
        pass

    # def whether_couldMove(self.initPlayer1, self.initPlayer2):
    #     # 先暂且默认这里player1指自己的棋子
    #     for i in self.initplayer1.chessList:
    #         if self.position == i.position:
    #             return False
    #     for i in self.initplayer2.chessList:
    #         if self.posiiton == i.position and self.rank > i.rank or (self.position == i.position and self.rank < i.rank and i.ifInTrap() == True) or (self.rank == 1 and i.rank == 9):
    #             self.initplayer2.chessList.remove(i)
    #             self.initplayer1.chessResult.add(i)
    #             i.changeStatus = False
    #             return TRUE

    # def whether_near_Water(self):
    #     (x, y) = self.position
    #     if (x, y) == (0, 3) or (0, 4) or (0, 5) or (3, 3) or (3, 4) or (3, 5) or (8, 3) or (8, 4) or (8, 5) or (1, 2) or (2, 2) or (4, 2) or (5, 2) or (1, 6) or (2, 6) or (4, 6) or (5, 6):
    #         return TRUE
    #     else:
    #         return False

    def whether_couldJumpRiver(self):
        if (self.whether_near_Water == True and self.whether_couldMove(self.initPlayer1, self.initPlayer2) == True):
            if self.player1.chessList.Rat.whetherInRiver == True:
                return False
            else:
                return True
        return True

    def upMove(self):  # need define players
        flag = False
        (x, y) = self.position
        for i in self.riverposition:
            if y+1 == i.y:
                flag = TRUE

        if y+1 > 8 or flag == TRUE or self.whether_couldMove == False or (x, y+1) == self.inTrap:
            self.position = (x, y)
        else:
            self.position = (x, y+1)
            Model.addMovehistory()
            Model.addCaptureResult()
            if (x, y+1) == self.initplayer2.inTrap:
                pass
                # controller()

    def downMove(self):
        flag = False
        (x, y) = self.position
        for i in self.riverposition:
            if y-1 == i.y:
                flag = TRUE

        if y-1 < 0 or flag == TRUE or self.whether_couldMove == False or (x, y-1) == self.inTrap:
            self.position = (x, y)
        else:
            self.position = (x, y-1)
            Model.addMovehistory()
            Model.addCaptureResult()
            if (x, y-1) == self.initplayer2.inTrap:
                pass
            # controller

    def leftMove(self):
        flag = False
        (x, y) = self.position
        for i in self.riverposition:
            if x-1 == i.x:
                flag = TRUE

        if x-1 < 0 or flag == TRUE or self.whether_couldMove == False or (x-1, y) == self.inTrap:
            self.position = (x, y)
        else:
            self.position = (x-1, y)
            Model.addMovehistory()
            Model.addCaptureResult()
            if (x-1, y) == self.initplayer2.inTrap:
                pass
            # controller

    def rightMove(self):
        flag = False
        (x, y) = self.position
        for i in self.riverposition:
            if x+1 == i.x:
                flag = TRUE

        if x+1 > 8 or flag == TRUE or self.whether_couldMove == False or (x+1, y) == self.inTrap:
            self.position = (x, y)
        else:
            self.position = (x+1, y)
            Model.addMovehistory()
            Model.addCaptureResult()
            if (x+1, y) == self.initplayer2.trap:
                pass
            # controller

    def changeStatus(self):
        self.status = False


class Lion(Animals):
    def _init_(self, nearWater):
        self.nearWater = False
        self.nearWater = nearWater
        self.rank = 7

    def whether_couldJumpRiver(self):
        if (self.whether_near_Water == True and self.whether_couldMove(self.initPlayer1, self.initPlayer2) == True):
            if self.player1.chessList.Rat.whetherInRiver == True:
                return False
            else:
                return True
        return True

    def jumpOverRiverUp(self):
        (x, y) = self.position
        if (self.whether_couldJumpRiver == True and y == 2):
            self.position = (x, y+3)
        else:
            self.position = (x, y)

    def jumpOverRiverDown(self):
        (x, y) = self.position
        if (self.whether_couldJumpRiver == True and y == 6):
            self.position = (x, y-3)
        else:
            self.position = (x, y)

    def jumpOverRiverLeft(self):
        (x, y) = self.position
        if (self.whether_couldJumpRiver == True and (x == 6 or x == 3)):
            self.position = (x, y-3)
        else:
            self.position = (x, y)

    def jumpOverRiverRight(self):
        (x, y) = self.position
        if (self.whether_couldJumpRiver == True and (x == 0 or x == 3)):
            self.position = (x, y-3)
        else:
            self.position = (x, y)


class Tiger(Animals):
    def _init_(self, nearWater):
        nearWater = False
        self.nearWater = nearWater
        self.rank = 6

    def jumpOverRiverUp(self):
        (x, y) = self.position
        if (self.whether_couldJumpRiver == True and y == 2):
            self.position = (x, y+3)
        else:
            self.position = (x, y)

    def jumpOverRiverDown(self):
        (x, y) = self.position
        if (self.whether_couldJumpRiver == True and y == 6):
            self.position = (x, y-3)
        else:
            self.position = (x, y)

    def jumpOverRiverLeft(self):
        (x, y) = self.position
        if (self.whether_couldJumpRiver == True and (x == 6 or x == 3)):
            self.position = (x, y-3)
        else:
            self.position = (x, y)

    def jumpOverRiverRight(self):
        (x, y) = self.position
        if (self.whether_couldJumpRiver == True and (x == 0 or x == 3)):
            self.position = (x, y-3)
        else:
            self.position = (x, y)


class Rat(Animals):
    def _init_(self):
        self.rank = 1

    def whetherInRiver(self):
        for i in self.riverposition:
            if i.x == self.position.x and i.y == self.position.y:
                return True
        return False
