from Components.Board import Board

def Ids(board: Board):
    layer = 0

    steps = run_dfs_in_layer(board, layer)
    while not steps:
        steps = run_dfs_in_layer(board, layer)

        layer += 1

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

        if len(visited) == 0:
            visited.add(board)

        new_boards = board.get_new_boards()[::-1]

        for new_board_idx in range(len(new_boards)):
            if new_boards[new_board_idx][0] in visited:
                continue
            else:
                stack.append((new_boards[new_board_idx][0], path + [new_boards[new_board_idx][1]], depth + 1))
                visited.add(new_boards[new_board_idx][0])

    return None