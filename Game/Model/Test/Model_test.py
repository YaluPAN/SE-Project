import unittest
import sys
import pathlib

path = str(pathlib.Path(__file__).parent.resolve())
path = "\\".join(path.split("\\")[:-2])
sys.path.append(path)
import Game.Model.Model as md
from unittest.mock import MagicMock
from unittest.mock import Mock


class ChessboardTest(unittest.TestCase):
    def setUp(self) -> None:
        self.md = md.Model()
    def test_ifCanMove(self):
        """
        There are totally 5 situations when an Animal Chess is moved:
            a)The animal's next step in out of chessboard range
            b)The animal's next step is on land
                i) a rat is going to jump out of river
                    1) there is no animals on the rat's next step
                    2) there is an animal in front its way

                ii) will be tested in test_if_new_position_has_enemy_that_can_be_eaten()
                ii) an animal is going to capture another opponent animal
                    1) common rule
                    2) rat eat an elephant

                iii) a push ,backup, left move or right move
                    1) the same side animal blocked the way
            c)The animal's next step is in River

                i) will be tested in test_if_new_position_has_enemy_that_can_be_eaten()
                i) rat in river
                    1) rat swim in river
                    2) rat in river going to capture another river

                ii) a lion, tiger will jump over a rat
                    1) they cannot jump over the river when a rat in the same river
                iii) other animals cannot attack a rat in river
        :return:
        """
        mock = Mock()

        # test for a
        rat1: md.Animals = self.md.downAnimalList[0]
        self.md.get_estimated_new_position = MagicMock()
        self.md.if_move_out_of_range = MagicMock()
        self.assertEqual(self.md.ifCanMove(rat1, "right")[0], False)
        # check self.md.get_estimated_new_position's call value
        self.md.get_estimated_new_position.assert_called_with(rat1, "right")
        self.md.if_move_out_of_range.assert_called_with((7, 2))

        # test for b-i-1  get_estimated_new_position will be executed every time
        # so here we won't test it
        rat1.position = (1, 3)
        self.assertEqual(self.md.ifCanMove(rat1, "left")[0], True)

        # test for (False, Hint3)
        cat1: md.Animals = self.md.downAnimalList[1]
        rat2: md.Animals = self.md.upAnimalList[0]
        rat2.position, cat1.position = (3, 6), (3, 5)
        self.assertEqual(self.md.ifCanMove(rat2, "down")[0], False)

        # test for (False, Hint4)
        cat1.position, rat1.position = (1, 1), (3, 5)
        self.assertEqual(self.md.ifCanMove(rat2, "down"), False)

        rat1.position = (6, 2)
        self.assertEqual(self.md.ifCanMove(rat2, "down"), True)

        # test for b-i-2
        wolf1 = self.md.upAnimalList[3]
        wolf1.position = (0, 3)

        self.assertEqual(self.md.ifCanMove(rat1, "left")[0], False)

        # test for b-iii
        wolf1.position, rat1.position = (6, 3), (6, 2)
        self.assertEqual(self.md.ifCanMove(rat1, "up")[0], False)

        elephant = self.md.upAnimalList[7]
        elephant.position = (6, 3)
        self.assertEqual(self.md.ifCanMove(elephant, "down")[0], False)

        # test for C-ii-1
        dog1: md.Animals = self.md.downAnimalList[2]
        dog1.position = (5, 2)
        self.assertEqual(self.md.ifCanMove(dog1, "up"), False)

        # test for C-iii
        lion1: md.Animals = self.md.upAnimalList[6]
        lion1.position, rat1.position = (2, 6), (2, 5)
        self.assertEqual(self.md.ifCanMove(lion1, "down"), False)

        # test for C-iii
        lion1.position = (0, 8)
        self.assertEqual(self.md.ifCanMove(lion1, "down"), True)

    def test_if_in_opposite_den(self):
        wolf1 = self.md.upAnimalList[3]
        wolf1.position = (3, 7)
        result = self.md.if_in_opposite_den(wolf1, 'up', 'move')
        self.assertEqual(result, False)

    def test_if_new_position_has_enemy_that_can_be_eaten(self) -> None:
        """
        1)in Land 1.1 All animals except Rat(1), can eat enemy that have the same/lower rank 1.2 Rat(1) can eat enemy
        Elephant(8) and Rat(1) The case that a Rat move from the water to attack enemy Elephant/Rat is NOT allowed.
        This case is already checked by ifCanMove() before this func. 2)in River only Rat(1) will in River. In this
        case, it can eat enemy Rat(1). 3)in Trap All animal in traps can eat any enemy pieces 4)in Den the side of
        the animal will win if the animal move to opponent's side. Because in this case, the animal will not care
        eating enemy anymore :return:
        """
        rat1, elephant = self.md.upAnimalList[0], self.md.downAnimalList[7]
        # a rat chess process a normal push from (6,2) to (6,3)
        self.assertEqual(self.md.if_new_position_has_enemy_that_can_be_eaten(rat1), False)

        wolf1 = self.md.upAnimalList[3]
        wolf1.position = (0, 3)
        elephant.position = (0, 3)
        # an elephant chess is going to eliminate the opponent wolf chess
        self.assertEqual(self.md.if_new_position_has_enemy_that_can_be_eaten(elephant), True)

        rat2 = self.md.downAnimalList[0]
        rat1.position, rat2.position = (1, 5), (1, 5)
        # at this time, both two rat are in river. they can elimate each other
        self.assertEqual(rat1.ifInRiver(), True)
        self.assertEqual(self.md.if_new_position_has_enemy_that_can_be_eaten(rat1), True)

        # wolf1 is upside, but it also could be any enemy eliminate as long as it fall into trap
        wolf1.position = (2, 8)
        self.assertEqual(wolf1.ifInTrap(), True)
        self.assertEqual(wolf1.rank, 0)
        self.assertEqual(self.md.if_new_position_has_enemy_that_can_be_eaten(wolf1), True)

        # if one animal go into opponent's dan
        elephant.position = (3, 0)
        self.assertEqual(elephant.ifInDen(), True)
        self.assertEqual(self.md.if_in_Den(elephant), True)

    def test_move(self) -> None:
        wolf1, rat1, leopard1 = self.md.downAnimalList[3], self.md.upAnimalList[0], self.md.downAnimalList[4]
        wolf1.move("up")
        self.assertEqual(wolf1.getPosition(), (2, 2))  # river is in front of downside wolf, so its position won't
        # change
        self.assertEqual(rat1.getPosition(), (0, 6))  # use unmoved chess as reference
        rat1.move("down")
        self.assertEqual(rat1.getPosition(), (0, 5))
        self.assertEqual(leopard1.getPosition(), (4, 2))
        leopard1.move("left")
        self.assertEqual(leopard1.getPosition(), (3, 2))

    def test_jumpover(self) -> None:
        """
        this function has been clearly tested in test_square, so here is just a brief test
        :return:
        """
        cat1, lion1, tiger1 = self.md.upAnimalList[1], self.md.downAnimalList[6], self.md.upAnimalList[5]
        cat1.position, lion1.position = (5, 6), (6, 3)
        try:
            cat1.jumpOver("up")
        except AttributeError:
            pass

        self.assertEqual(self.md.jumpOver(lion1, "left"), (3, 3))  # here, no rat at river!
        tiger1.position = (1, 6)
        self.assertEqual(self.md.jumpOver(tiger1, "down"), (1, 2))
    def test_get_same_position_enemy(self):
        cat1, dog2 = self.md.upAnimalList[1], self.md.downAnimalList[2]
        cat1.position = (3, 4)
        dog2.position = (3, 4)
        self.assertEqual(self.md.get_same_position_enemy(dog2),'upside_Cat')

    def test_die(self) -> None:
        cat1: md.Animals = self.md.upAnimalList[1]
        self.md.die(cat1)
        self.assertEqual(cat1.status, False)

    def test_get_estimated_new_position(self) -> None:
        """
        because this is only the first step to check the validity of the movement
        so for this question it won't care about whether the result contain negative
        number, result is correct or not.
        :return: None
        """
        rat1: md.Animals = self.md.downAnimalList[0]
        temp: tuple = md.Model().get_estimated_new_position(rat1, "left", 'move')
        temp1: tuple = md.Model().get_estimated_new_position(rat1, "right", 'move')
        self.assertEqual(temp, (5, 2))
        self.assertEqual(temp1, (7, 2))

    def test_if_move_out_of_range(self) -> None:
        """
        we will test in total six situations:
        1. at Original point
        2. out of board, in the bottom left direction
        3. in the river
        4. out of board, int the top right direction
        5. at downside den
        :return:
        """
        temp = md.Model()
        self.assertEqual(temp.if_move_out_of_range((0, 0)), False)
        self.assertEqual(temp.if_move_out_of_range((-1, -5)), True)
        self.assertEqual(temp.if_move_out_of_range((1, 4)), False)
        self.assertEqual(temp.if_move_out_of_range((9, 4)), True)
        self.assertEqual(temp.if_move_out_of_range((3, 0)), False)

    def test_if_next_step_in_land(self) -> None:
        """
        1. in the left river
        2. in the right river
        3. a random point on the land of board
        4. a position one step near the river
        in fact, before calling this method, we have already filtered out the situation
        that chess will out of board, so this function won't check it
        :return:
        """
        self.assertEqual(self.md.if_next_step_in_land((2, 5)), False)
        self.assertEqual(self.md.if_next_step_in_land((4, 3)), True)
        self.assertEqual(self.md.if_next_step_in_land((3, 1)), False)
        self.assertEqual(self.md.if_next_step_in_land((1, 6)), False)

    def test_if_position_has_same_side_animal(self) -> None:
        """
        1. the position stands an enemy chess
        2. the position stands the same side chess
        3. the position stands nothing
        :return:
        ps: the dead chess will immediately be deleted or switched to another container
        the pos is new position of elephant1, program will iterator through two chesslist to
        look for whether there is a chess stay the same place with "pos"
        """
        self.md.downAnimalList[7].position = (6, 2)  # the enemy chess on the next step of moving chess
        elephant1: md.Animals = md.Animals("upside_Elephant", 8, (5, 2), True)
        pos: tuple = self.md.get_estimated_new_position(elephant1, "right", 'move')
        self.assertEqual(self.md.if_position_has_same_side_animal(elephant1, pos), False)
        self.md.upAnimalList[5].position = (6, 2)
        self.assertEqual(self.md.if_position_has_same_side_animal(elephant1, pos), True)

        # restore the position of chess in List, so the next step of moving elephant is an empty position
        self.md.downAnimalList[7].position, self.md.upAnimalList[5].position = (0, 2), (2, 6)
        self.assertEqual(self.md.if_position_has_same_side_animal(elephant1, pos), False)

    def test_if_position_has_same_rank_enemy(self) -> None:
        """
        1. the position stands a same rank enemy
        2. the position with a different rank enemy,
        3. a rat is going to jump out of river but there is an enemy rat on the way
        4. a rat going to capture another rat in the river
        :return:
        ps: the calling of if_position_has_same_side_animal is before this function, so
        the only possible left here must be an enemy chess (function input require an animal
        class, cannot input an empty position in)
        """
        dog1: md.Animals = self.md.upAnimalList[2]  # upside dog
        dog2: md.Animals = self.md.downAnimalList[2]  # downside dog
        cat1: md.Animals = self.md.downAnimalList[1]  # downside cat
        pos: tuple = self.md.get_estimated_new_position(dog1, "right", 'move')
        # met with the same rank enemy
        dog2.position = (2, 7)
        self.assertEqual(self.md.if_position_has_same_rank_enemy(dog1, pos), True)
        # met with different rank enemy
        cat1.position = (2, 7)
        self.assertEqual(self.md.if_position_has_same_rank_enemy(cat1, pos), False)

        rat1, rat2 = self.md.upAnimalList[0], self.md.downAnimalList[0]
        rat1.position, rat2.position = (2, 3), (2, 4)
        # now upside rat rat1 is gonna right jump out of river, but there is a downside rat on its way
        rat1.move('right')
        self.assertEqual(self.md.if_position_has_same_rank_enemy(rat1, (2, 4)), True)

        # downside rat rat2 now in the same river with rat1
        rat2.position = (2, 2)
        self.assertEqual(self.md.if_position_has_same_rank_enemy(rat1, (2, 3)), False)

    def test_if_position_has_lower_rank_enemy(self) -> None:
        """
        1. two common animal (expected rat and elephant), moving one is lower
        2. two common animal (expected rat and elephant), moving one is higer
        3. an elephant cant eat rat
        :return:
        in our system, before judging two animals' rank in this function, rat chess has been excluded
        """
        dog1, wolf1, cat1, rat1, elephant1 = self.md.downAnimalList[2], self.md.upAnimalList[3], self.md.upAnimalList[
            1], self.md.upAnimalList[0], self.md.downAnimalList[7]
        dog1.position = (3, 2)

        wolf1.position = (3, 3)
        self.assertEqual(self.md.if_position_has_lower_rank_enemy(dog1, (3, 3)), False)

        cat1.position = (3, 5)
        self.assertEqual(self.md.if_position_has_lower_rank_enemy(dog1, (3, 5)), True)

        rat1.position, elephant1.position = (6, 4), (6, 5)
        self.assertEqual(self.md.if_position_has_lower_rank_enemy(elephant1, (6, 4)), True)

    def test_if_position_has_higher_rank_enemy(self) -> None:
        """
        1. a rat going to jump out of water
        2. a square that already occupied by enemies that have a higher rank
        :return:
        in our system, this function is applied to situations without elephant involved
        """
        leopard2, elephant1, leopard1, wolf1 = self.md.downAnimalList[4], self.md.downAnimalList[7], \
                                               self.md.upAnimalList[4], self.md.downAnimalList[3]
        leopard1.position, elephant1.position = (1, 5), (1, 6)
        self.assertEqual(self.md.if_position_has_higher_rank_enemy(leopard1, (1, 6)), True)

        wolf1.position, leopard1.position = (3, 5), (3, 6)
        self.assertEqual(self.md.if_position_has_higher_rank_enemy(leopard1, (3, 5)), False)

    def test_if_next_step_in_river(self) -> None:
        """
        only used to test whether next step will cross in river
        :return:
        """
        self.assertEqual(self.md.if_next_step_in_river((1, 3)), True)
        self.assertEqual(self.md.if_next_step_in_river((5, 6)), False)
        self.assertEqual(self.md.if_next_step_in_river((2, 4)), True)

    def test_if_position_has_enemy_Elephant(self) -> None:
        """
        system will iterate through two chess list two match with two elephants' position
        then compare with current moving chess's next step location
        1. there isn't an elephant (empty position)
        2. there isn't an elephant, but with a same side elephant
        2. there is an enemy elephant
        :return:
        """
        animals, elephant1, elephant2 = self.md.upAnimalList[3], self.md.downAnimalList[7], self.md.upAnimalList[7]

        # the enemy elephant on the way
        self.assertEqual(self.md.if_position_has_enemy_Elephant(animals, (0, 2)), True)

        # the same side on the way
        elephant2.position = (3, 6)
        self.assertEqual(self.md.if_position_has_enemy_Elephant(animals, (3, 6)), False)

        # nothing on the way
        self.assertEqual(self.md.if_position_has_enemy_Elephant(animals, (1, 2)), False)

    def test_if_position_has_enemy_Rat(self) -> None:
        """
        1. there is an enemy rat
        2. there isnt--empty position
        3. there isnt--same side rat
        :return:
        """
        rat1, rat2, wolf1, cat1 = self.md.upAnimalList[0], self.md.downAnimalList[0], self.md.upAnimalList[3], \
                                  self.md.downAnimalList[1]
        rat1.position, cat1.position = (3, 6), (3, 5)
        self.assertEqual(self.md.if_position_has_enemy_Rat(cat1, (3, 6)), True)

        rat1.position = (0, 6)
        self.assertEqual(self.md.if_position_has_enemy_Rat(cat1, (0,5)), False)

        rat2.position = (4, 6)
        self.assertEqual(self.md.if_position_has_enemy_Rat(cat1, (4,6)), False)

        # with other enemy animals
        wolf1.position = (5, 6)
        self.assertEqual(self.md.if_position_has_enemy_Rat(wolf1, (0,6)), False)

    def test_if_position_has_lower_rank_enemy_except_Rat(self) -> None:
        """
        1. empty position
        2. not rat with a lower rank
        3. is a same side rat
        4. is an enemy rat
        :return:
        """
        rat1, rat2, lion1, elephant = self.md.downAnimalList[0], self.md.upAnimalList[0], self.md.downAnimalList[6], \
                                      self.md.upAnimalList[7]
        rat1.position = (2, 4)
        lion1.position = (4, 7)
        self.assertEqual(self.md.if_position_has_lower_rank_enemy_except_Rat(elephant, (2, 3)), False)
        self.assertEqual(self.md.if_position_has_lower_rank_enemy_except_Rat(elephant, (4, 7)), True)
        self.assertEqual(self.md.if_position_has_lower_rank_enemy_except_Rat(elephant, (2, 4)), False)

    def test_if_rat_in_that_river(self) -> None:
        """
        1. two rat in two different river
        2. one rat in any of the river, the other on land
        3. no rat in river
        :return:
        """
        rat1: md.Animals = self.md.downAnimalList[0]
        rat1.position = (4, 5)
        rat2: md.Animals = self.md.upAnimalList[0]
        rat2.position = (2, 5)
        self.assertEqual(self.md.if_rat_in_that_river("left"), True)



if __name__ == "__main__":
    unittest.main()
