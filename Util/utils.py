from enum import Enum


class SearchAlgorithms(Enum):
    IDS = 1
    BFS = 2
    A_STAR = 3
    IDA_STAR = 4
    DFS = 5

class MovePriority(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class MoveTypes(Enum):
    RIGHT = 'R'
    LEFT = 'L'
    UP = 'U'
    DOWN = 'D'


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def getAlgorithmFromInt(algoNum):
    try:
        return SearchAlgorithms(algoNum)
    except ValueError:
        return None
