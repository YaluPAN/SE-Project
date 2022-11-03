import unittest
from unittest import mock
import sys
sys.path.append("../")
sys.path.append("../..")


class ChessTestCase(unittest.TestCase):
    def setup(self):
        ''' 
        TestCase1: whether the Chess Constructor can construct a valid class without data types error or violating game rules.
        '''
        downside_animal1 = ["downside_Rat", 1, (6, 2), True]
        downside_animal2 = ["downside_Cat", 2, (1, 1), True]
        downside_animal3 = ["downside_Dog", 3, (5, 1), True]
        downside_animal4 = ["downside_Wolf", 4, (2, 2), True]
        downside_animal5 = ["downside_Leopard", 5, (4, 2), True]
        downside_animal6 = ["downside_Tiger", 6, (0, 0), True]
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

        # Elephant 象
        # 7 Lion 獅
        # 6 Tiger 虎
        # 5 Leopard 豹
        # 4 Wolf 狼
        # 3 Dog 狗
        # 2 Cat 貓
        # 1 Rat

        

    # TestCase: whether the rat can move successfully into the river,

    '''
    TestCase: whether A piece may capture any enemy piece in one of the player's trap squares regardless of rank
    1. a piece is in its side's trap, so that any enemy piece can capture it
    2. a piece is in enemy side's trap, so that any enemy piece can capture it too
    
    关于trap的判断
    棋子如果到了trap的位置 就看有无敌方棋子在同一个位置上，如果有，就吃掉。

    '''

    # TestCase: whether
