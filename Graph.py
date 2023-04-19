import math
from SearchAlgorithms import SearchAlgorithms
from Node import Node
import copy


def inputToGraph(algoNum, boardSize, inputList):
    if (not isValidInput(algoNum, boardSize, inputList)):
        return None

    return Node(inputList)


def canMoveLeft(graph, boardSize):
    index_of_zero = graph.data.index(0)
    return index_of_zero + 1 <= boardSize**2 and index_of_zero + 1 >= 0


def moveLeft(graph, boardSize):
    index_of_zero = graph.data.index(0)

    if (canMoveLeft(graph, boardSize)):
        tempGraph = copy.deepcopy(graph)
        tempGraph.data[index_of_zero] = tempGraph.data[index_of_zero + 1]
        tempGraph.data[index_of_zero + 1] = 0
        return Node(tempGraph.data)

    return None


def canMoveRight(graph, boardSize):
    index_of_zero = graph.data.index(0)
    return index_of_zero - 1 <= boardSize**2 and index_of_zero - 1 >= 0


def moveRight(graph, boardSize):
    index_of_zero = graph.data.index(0)

    if (canMoveRight(graph, boardSize)):
        tempGraph = copy.deepcopy(graph)
        tempGraph.data[index_of_zero] = tempGraph.data[index_of_zero - 1]
        tempGraph.data[index_of_zero - 1] = 0
        return Node(tempGraph.data)

    return None


def canMoveUp(graph, boardSize):
    index_of_zero = graph.data.index(0)
    return index_of_zero + boardSize <= boardSize**2 and index_of_zero + boardSize >= 0


def moveUp(graph, boardSize):
    index_of_zero = graph.data.index(0)

    if (canMoveUp(graph, boardSize)):
        tempGraph = copy.deepcopy(graph)
        tempGraph.data[index_of_zero] = tempGraph.data[index_of_zero + boardSize]
        tempGraph.data[index_of_zero + boardSize] = 0
        return Node(tempGraph.data)

    return None


def canMoveDown(graph, boardSize):
    index_of_zero = graph.data.index(0)
    return index_of_zero - boardSize <= boardSize**2 and index_of_zero - boardSize >= 0


def moveDown(graph, boardSize):
    index_of_zero = graph.data.index(0)

    if (canMoveDown(graph, boardSize)):
        tempGraph = copy.deepcopy(graph)
        tempGraph.data[index_of_zero] = tempGraph.data[index_of_zero - boardSize]
        tempGraph.data[index_of_zero - boardSize] = 0
        return Node(tempGraph.data)

    return None


def isValidInput(algoNum, boardSize, inputList):
    matching_algorithm = None
    try:
        matching_algorithm = SearchAlgorithms(algoNum)
    except ValueError:
        pass

    if matching_algorithm is None:
        return False

    if (boardSize <= 0):
        return False

    if (math.sqrt(len(inputList)) != boardSize):
        return False

    return True
