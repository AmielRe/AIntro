import string

from Components.Board import Board
from collections import deque

from Util.utils import MoveTypes

def get_new_boards(board: Board):
    possible_moves = []
    empty_item_pos = board.get_board_state().index(0)
    empty_row = empty_item_pos // board.width()
    empty_col = empty_item_pos % len(board[empty_row])

    if empty_row + 1 < board.width() and board.can_move_up(empty_row + 1, empty_col):  # move empty item up
        new_board = Board(board.width(), board.get_board_state())
        new_board.move_up(empty_row + 1, empty_col)
        possible_moves.append((new_board, MoveTypes.UP))

    if board.can_move_down(empty_row - 1, empty_col):  # move empty item down
        new_board = Board(board.width(), board.get_board_state())
        new_board.move_down(empty_row - 1, empty_col)
        possible_moves.append((new_board, MoveTypes.DOWN))

    if empty_col + 1 < len(board[empty_row]) and board.can_move_left(empty_row, empty_col + 1):  # move empty item left
        new_board = Board(board.width(), board.get_board_state())
        new_board.move_left(empty_row, empty_col + 1)
        possible_moves.append((new_board, MoveTypes.LEFT))

    if board.can_move_right(empty_row, empty_col - 1):  # move empty item right
        new_board = Board(board.width(), board.get_board_state())
        new_board.move_right(empty_row, empty_col - 1)
        possible_moves.append((new_board, MoveTypes.RIGHT))

    return possible_moves


def ids(board: Board):
    layer = 0

    goal: list[int] = board.get_goal_state()

    steps: list[string]

    while True:
        stack = deque()
        stack.append(board)
        visited = set()
        steps = run_dfs_in_layer(stack, visited, goal, layer)

        if steps is not None or len(visited) == len(goal):
            break
        layer += 1

    return reversed(steps)


def run_dfs_in_layer(stack: deque, visited, goal: list[int], layer: int):
    node = stack.pop()

    if node.__str__() not in visited and layer > -1:
        if node.get_board_state() == goal:
            return []

        visited.add(node.__str__())

        new_boards = get_new_boards(node)

        moves = []

        for new_board in new_boards:
            stack.append(new_board[0])
            steps_to_goal = run_dfs_in_layer(stack, visited, goal, layer - 1)

            if steps_to_goal is not None:
                moves = steps_to_goal

                moves.append(new_board[1])

        if moves:
            return moves
