from Components.Board import Board
from Algorithms.AStar import AStar

def IDA(board: Board):
    """
    IDA (Iterative Deep A* Algorithm)
    """
    layer = 0

    while True:
        steps = AStar(board, layer)

        if steps is not None:
            break
        layer += 1

    if not steps:
        return []

    return steps