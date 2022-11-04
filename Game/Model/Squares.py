from operator import truediv
from pickle import TRUE
import typing
from typing import List, Type, TypeVar


class Squares:
    '''
    The class "Squares" is designed to represent static squares in a chessboard, including den squares, traps squares and river squares.
    '''

    def __init__(self):
        self.den_position = [(3, 0), (3, 8)]
        self.trap_position = [(2, 0), (4, 0), (3, 1), (2, 8), (3, 7), (4, 8)]
        self.river_position = [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4),
                               (2, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)]

    def getRiverSide(self, square_position: tuple) -> str:
        '''
        1. This function is used to get the river side based on a specific square position. 
        2. Function parameter: "square_position" is passed from get_new_estimated_position() in Model. 
        3. Return value: returns a str, ether 'left' or 'right'. 
        4. How to achieve: by iterating all river squares position, and find which on is the same as the "square_position"
        '''
        pass

    def get_den_position(self) -> list:
        # get den squares position, return a list of den position which is represented in tuple (x,y)
        return self.den_position

    def get_trap_position(self) -> list:
        # get traps squares position, return a list of traps position which is represented in tuple (x,y)
        return self.trap_position

    def get_river_position(self) -> list:
        # get river squares position, return a list of river position which is represented in tuple (x,y)
        return self.river_position


class Animals(Squares):
    '''
    The class "Squares" is designed to represent animals squares in a chessboard, including 8 types of animals. 
    The important attribute of the animals are: name, rank, position, and status(indicates they're live or dead)
    '''

    def __init__(self, name, rank, position: tuple, status):
        super().__init__()
        self.name = name
        self.rank = rank
        self.position = position
        status = True
        self.status = status

    def getRank(self) -> int:
        return self.rank

    def getPosition(self) -> tuple:
        return self.position

    def ifInTrap(self) -> bool:
        # check whether an animal position is in trap
        pass

    def ifInLand(self) -> bool:
        # check whether an animal position is in land
        pass

    def ifInDen(self) -> bool:
        # check whether an animal position is in den
        pass

    def ifInRiver(self) -> bool:
        # check whether an animal position is in river
        pass

    def move(self, direction) -> None:
        '''
        This function can be used only when ifCanMove() == True. The attribute of "position" of Animal instance will be changed after moving into next step in this function.

        The reason that we divide move() into 4 clear functions, is to make the programming more object-oriented.

        No return value of this function. Because the purpose of this func is to change the "position" attribute of an Animal instance.

        '''

        try:
            if (direction == "up"):
                self.upMove()
            elif (direction == "down"):
                self.downMove()
            elif (direction == "left"):
                self.leftMove()
            elif (direction == "right"):
                self.rightMove()
        except Exception:
            print("Error! The Animal's position can't change. Pls check move()")

    def jumpOver(self, direction) -> None:
        '''
        This function is used only when the animal is Lion or Tiger. As they can jump over the river to the opponent side. Lion/Tiger's attribute of "position" will change. 
        No return value of this func.
        '''
        try:
            if (direction == "up"):
                self.jumpOverUp()
            elif (direction == "down"):
                self.jumpOverDown()
            elif (direction == "left"):
                self.jumpOverLeft()
            elif (direction == "right"):
                self.jumpOverRight()

        except Exception:
            print("Error! The Animal's position can't change. Pls check jumpOver()")

    '''
    The 4 following functions (upMove(), downMove(), leftMove(), rightMove()), are used in move().

    No return value of these function. Because the purpose of this func is to change the "position" attribute of an Animal instance.
    '''

    def upMove(self) -> None:
        (x, y) = self.position
        self.position = (x, y+1)

    def downMove(self) -> None:
        (x, y) = self.position
        self.position = (x, y-1)

    def leftMove(self) -> None:
        (x, y) = self.position
        self.position = (x-1, y)

    def rightMove(self) -> None:
        (x, y) = self.position
        self.position = (x+1, y)

    '''
    The 4 following functions (jumpOverUp(), jumpOverDown(), jumpOverLeft(), jumpOverRight()), are used in move().

    No return value of these function. Because the purpose of this func is to change the "position" attribute of an Animal instance by changing the value of x or y in tuple of position. 
    '''

    def jumpOverUp(self) -> None:
        pass

    def jumpOverDown(self) -> None:
        pass

    def jumpOverLeft(self) -> None:
        pass

    def jumpOverRight(self) -> None:
        pass

if __name__ == "__main__":
    print("everything OK")