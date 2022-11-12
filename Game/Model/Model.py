from Game.Model.Squares import Squares, Animals
import os

class Model():
    '''
    The Model component manages the system data and associated operations on that data.
    The "Model" class here is initialized to be a new chessboard at every time the game starts.
    In the chessboard, it has 2 lists of animals, respectively corresponding to the down side and up side animals in the chessboard.
    Besides, there are other squares in the chessboard, representing the den area, traps area, and river area.
    The purpose that we put the chessboard into Model component, is the data changing in system is for chess status. For example, the players input commands to move a chess, making the chess position, status, or other attributes changed.
    Therefore, we initialize totally 16 animals(downside_Rat, upside_Rat, downside_Cat, upside_Cat...) with their original position(the precise position, if the position is in trap), rank and status. These animals objects are stored in lists as data structure.
    To initialize other squares, we use the "Squares" class to get those squares (den, traps, and river squares).
    '''

    # initialize a new Chessboard
    def __init__(self):
        # def _init_(self, name, rank, position: tuple(), inTrap,  status):
        downside_Rat = Animals("downside_Rat", 1, (6, 2), True)
        downside_Cat = Animals("downside_Cat", 2, (1, 1), True)
        downside_Dog = Animals("downside_Dog", 3, (5, 1), True)
        downside_Wolf = Animals("downside_Wolf", 4, (2, 2), True)
        downside_Leopard = Animals("downside_Leopard", 5, (4, 2), True)
        downside_Tiger = Animals("downside_Tiger", 6, (0, 0), True)
        downside_Lion = Animals("downside_Lion", 7, (6, 0), True)
        downside_Elephant = Animals(
            "downside_Elephant", 8, (0, 2), True)

        upside_Rat = Animals("upside_Rat", 1, (0, 6), True)
        upside_Cat = Animals("upside_Cat", 2, (5, 7), True)
        upside_Dog = Animals("upside_Dog", 3, (1, 7), True)
        upside_Wolf = Animals("upside_Wolf", 4, (4, 6), True)
        upside_Leopard = Animals("upside_Leopard", 5, (2, 6), True)
        upside_Tiger = Animals("upside_Tiger", 6, (6, 8), True)
        upside_Lion = Animals("upside_Lion", 7, (0, 8), True)
        upside_Elephant = Animals("upside_Elephant", 8, (6, 6), True)

        downAnimalList = [downside_Rat, downside_Cat, downside_Dog,
                          downside_Wolf, downside_Leopard, downside_Tiger, downside_Lion, downside_Elephant]

        upAnimalList = [upside_Rat, upside_Cat, upside_Dog,
                        upside_Wolf, upside_Leopard, upside_Tiger, upside_Lion, upside_Elephant]

        squares = Squares()
        den_position = squares.get_den_position()
        trap_position = squares.get_trap_position()
        river_position = squares.get_river_position()

        self.downAnimalList = downAnimalList
        self.upAnimalList = upAnimalList
        self.den_position = den_position
        self.trap_position = trap_position
        self.river_position = river_position

    def ifCanMove(self, moving_animal: Animals, direction, action) -> tuple:
        '''
        1. Purpose: This function is used to check whether the animal can move to next step.
        2. Function parameters: "moving_animal" and "direction" are parameters that passed from Controller
        3. Return value: return a tuple that contains a boolean value and a string value. The boolean value represents whether the animal can move to next step. The str are hints that remind true/wrong operation of moving to the player. For example, if an animal can't move to next step because the new position is in river, the str will contain a hint that told the player why his movement is failed.
        4. There are totally 5 situations when an Animal Chess is moved:
            a)The animal's next step in out of chessboard range
            b)The animal's next step is on land
            c)The animal's next step is in River
            d)The animal's next step is in Trap
            e)The animal's next step is in Den
            For a, b and c situations, we consider cases that the Animal can't move legally. If the Animal can't move, the function will return False and a hint string. The hint string can be used in the View component so that users can know reasons that the animal can't move and make revision.
            As for d and e situations, it's always allowed that an animal want to move to a trap or a den. So we will not check case in these 2 situations.
        '''

        Hint1 = 1
        Hint2 = 2
        Hint3 = 3
        Hint4 = 4
        Hint5 = 5
        Hint6 = 6
        Hint7 = 7
        Hint8 = 8

        # get the estimated new position of the animal. This position is NOT the real position of animals, but an estimated one, which is used for validating purpose.
        try:
            new_position = self.get_estimated_new_position(moving_animal, direction, action)
            if self.get_estimated_new_position(moving_animal, direction, action) == self.den_position:
                if moving_animal.name[0] == 'u':
                    if self.get_estimated_new_position(moving_animal, direction, action) == (3, 8):
                        return False, Hint8
                    return True, Hint8
                if moving_animal.name[0] == 'd':
                    if self.get_estimated_new_position(moving_animal, direction, action) == (3, 0):
                        return False, Hint8
                    return True, Hint8

            # 1 If the animal's next step in out of chessboard range
            elif (self.if_move_out_of_range(new_position) == True):
                return (False, Hint1)

            # 2 If the animal's next step is in land:
            elif (self.if_next_step_in_land(new_position) == True):
                # For all Animals, they're not allowed to move to:
                # 2.1 a land square that already occupied by its side's animals
                if (self.if_position_has_same_side_animal(self, moving_animal, new_position) == False):
                    return (False, Hint2)

                # 2.2
                # a. For Rat(1): if its original position is in River, it can't move to a square that already occupied by enemy Elephant(8)(Elephant belonged to any higher rank, case a) or enemy Rat(1), because it will be eaten by enemy Elephant(8) or enemy Rat(1).
                elif (moving_animal.getRank == '1'):
                    if (self.if_position_has_higher_rank_enemy(moving_animal, new_position)
                    ):
                        return (False, Hint3)
                    elif (self.if_position_has_same_rank_enemy(moving_animal, new_position)):
                        return (False, Hint4)
                    else:
                        return True
                # b. For all Animals except Elephant(8): a square that already occupied by enemies that have a higher rank.
                elif (moving_animal.getRank() != '8'):
                    return (not self.if_position_has_higher_rank_enemy(moving_animal, new_position), Hint3)
                # c. For Elephant(8): a square that already occupied by enemy Rat(1)
                elif (moving_animal.getRank() == '8'):
                    return (not self.if_position_has_enemy_Rat(moving_animal, new_position), Hint4)

            # 3 If the animal's next step is in river:
            elif (self.if_next_step_in_river(new_position) == True):
                # 3.1 For Elephant(8), Leopard(5), Wolf(4), Dog(3), Cat(2): can't move across the river
                if (
                        moving_animal.getRank() == '8' or moving_animal.getRank() == '5' or moving_animal.getRank() == '4' or moving_animal.getRank() == '3' or moving_animal.getRank() == '2'):
                    return (False, Hint5)
                # 3.2 For Lion(7), Tiger(6): can move across the river  when there is NOT a Rat(1)(no matter friendly or enemy) in the river
                elif (moving_animal.getRank() == '7' or moving_animal.getRank() == '6'):
                    side_of_river = Squares.getRiverSide(new_position)
                    return (not self.if_rat_in_that_river(side_of_river), Hint6)

            else:
                return (True, Hint7)
            # 3.3 For Rat(1): can randomly go into the river
            # elif (self.getRank() == '1'):
            #     return (True, noHint)

        except Exception:
            print(
                "Error! Can't check whether the animal can move to next step. Pls check ifCanMove() in Model.py")

    def move(self, moving_animal: Animals, direction) -> None:
        '''
        1. Purpose: This function is used for change the moving animal's position.
        2. Function parameters: "moving_animal" and "direction" are parameters that passes from Controller
        3. Return value: None. Because the func only changes the position attribute in an animal object.
        '''
        moving_animal.move(direction)

    def if_in_opposite_den(self, moving_animal: Animals, direction, action):
        if moving_animal.name[0] == 'u':
            if self.get_estimated_new_position(moving_animal, direction, action) == (3, 0):
                return True
            return False
        else:
            if self.get_estimated_new_position(moving_animal, direction, action) == (3, 8):
                return True
            return False

    def jumpOver(self, moving_animal: Animals, direction) -> None:
        '''
        1. Purpose: This function is used for change the moving Tiger/Lion position if they want to jump over a river.
        2. Function parameters: "moving_animal" and "direction" are parameters that passes from Controller
        3. Return value: None. Because the func only changes the position attribute in an animal object.
        '''
        moving_animal.jumpOver(direction)

    def if_new_position_has_enemy_that_can_be_eaten(self, moving_animal: Animals) -> bool:
        '''
        1. Purpose: This function is used to check that if the new position where the animal move to has an enemy that it can eat.
        2. Function parameter: "moving_animal" is passed from Controller
        3. Return value: returns a boolean value, representing whether the new position has an enemy that can be eaten.
        4. The process that we have considered is: After the Animal move to next square, the animal may be:
            1)in Land
                1.1 All animals except Rat(1), can eat enemy that have the same/lower rank
                ??? can elephant eat rat?
                1.2 Rat(1) can eat enemy Elephant(8) and Rat(1)
                    The case that a Rat move from the water to attack enemy Elephant/Rat is NOT allowed. This case is already checked by ifCanMove() before this func.
            2)in River
                only Rat(1) will in River. In this case, it can eat enemy Rat(1).
            3)in Trap
                All animal in traps can eat any enemy pieces
            4)in Den
                the side of the animal will win if the animal move to opponent's side.
                Because in this case, the animal will not care eating enemy anymore
        '''
        try:
            # 1 in Land
            if (moving_animal.ifInLand()):
                # 1.1 All animals except Rat(1), can eat enemy that have the same/lower rank
                position = moving_animal.getPosition()
                if (moving_animal.getRank() != '1'):
                    return not self.if_position_has_higher_rank_enemy(self, moving_animal, position)

                # 1.2 Rat(1) can eat enemy Elephant(8) and Rat(1)
                elif (moving_animal.getRank() == '1'):
                    # The case that a Rat move from the water to attack enemy Elephant/Rat is NOT allowed. However, this case is already checked by ifCanMove() before this func.
                    return self.if_position_has_enemy_Elephant(self, moving_animal,
                                                               position) | self.if_position_has_same_rank_enemy(self,
                                                                                                                moving_animal,
                                                                                                                position)

            # 2 in River
            elif (moving_animal.ifInRiver()):
                # only Rat(1) will in River. In this case, it can eat enemy Rat(1).
                return self.if_position_has_same_rank_enemy(self, moving_animal, position)

            # 3 in Trap
            elif (moving_animal.ifInTrap()):
                return True

            else:
                return False
        except Exception:
            print(
                "Error! Can't check whether the animal can eat enemy. Pls check ifCanEatEnemy()")

    def get_same_position_enemy(self, moving_animal: Animals) -> 'Animals':
        if moving_animal.name[0] == 'd':
            for i in self.upAnimalList:
                if i.position == moving_animal.position:
                    return i.name
        else:
            for i in self.upAnimalList:
                if i.position == moving_animal.position:
                    return i.name

        '''
        1. Purpose: This function is used only when if_new_position_has_enemy_that_can_be_eaten() is True. Because it's confirmed that the animal has moved to the square that has enemy pieces that it can eat, this func will search the exact enemy piece that will be eaten
        2. Function parameters: "moving_animal" is passed from Controller
        3. Return value: returns an enemy piece object
        4. How to achieve: by iterating positions of all enemy pieces, and find the one which has a same position with moving_animal
        '''

    def die(self, dying_animal: Animals) -> None:
        dying_animal.change_status()

        '''
        1. Purpose: This function is used after found the enemy to be eaten. The enemy piece's attribute of "status" will change from True(live) to False(dead).
        2. Function parameter: "dying_animal" is passed from get_same_position_enemy()
        3. Return value: None. Because it only change the status attribute of an animal object
        '''

    def get_estimated_new_position(self, moving_animal: Animals, direction, action) -> tuple:
        (x, y) = Animals.getPosition()
        if action == 'move':
            if direction == 'up':
                return x, y + 1
            elif direction == 'down':
                return x, y - 1
            elif direction == 'left':
                return x - 1, y
            elif direction == 'right':
                return x + 1, y

        if action == 'jump':
            if direction == 'up':
                return x, y + 4
            elif direction == 'down':
                return x, y - 4
            elif direction == 'left':
                return x - 3, y
            elif direction == 'right':
                return x + 3, y

        '''
        1. Purpose: get the estimated position of an animal's move
        2. Function parameter: "moving_animal" and "direction" are passed from Controller
        3. Return value: a tuple, which is the precise estimated position in a form of (x,y)
        4. How to achieve: by calculating the position change based on direction.
        '''

    def if_move_out_of_range(self, position: tuple) -> bool:
        """
        1. Purpose: check if the position is out of range of a chessboard
        2. Function parameter: "position" is passed from get_estimated_new_position()
        3. Return value: a boolean value
        4. How to achieve: by iterating all squares positions in a chessboard, and check whether the "position" is same as one of them
        """
        (x, y) = position
        if x < 0 or x > 6 or y < 0 or y > 8:
            return True
        return False

    def if_next_step_in_land(self, new_position: tuple) -> bool:
        """
        1. Purpose: check if the new position is in a land square
        2. Function parameter: "new_position" is passed from get_estimated_new_position()
        3. Return value: a boolean value
        4. How to achieve: by iterating all land squares positions in a chessboard, and check whether the "position" is same as one of them
        """
        for i in self.river_position:
            if new_position == i:
                return False
        return True

    def if_position_has_same_side_animal(self, moving_animal: Animals, position: tuple) -> bool:
        """
        1. Purpose: check if the new position is occupied by a same side animal
        2. Function parameter: "moving_animal" is passed from if_new_position_has_enemy_that_can_be_eaten from Controller, "position" is passed from get_estimated_new_position()
        3. Return value: a boolean value
        4. How to achieve: by iterating all same side animals' positions in a chessboard, and check whether the "position" is same as one of them
        """
        if moving_animal.name[0] == 'd':
            for i in self.downAnimalList:
                if i.position == position:
                    return True
            return False
        else:
            for i in self.downAnimalList:
                if i.position == position:
                    return True
            return False

    def if_position_has_same_rank_enemy(self, moving_animal: Animals, position: tuple) -> bool:
        """
        1. Purpose: check if the new position is occupied by a same rank animal
        2. Function parameter: "moving_animal" is passed from if_new_position_has_enemy_that_can_be_eaten from Controller, "position" is passed from get_estimated_new_position()
        3. Return value: a boolean value
        4. How to achieve: by comparing the same rank animal's position with "position"
        """
        # 不需要
        if moving_animal.name[0] == 'u':
            for i in self.downAnimalList:
                if i.position == position:
                    if i.rank == moving_animal.rank:
                        return True
            return False
        else:
            for i in self.upAnimalList:
                if i.position == position:
                    if i.rank == moving_animal.rank:
                        return True
            return False

        pass

    def if_position_has_lower_rank_enemy(self, moving_animal: Animals, position: tuple) -> bool:
        '''
        1. Purpose: check if the new position is occupied by a lower rank enemies
        2. Function parameter: "moving_animal" is passed from if_new_position_has_enemy_that_can_be_eaten from Controller, "position" is passed from get_estimated_new_position()
        3. Return value: a boolean value
        4. How to achieve: by iterating all lower rank animals' positions in a chessboard, and check whether the "position" is same as one of them
        '''
        if moving_animal.getRank() == '8':
            # if the moving animal is an Elephant, it can never eat enemy Rat
            return self.if_position_has_lower_rank_enemy_except_Rat(moving_animal, position)
        else:
            if moving_animal.name[0] == 'u':
                for i in self.downAnimalList:
                    if i.position == position:
                        if i.rank < moving_animal.rank:
                            return True
                return False
            else:
                for i in self.upAnimalList:
                    if i.position == position:
                        if i.rank < moving_animal.rank:
                            return True
                return False

            # if the moving animal is NOT Elephant, the function will check whether its estimated position has a lower rank enemy
            # if_position_has_lower_rank_enemy()

    def if_position_has_higher_rank_enemy(self, moving_animal: Animals, position: tuple) -> bool:
        # 不需要
        """
        1. Purpose: check if the new position is occupied by a higher rank enemies (Rat is an excluding example here)
        2. Function parameter: "moving_animal" is passed from if_new_position_has_enemy_that_can_be_eaten from Controller, "position" is passed from get_estimated_new_position()
        3. Return value: a boolean value
        4. How to achieve:
            a)For all Animals except Elephant(8): find if the position is already occupied by enemies that have a higher rank.
            b)For Elephant(8): find if the position is already occupied by enemy Rat(1)
        """
        if (moving_animal.getRank() != '8'):
            # find if the position is already occupied by enemies that have a higher rank.
            if moving_animal.name[0] == 'u':
                for i in self.downAnimalList:
                    if i.position == position:
                        if i.rank > moving_animal.rank:
                            return True
                return False
            else:
                for i in self.upAnimalList:
                    if i.position == position:
                        if i.rank > moving_animal.rank:
                            return True
                return False
        else:
            return self.if_position_has_enemy_Rat(moving_animal, position)

    def if_next_step_in_river(self, new_position: tuple) -> bool:
        """
        1. Purpose: check if the new position is in a river square
        2. Function parameter: "new_position" is passed from get_estimated_new_position()
        3. Return value: a boolean value
        4. How to achieve: by iterating all river squares positions in a chessboard, and check whether the "position" is same as one of them
        """
        for i in self.river_position:
            if i == new_position:
                return True
            return False

    def if_position_has_enemy_Elephant(self, moving_animal: Animals, position: tuple) -> bool:
        """
        1. Purpose: check if the new position is already occupied by an enemy elephant
        2. Function parameter: "moving_animal" is passed from if_new_position_has_enemy_that_can_be_eaten from Controller, "position" is passed from get_estimated_new_position()
        3. Return value: a boolean value
        4. How to achieve: by comparing the enemy elephant's position with "position"
        """

        if moving_animal.name[0] == 'u':
            for i in self.downAnimalList:
                if i.position == position and i.name == 'downside_Elephant':
                    return True
            return False

        else:
            for i in self.downAnimalList:
                if i.position == position and i.name == 'upside_Elephant':
                    return True
            return False

    def if_position_has_enemy_Rat(self, moving_animal: Animals, position: tuple):
        """
        1. Purpose: check if the new position is already occupied by an enemy rat
        2. Function parameter: "moving_animal" is passed from if_new_position_has_enemy_that_can_be_eaten from Controller, "position" is passed from get_estimated_new_position()
        3. Return value: a boolean value
        4. How to achieve: by comparing the enemy rat's position with "position"
        """
        if moving_animal.name[0] == 'u':
            for i in self.downAnimalList:
                if i.position == position and i.name == 'downside_Rat':
                    return True
            return False

        else:
            for i in self.downAnimalList:
                if i.position == position and i.name == 'upside_Rat':
                    return True
            return False

    def if_position_has_lower_rank_enemy_except_Rat(self, moving_animal: Animals, position: tuple):
        """
        1. Purpose: This function is only used when moving_animal is Elephant. To check if the new position is occupied by a lower rank enemies except Rat.
        2. Function parameter: "moving_animal" is passed from if_new_position_has_enemy_that_can_be_eaten from Controller, "position" is passed from get_estimated_new_position()
        3. Return value: a boolean value
        4. How to achieve: by iterating all lower rank animals' positions except rat's in a chessboard, and check whether the "position" is same as one of them
        """
        if moving_animal.name[0] == 'u':
            for i in self.downAnimalList:
                if i.position == position and i.name != 'downside_Rat' and i.rank < moving_animal.rank:
                    return True
            return False

        else:
            for i in self.downAnimalList:
                if i.position == position and i.name != 'upside_Rat' and i.rank < moving_animal.rank:
                    return True
            return False


    def if_rat_in_that_river(self, side_of_river: str):
        if self.downAnimalList[0].getRiverSide() == side_of_river or self.upAnimalList[
            0].getRiverSide() == side_of_river:
            return True
        return False


if __name__ == "__main__":
    print("OK")
