from Util.utils import MoveTypes
from Components.Board import Board


def DFS(board, max_depth):
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

        if board.can_move_right(row, col - 1):
            temp_board = Board(board.length(), board.get_board_state())
            temp_board.move_right(row, col - 1)
            if temp_board not in visited:
                stack.append((temp_board, path + [MoveTypes.RIGHT], depth + 1))

        if board.can_move_left(row, col + 1):
            temp_board = Board(board.length(), board.get_board_state())
            temp_board.move_left(row, col + 1)
            if temp_board not in visited:
                stack.append((temp_board, path + [MoveTypes.LEFT], depth + 1))

        if board.can_move_down(row - 1, col):
            temp_board = Board(board.length(), board.get_board_state())
            temp_board.move_down(row - 1, col)
            if temp_board not in visited:
                stack.append((temp_board, path + [MoveTypes.DOWN], depth + 1))

        if board.can_move_up(row + 1, col):
            temp_board = Board(board.length(), board.get_board_state())
            temp_board.move_up(row + 1, col)
            if temp_board not in visited:
                stack.append((temp_board, path + [MoveTypes.UP], depth + 1))

    return None
