from Graph import *


def main():
    graph = inputToGraph(1, 4, [1, 2, 3, 4, 5, 6, 7, 8,
                                9, 10, 11, 12, 13, 0, 14, 15])

    # Check graph is created and format is valid
    if (graph == None):
        print("Invalid input, please check format!")
        return

    # If we got here, input is good and initial state is in 'graph'
    print("-------------------- BFS --------------------")

    # RUN BFS

    print("---------------------------------------------")

    print("-------------------- DFS --------------------")

    # RUN DFS

    print("---------------------------------------------")

    print("-------------------- A* --------------------")

    # RUN A*

    print("---------------------------------------------")

    print("-------------------- Last algo --------------------")

    # RUN last algo (Tal's algo)

    print("---------------------------------------------")


if __name__ == "__main__":
    main()
