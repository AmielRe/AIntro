import unittest
from Components.Board import Board
from Util.utils import MoveTypes
from Algorithms.DFS import DFS
from Algorithms.AStar import AStar

class Tests(unittest.TestCase):

    # DFS Tests
    def test_DFS_4d_easy(self):
        board = Board(4, [1, 2, 3, 4, 5, 6, 7, 8,
                      9, 10, 11, 12, 13, 0, 14, 15])
        self.assertListEqual(
            DFS(board, 2), [MoveTypes.LEFT, MoveTypes.LEFT], 'The solution is wrong!')

    def test_DFS_3d_medium(self):
        board = Board(3, [1, 2, 3, 7, 0, 5, 8, 4, 6])
        self.assertListEqual(
            DFS(board, 6), [MoveTypes.UP, MoveTypes.RIGHT, MoveTypes.DOWN, MoveTypes.LEFT, MoveTypes.LEFT, MoveTypes.UP], 'The solution is wrong!')

    def test_DFS_3d_hard(self):
        board = Board(3, [2, 1, 3, 5, 4, 0, 7, 8, 6])
        self.assertListEqual(
            DFS(board, 16), [MoveTypes.DOWN, MoveTypes.RIGHT, MoveTypes.UP, MoveTypes.RIGHT, MoveTypes.DOWN, MoveTypes.LEFT, MoveTypes.LEFT, MoveTypes.UP, MoveTypes.RIGHT, MoveTypes.RIGHT, MoveTypes.DOWN, MoveTypes.LEFT, MoveTypes.UP, MoveTypes.LEFT, MoveTypes.UP], 'The solution is wrong!')

    # AStar Tests
    def test_AStar_4d_easy(self):
        board = Board(4, [1, 2, 3, 4, 5, 6, 7, 8,
                      9, 10, 11, 12, 13, 0, 14, 15])
        self.assertListEqual(
            AStar(board), [MoveTypes.LEFT, MoveTypes.LEFT], 'The solution is wrong!')

    def test_AStar_3d_medium(self):
        board = Board(3, [1, 2, 3, 7, 0, 5, 8, 4, 6])
        self.assertListEqual(
            AStar(board), [MoveTypes.UP, MoveTypes.RIGHT, MoveTypes.DOWN, MoveTypes.LEFT, MoveTypes.LEFT, MoveTypes.UP], 'The solution is wrong!')

    def test_AStar_3d_hard(self):
        board = Board(3, [2, 1, 3, 5, 4, 0, 7, 8, 6])
        self.assertListEqual(
            AStar(board), [MoveTypes.DOWN, MoveTypes.RIGHT, MoveTypes.UP, MoveTypes.RIGHT, MoveTypes.DOWN, MoveTypes.LEFT, MoveTypes.LEFT, MoveTypes.UP, MoveTypes.RIGHT, MoveTypes.RIGHT, MoveTypes.DOWN, MoveTypes.LEFT, MoveTypes.UP, MoveTypes.LEFT, MoveTypes.UP], 'The solution is wrong!')


if __name__ == '__main__':
    unittest.main()
