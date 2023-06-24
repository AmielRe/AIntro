from Components.Board import Board
from Algorithms.AStar import AStar
import sys

def IDA(board: Board):
    """
    IDA (Iterative Deep A* Algorithm) search algorithm to solve the sliding puzzle board.
    Returns the path of movements required to solve the board.
    """
    threshold = [0]

    while True:
        # Call AStar with threshold (passed as array of 1 int because we want to change it inside the function for the next iteration)
        steps = AStar(board, threshold)

        if steps is not None:
            break

    if not steps:
        return []

    return steps
