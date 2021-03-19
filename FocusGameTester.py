# Author: Breanna Moore
# Date: 12/11/2020
# Description: Unit Testing for FocusGame file.


import unittest
from FocusGame import Player, Board, FocusGame

var = unittest.TestLoader


class TestFocusGame(unittest.TestCase):
    """Contains unit tests for the FocusGame class methods."""

    @classmethod
    def setUpClass(cls):
        print("setupClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        self.game = FocusGame(("John", "Green"), ("Sarah", "Red"))

    def tearDown(self):
        pass

    def test_player_name(self):
        self.assertEqual(self.game.get_player1().get_name(), "John")
        self.assertEqual(self.game.get_player2().get_name(), "Sarah")

    def test_player_color(self):
        self.assertEqual(self.game.get_player1().get_color(), "Green")
        self.assertEqual(self.game.get_player2().get_color(), "Red")

    def test_game_state(self):
        self.assertEqual(self.game.get_game_state(), "STILL IN PLAY")

    def test_player_reserves(self):
        self.assertEqual(self.game.get_player1().get_reserves(), 0)
        self.assertEqual(self.game.get_player2().get_reserves(), 0)

    def test_player_captured(self):
        self.assertEqual(self.game.get_player1().get_captured(), 0)
        self.assertEqual(self.game.get_player2().get_captured(), 0)

    def test_board_stacks(self):
        self.assertListEqual(self.game.show_pieces((0,0)), ["Green"])
        self.assertListEqual(self.game.show_pieces((0,2)), ["Red"])
        self.assertListEqual(self.game.show_pieces((5,3)), ["Green"])
        self.assertListEqual(self.game.show_pieces((5,5)), ["Red"])



def main():
    """main function"""


if __name__ == '__main__':
    unittest.main()