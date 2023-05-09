from Components.Board import Board
from Components.Graph import Graph
from Util.file import File, MoveTypes, SearchAlgorithms, getAlgorithmFromInt
from Algorithms.DFS import DFS
from Algorithms.Ids import Ids


def main():
    algorithm_num, length, board_values = File.read_input(r'Files/input.txt')

    # Check graph is created and format is valid
    if not File.isValidInput(algorithm_num, length, board_values):
        print("Invalid input, please check format!")
        return

    algorithm = getAlgorithmFromInt(algorithm_num)
    board = Board(length, board_values)
    graph = Graph(board)
    moves: list[MoveTypes] = []

    # If we got here, input is good and initial state is in 'graph'
    if (algorithm == SearchAlgorithms.BFS):
        pass
        # RUN BFS

    elif (algorithm == SearchAlgorithms.DFS):
        moves = DFS(board, 20)

    elif (algorithm == SearchAlgorithms.A_STAR):
        pass
        # RUN A*

    elif (algorithm == SearchAlgorithms.IDS):
        Ids(board, 20)

    elif (algorithm == SearchAlgorithms.IDA_STAR):
        print("IDA* algorithm isn't supported currently, please try a different algorithm!")

    File.write_output(moves=moves, algorithm=algorithm)


if __name__ == "__main__":
    main()
