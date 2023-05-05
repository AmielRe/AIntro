import unittest
from Components.Board import Board
from Util.utils import MoveTypes
from Algorithms.Ids import Ids


class Ids_tests(unittest.TestCase):
    def test_DFS_4d_easy(self):
        board = Board(4, [1, 2, 3, 4, 5, 6, 7, 8,
                          9, 10, 11, 12, 13, 0, 14, 15])
        self.assertListEqual(
            Ids(board, 2), [MoveTypes.LEFT, MoveTypes.LEFT], 'The solution is wrong!')

    def test_Ids_3d_medium(self):
        board = Board(3, [1, 2, 3, 7, 0, 5, 8, 4, 6])
        self.assertListEqual(
            Ids(board, 6),
            [MoveTypes.UP, MoveTypes.RIGHT, MoveTypes.DOWN, MoveTypes.LEFT, MoveTypes.LEFT, MoveTypes.UP],
            'The solution is wrong!')

    def test_Ids_3d_hard(self):
        board = Board(3, [2, 1, 3, 5, 4, 0, 7, 8, 6])
        self.assertListEqual(
            Ids(board, 26),
            [MoveTypes.RIGHT, MoveTypes.DOWN, MoveTypes.RIGHT, MoveTypes.UP, MoveTypes.LEFT, MoveTypes.LEFT,
             MoveTypes.DOWN, MoveTypes.RIGHT, MoveTypes.RIGHT, MoveTypes.UP, MoveTypes.LEFT, MoveTypes.DOWN,
             MoveTypes.LEFT, MoveTypes.UP, MoveTypes.UP], 'The solution is wrong!')


if __name__ == '__main__':
    unittest.main()
