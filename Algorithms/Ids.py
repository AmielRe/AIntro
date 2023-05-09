import string
from Components.Board import Board
from collections import deque
from Util.utils import MoveTypes


def Ids(board: Board, max_depth):
    layer = 0

    goal: list[int] = board.get_goal_state()

    steps: list[string]

    while True:
        stack = deque()
        stack.append(board)
        visited = set()
        steps = run_dfs_in_layer(stack, visited, goal, layer, [])

        if steps is not None or layer > max_depth:
            break
        layer += 1

    if not steps:
        return []

    return list(reversed(steps))

def run_dfs_in_layer(stack: deque, visited, goal: list[int], layer: int, array: list[MoveTypes]):
    node = stack.pop()

    if node.__str__() not in visited and layer > -1:
        if node.get_board_state() == goal:
            return []

        visited.add(node.__str__())

        # Get all available movements and reverse the order
        new_boards = node.get_new_boards()[::-1]

        moves = []

        for new_board_inx in range(0, len(new_boards)):
            stack.append(new_boards[new_board_inx][0])
            steps_to_goal = run_dfs_in_layer(stack, visited, goal, layer - 1, array + [new_boards[new_board_inx][1]])

            if steps_to_goal is not None:
                moves = steps_to_goal

                moves.append(new_boards[new_board_inx][1])

        if moves:
            return moves
