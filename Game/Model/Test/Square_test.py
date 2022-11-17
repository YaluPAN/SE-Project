import unittest
import Game.Model.Squares as sq


class ChessTestCase(unittest.TestCase):
    def testSquares(self):
        """
        TestCase1: whether the Chess Constructor Squares can construct a valid class without data types error or violating game rules.
        """

        a = sq.Squares()
        self.assertEqual(a.den_position, [(3, 0), (3, 8)])
        # test whether den position initialization valid
        self.assertEqual(a.trap_position, [(2, 0), (4, 0), (3, 1), (2, 8), (3, 7), (4, 8)])
        # test whether trap position initialization valid
        self.assertEqual(a.river_position, [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4),
                                            (2, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)])
        # test whether river position initialization valid

    def setUp(self) -> None:
        self.target1 = sq.Animals("downside_Rat", 1, (1, 4), True)
        self.target2 = sq.Animals("downside_Leopard", 5, (3, 8), True)
        self.target3 = sq.Animals("upside_Rat", 1, (5, 5), True)

    def testAnimals(self):
        """
        TestCase2: whether the Chess Constructor Animals can construct a valid class without data types error or violating game rules.
        """
        a = sq.Animals("downside_Rat", 1, (6, 2), True)
        b = sq.Animals("downside_Cat", 2, (1, 1), True)
        c = sq.Animals("downside_Dog", 3, (5, 1), True)
        d = sq.Animals("upside_Rat", 1, (0, 6), True)
        e = sq.Animals("upside_Dog", 3, (1, 7), True)
        f = sq.Animals("upside_Tiger", 6, (6, 8), True)
        downside_animal1 = ["downside_Rat", 1, (6, 2), True]
        downside_animal2 = ["downside_Cat", 2, (1, 1), True]
        downside_animal3 = ["downside_Dog", 3, (5, 1), True]

        downside_animal7 = ["downside_Lion", 7, (6, 0), True]
        downside_animal8 = ["downside_Elephant", 8, (0, 2), True]
        upside_animal1 = ["upside_Rat", 1, (0, 6), True]
        upside_animal2 = ["upside_Cat", 2, (5, 7), True]
        upside_animal3 = ["upside_Dog", 3, (1, 7), True]
        upside_animal4 = ["upside_Wolf", 4, (4, 6), True]
        upside_animal5 = ["upside_Leopard", 5, (2, 6), True]
        upside_animal6 = ["upside_Tiger", 6, (6, 8), True]
        upside_animal7 = ["upside_Lion", 7, (0, 8), True]
        upside_animal8 = ["upside_Elephant", 8, (6, 6), True]

        self.assertEqual([a.name, a.rank, a.position, a.status], downside_animal1)
        self.assertEqual([b.name, b.rank, b.position, b.status], downside_animal2)
        self.assertEqual([c.name, c.rank, c.position, c.status], downside_animal3)
        self.assertEqual([d.name, d.rank, d.position, d.status], upside_animal1)
        self.assertEqual([e.name, e.rank, e.position, e.status], upside_animal3)
        self.assertNotEqual([f.name, f.rank, f.position, f.status], upside_animal5)
        # test whether animal initialization valid and test all the parameter to see whether they are valid

    def testget_den_position(self):
        """
        TestCase4:test whether the function get_den_position can return all the den position
        """
        self.assertEqual(sq.Squares().get_den_position(), [(3, 0), (3, 8)])

    def testget_trap_position(self):
        """
        TestCase5:test whether the function get_trap_position can return all the traps position
        """
        self.assertEqual(sq.Squares().get_trap_position(), [(2, 0), (4, 0), (3, 1), (2, 8), (3, 7), (4, 8)])

    def testget_river_position(self):
        """
        TestCase6:test whether the function get_river_position can return all the river position
        """
        self.assertEqual(sq.Squares().get_river_position(), [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4),
                                                             (2, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)])

    def testgetRank(self):
        """
        TestCase7:test whether the function getrank can return animal's correct rank
        """
        a = sq.Animals("downside_Rat", 1, (6, 2), True)
        self.assertEqual(a.getRank(), 1)

    def testgetposition(self):
        """
        TestCase7:test whether the function getposition can return animal's correct position
        """
        b = sq.Animals("downside_Cat", 2, (1, 1), True)
        self.assertEqual(b.position, (1, 1))

    def testifInTrap(self):
        """
        TestCase8:test whether the function ifInTrap can specify the real situation that the animal in trap or not
        """
        c = sq.Animals("downside_Dog", 3, (5, 1), True)
        d = sq.Animals("upside_Rat", 1, (2, 0), True)
        self.assertEqual(c.ifInTrap(), False)  # (5,1) is not a trap position so that the function should return false
        self.assertEqual(d.ifInTrap(), True)  # (2,0) is a trap position so that the function should return true


    def testifInLand(self):
        """
        TestCase9:test whether the function ifInLand can specify the real situation that the animal in land or not
        """
        a = sq.Animals("downside_Rat", 1, (6, 2), True)
        d = sq.Animals("upside_Rat", 1, (1, 3), True)
        self.assertEqual(a.ifInLand(), True)  # (6,2) is a position on land,so the function should return true
        self.assertEqual(d.ifInLand(), False)  # (1,3) is a position on river,so the function should return true

    def test_get_river_side(self):
        """
        test 10: return which side river the animal in
        """
        self.assertEqual(self.target1.getRiverSide(), "left")
        self.assertEqual(self.target3.getRiverSide(), "right")

    def test_in_den(self):
        """
        test 10.1: return whether animal in Den
        """
        self.assertEqual(self.target1.ifInDen(), False)
        self.assertEqual(self.target2.ifInDen(), True)


    def testIfInRiver(self):
        """
        TestCase11:test whether the function ifInRiver can specify the real situation that the animal in River or not
        """
        f = sq.Animals("upside_Tiger", 6, (6, 8), True)  # (6,8) is a
        d = sq.Animals("upside_Rat", 1, (1, 3), True)
        self.assertEqual(f.ifInRiver(), False)  # (6,8) is not a river position. So the function will return false
        self.assertEqual(d.ifInRiver(),
                         True)  # (1,3) is a river position and rat is allowed to enter the river, so the function
        # should return true.

    def testMove(self):
        """
        TestCase12:test whether the function Move can let the chess go to the correct position after move
        """
        a = sq.Animals("downside_Rat", 1, (6, 2), True)
        b = sq.Animals("downside_Cat", 2, (1, 1), True)
        c = sq.Animals("downside_Dog", 3, (6, 6), True)
        d = sq.Animals("upside_Rat", 1, (0, 6), True)
        self.assertEqual(a.getPosition(), (6, 2))  # test before move , whether the position is correct
        a.move("up")
        self.assertEqual(a.getPosition(), (6, 3))  # test after move, whether the position is correct(test jump up)
        self.assertEqual(b.getPosition(), (1, 1))  # test before move , whether the position is correct
        b.move("down")
        self.assertEqual(b.getPosition(), (1, 0))  # test after move, whether the position is correct(test jump down)
        self.assertEqual(c.getPosition(), (6, 6))  # test before move , whether the position is correct
        c.move("left")
        self.assertEqual(c.getPosition(), (5, 6))  # test after move, whether the position is correct(test jump left)
        self.assertEqual(d.getPosition(), (0, 6))  # test before move , whether the position is correct
        d.move("right")
        self.assertEqual(d.getPosition(), (1, 6))  # test after move, whether the position is correct(test jump right)

    def testJumpOver(self):
        """
        TestCase13:test whether the function jumpOver can let the chess go to the correct position after jumpOver
        """
        f = sq.Animals("upside_Tiger", 6, (4, 6), True)
        g = sq.Animals("downside_Lion", 7, (5, 2), True)
        h = sq.Animals("downside_Tiger", 6, (0, 3), True)
        i = sq.Animals("upside_Lion", 7, (6, 4), True)
        self.assertEqual(g.getPosition(), (5, 2))  # test before jump over, whether the position is correct
        self.assertEqual(f.getPosition(), (4, 6))  # test before jump over, whether the position is correct
        g.jumpOver("up")
        self.assertEqual(g.getPosition(), (5, 6))  # test after jump over, whether the position is correct(test jump up)
        f.jumpOver("down")
        self.assertEqual(f.getPosition(),
                         (4, 2))  # test after jump over, whether the position is correct(test jump down)
        self.assertEqual(h.getPosition(), (0, 3))  # test before jump over, whether the position is correct
        h.jumpOver("right")
        self.assertEqual(h.getPosition(),
                         (3, 3))  # test after jump over, whether the position is correct(test jump right)
        self.assertEqual(i.getPosition(), (6, 4))  # test before jump over, whether the position is correct
        i.jumpOver("left")
        self.assertEqual(i.getPosition(),
                         (3, 4))  # test after jump over, whether the position is correct(test jump right)

    def testupMove(self):
        """
        TestCase14:test whether the function upMove is correct
        """
        a = sq.Animals("downside_Rat", 1, (5, 2), True)
        b = sq.Animals("downside_Cat", 2, (4, 2), True)
        e = sq.Animals("upside_Dog", 3, (2, 1), True)
        f = sq.Animals("upside_Tiger", 6, (2, 2), True)
        self.assertEqual(a.getPosition(), (5, 2))  # test before move , whether the position is correct
        a.upMove()
        self.assertEqual(a.getPosition(), (
            5, 3))  # test the simple case whether a rat can enter the river, rat can, so the position change
        self.assertEqual(b.getPosition(), (4, 2))  # test before move , whether the position is correct
        b.upMove()
        self.assertEqual(e.getPosition(), (2, 1))  # test before move , whether the position is correct
        e.upMove()
        # to the same player, at this time, the dog can not move.so the position should not change
        self.assertEqual(f.getPosition(), (2, 2))  # test before move , whether the position is correct

    def testDownMove(self):
        """
        TestCase15:test whether the function downMove is correct
        """
        a = sq.Animals("downside_Rat", 1, (5, 6), True)
        b = sq.Animals("downside_Cat", 2, (3, 1), True)
        c = sq.Animals("downside_Dog", 3, (3, 3), True)
        e = sq.Animals("upside_Dog", 3, (1, 7), True)
        f = sq.Animals("upside_Tiger", 6, (1, 6), True)
        self.assertEqual(a.getPosition(), (5, 6))  # test before move , whether the position is correct
        a.downMove()
        self.assertEqual(a.getPosition(), (
            5, 5))  # test the simple case whether a rat can enter the river, rat can, so the position change
        self.assertEqual(b.getPosition(), (3, 1))  # test before move , whether the position is correct
        self.assertEqual(c.getPosition(), (3, 3))  # test before move , whether the position is correct
        c.downMove()
        self.assertEqual(c.getPosition(), (3, 2))  # test the normal down move
        self.assertEqual(f.getPosition(), (1, 6))  # test before move , whether the position is correct

    def testLeftMove(self):
        """
        TestCase16:test whether the function leftMove is correct
        """
        a = sq.Animals("downside_Rat", 1, (1, 5), True)
        b = sq.Animals("downside_Cat", 2, (0, 8), True)
        c = sq.Animals("downside_Dog", 3, (4, 1), True)
        f = sq.Animals("upside_Tiger", 6, (3, 1), True)
        self.assertEqual(a.getPosition(), (1, 5))  # test before move , whether the position is correct
        a.leftMove()
        self.assertEqual(a.getPosition(), (0, 5))  # test leftMove in the simple situation work or not
        self.assertEqual(b.getPosition(), (0, 8))  # test before move , whether the position is correct
        b.leftMove()
        self.assertEqual(b.getPosition(), (-1,
                                           8))  # test after move , if the move is out of the chess board,the move
        # should not work, so the position should not change
        self.assertEqual(c.getPosition(), (4, 1))  # test before move , whether the position is correct
        self.assertEqual(f.getPosition(), (3, 1))  # test before move , whether the position is correct
        self.assertEqual(f.status, True)  # test before move, the tiger chess's status

    def testRightMove(self):
        """
        TestCase17:test whether the function rightMove is correct
        """
        a = sq.Animals("downside_Rat", 1, (2, 3), True)
        d = sq.Animals("upside_Rat", 1, (1, 3), True)
        b = sq.Animals("downside_Elephant", 8, (3, 2), True)
        self.assertEqual(a.getPosition(), (2, 3))  # test before move , whether the position is correct
        self.assertEqual(b.getPosition(), (3, 2))  # test before move , whether the position is correct
        self.assertEqual(d.getPosition(), (1, 3))  # test before move , whether the position is correct
        self.assertEqual(b.status, True)  # test before move , whether upside Rat status is correct
        self.assertEqual(a.status, True)  # test before move , whether downside  Rat status is correct

    def testJumpOverUp(self):
        """
        TestCase17:test whether the function jumpOverUp is correct
        """
        f = sq.Animals("upside_Tiger", 6, (1, 2), True)
        g = sq.Animals("downside_Dog", 3, (1, 6), True)
        self.assertEqual(f.getPosition(), (1, 2))  # test before move , whether the position is correct
        self.assertEqual(g.getPosition(), (1, 6))  # test before move , whether the position is correct
        self.assertEqual(g.status, True)  # test before move , whether downside dog status is correct
        f.jumpOverUp()
        self.assertEqual(f.getPosition(), (1, 6))  # test after move, the position of tiger

    def testJumpOverDown(self):
        """
        TestCase17:test whether the function jumpOverDown is correct
        """
        f = sq.Animals("upside_Tiger", 6, (1, 6), True)
        e = sq.Animals("upside_Dog", 3, (1, 2), True)
        self.assertEqual(f.getPosition(), (1, 6))  # test before move , whether the position is correct
        self.assertEqual(e.getPosition(), (1, 2))  # test before move , whether the position is correct
        self.assertEqual(e.status, True)  # test before move , whether upside dog status is correct
        f.jumpOverDown()
        self.assertEqual(e.status,
                         True)  # test after move, the upside dog should not be eaten, the status should be true
        self.assertEqual(f.getPosition(), (
            1,
            2))  # test after move, the position of tiger should not change since it can not eat the player's own chess

    def testJumpOverLeft(self):
        """
        TestCase17:test whether the function jumpOverLeft is correct
        """
        f = sq.Animals("upside_Tiger", 6, (3, 3), True)
        g = sq.Animals("downside_Lion", 7, (0, 3), True)
        self.assertEqual(g.getPosition(), (0, 3))  # test before move , whether the position is correct
        self.assertEqual(f.getPosition(), (3, 3))  # test before move , whether the position is correct
        self.assertEqual(g.status, True)  # test before move , whether downside lion status is correct
        f.jumpOverLeft()
        self.assertEqual(g.status,
                         True)  # test after move, the downside lion should not be eaten, the status should be true

    def testJumpOverRight(self):
        """
        TestCase17:test whether the function jumpOverRight is correct
        """
        a = sq.Animals("downside_Rat", 1, (4, 3), True)
        f = sq.Animals("upside_Tiger", 6, (3, 3), True)
        g = sq.Animals("downside_Lion", 7, (0, 3), True)
        h = sq.Animals("downside_Tiger", 6, (0, 8), True)
        self.assertEqual(g.getPosition(), (0, 3))  # test before move , whether the position is correct
        self.assertEqual(f.getPosition(), (3, 3))  # test before move , whether the position is correct
        self.assertEqual(h.getPosition(), (0, 8))
        self.assertEqual(f.status, True)  # test before move , whether upside lion status is correct
        g.jumpOverRight()
        self.assertEqual(f.status, True)  # test after move, the upside tiger should be eaten, the status should be true
        self.assertEqual(g.getPosition(), (
            3, 3))  # test after move, the position of lion should change since it can eat a lower rank chess
        g.jumpOverRight()
        self.assertEqual(g.getPosition(), (6,
                                           3))  # test after move, the position of lion should not change since the
        # rat is in the right water area to stop the lion to jump left
        h.jumpOverRight()
        self.assertEqual(h.getPosition(), (3,
                                           8))  # test after move, the position of tiger should not change because it
        # is not neat the water, so it can not jump


if __name__ == '__main__':
    unittest.main()
