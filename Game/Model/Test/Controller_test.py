import os
import unittest
from mock import patch

import Game.Model.Model
import Game.Model.Model as md
import Game.View.View as view
from Game.Controller.Controller import Controller

class ControllerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.model = md.Model()
        self.view = view.View()
        self.ctl = Controller(self.model, self.view)

    @patch('Game.Controller.Controller.Controller')
    @patch("builtins.input", return_value="up")
    def test_chooseSide(self, m, mock_chooseSide) -> None:
        """
        test when user input correct value
        """
        cs = self.ctl
        cs.chooseSide()
        self.assertTrue(mock_chooseSide.called)

    @patch('Game.Controller.Controller.Controller')
    @patch("builtins.input", return_value="down")
    def test_chooseSide_0(self, m, mock_chooseSide) -> None:
        """
        test when user input correct value
        """
        cs = self.ctl
        cs.chooseSide()
        self.assertTrue(mock_chooseSide.called)

    @patch('Game.Controller.Controller.Controller')
    @patch("builtins.input", return_value = "upt")
    def test_chooseSide_1(self, m, mock_chooseSide) -> None:
        """
        test when user input wrong input
        """
        cs = self.ctl
        with self.assertRaises(RecursionError) as re:
            cs.chooseSide()
            mock_chooseSide.get.assert_called_once()

    @patch('Game.Controller.Controller.Controller')
    @patch("builtins.input", side_effect=["exit", "yes"])
    def test_executeInput(self, m, mock_processing) -> None:
        """
        test when user input correct value
        """
        cs = self.ctl
        cs.executeInput()
        self.assertTrue(mock_processing.called)

    def test_wordProcessing(self):
        self.assertEqual(self.ctl.wordProcess(["sdf", "tiger", "left"]), True)
        self.assertEqual(self.ctl.wordProcess(["move", "tigeu", "right"]), False)
        self.assertEqual(self.ctl.wordProcess(["jump", "lion", "letd"]), False)

    def test_commandRecord(self, inputs: str):
        previous = os.path.getsize("/history.txt")
        commandRecord(inputs)
        now = os.path.getsize("/history.txt")
        self.assertTrue(now > previous)

    # @patch("Game.Controller.Controller.Controller.finalPrint")
    def test_final_print(self):
        with self.assertRaises(SystemExit):
            self.ctl.finalPrint()

    @patch("builtins.input", return_value="yes")
    def test_AdmitPatch(self, m):
        with self.assertRaises(SystemExit):
            self.ctl.AdmitDefeat()

    @patch("builtins.input", return_value = "yes")
    def test_Exit(self, m):
        with self.assertRaises(SystemExit):
            self.ctl.Exit()

    def test_returnOpponent(self):
        moving = self.model.upAnimalList[0]
        self.assertEqual(self.ctl.returnOpponent(moving), self.model.downAnimalList)

    @patch("Game.Controller.Controller.Controller.returnOpponent")
    def test_alldead(self, mock_opp):
        moving = self.model.downAnimalList[4]
        self.ctl.all_dead(moving)
        self.assertTrue(mock_opp.called)
        self.assertFalse(self.ctl.all_dead(moving))

    @patch("Game.Model.Model.Model.if_in_opposite_den")
    def test_if_end(self, mock_ifinopden):
        moving = self.model.downAnimalList[3]
        direction = "left"
        action = "move"
        self.ctl.ifEnd(moving, direction, action)
        self.assertTrue(mock_ifinopden.called)

    @patch("Game.Controller.Controller.Controller.ifEnd")
    def test_if_end_1(self, mock_ifalldead):
        moving = self.model.downAnimalList[3]
        direction = "left"
        action = "move"
        self.ctl.ifEnd(moving, direction, action)
        self.assertTrue(mock_ifalldead.called)