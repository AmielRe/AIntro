from Graph import *


def main():

    with open('input.txt', 'r') as file:
        lines = file.readlines()
        algoNum = int(lines[0].rstrip('\n'))
        boardSize = int(lines[1].rstrip('\n'))
        inputBoard = [int(x) for x in lines[2].split("-")]
    graph = inputToGraph(algoNum, boardSize, inputBoard)

    # Check graph is created and format is valid
    if (graph == None):
        print("Invalid input, please check format!")
        return

    # If we got here, input is good and initial state is in 'graph'
    print("-------------------- BFS --------------------")

    # RUN BFS

    # Output BFS result

    print("---------------------------------------------")

    print("-------------------- DFS --------------------")

    # RUN DFS

    # Output DFS result

    print("---------------------------------------------")

    print("-------------------- A* --------------------")

    # RUN A*

    # Output A* result

    print("---------------------------------------------")

    print("-------------------- Last algo --------------------")

    # RUN last algo (Tal's algo)

    # Output Last algo result

    print("---------------------------------------------")


if __name__ == "__main__":
    main()
