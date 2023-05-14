import string
from Components.Board import Board
from collections import deque
from Util.utils import MoveTypes

def Ids(board: Board):
    layer = 0

    goal: list[int] = board.get_goal_state()

    steps: list[MoveTypes]

    while True:

        steps = run_dfs_in_layer(board, layer)

        if steps is not None:
            break
        layer += 1

    if not steps:
        return []

    return list(steps)

def run_dfs_in_layer(board, max_depth):
    """
    Iterative depth-limited search algorithm to solve the sliding puzzle board.
    Returns the path of movements required to solve the board.
    """

    stack = [(board, [], 0)]
    visited = set()

    while stack:
        board, path, depth = stack.pop()

        if board.get_board_state() == board.get_goal_state():
            return path

        if depth == max_depth:
            continue

        if board in visited:
            continue

        visited.add(board)

        row, col = board.find_zero_index()
        if row is None:
            continue

        new_boards = list(reversed(board.get_new_boards()));

        for new_board_idx in range(len(new_boards)):
            stack.append((new_boards[new_board_idx][0], path + [new_boards[new_board_idx][1]], depth + 1))

    return None