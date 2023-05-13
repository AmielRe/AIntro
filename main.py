from Components.Board import Board
from Util.file import File, MoveTypes, SearchAlgorithms, getAlgorithmFromInt
from Algorithms.AStar import AStar
from Algorithms.Ids import Ids
from Algorithms.IDA import IDA
from Algorithms.BFS import BFS


def main():
    algorithm_num, length, board_values = File.read_input(r'Files/input.txt')

    # Check graph is created and format is valid
    if not File.isValidInput(algorithm_num, length, board_values):
        print("Invalid input, please check format!")
        return

    algorithm = getAlgorithmFromInt(algorithm_num)
    board = Board(length, board_values)
    moves: list[MoveTypes] = []

    # If we got here, input is good and initial state is in 'graph'
    if algorithm == SearchAlgorithms.BFS:
        moves = BFS(board)

    elif algorithm == SearchAlgorithms.DFS:
        print("DFS algorithm isn't supported currently, please try a different algorithm!")

    elif algorithm == SearchAlgorithms.A_STAR:
        moves = AStar(board)

    elif algorithm == SearchAlgorithms.IDS:
        Ids(board, 20)

    elif algorithm == SearchAlgorithms.IDA_STAR:
        moves = IDA(board)

    print(algorithm)
    print([move.value for move in moves])
    File.write_output(moves=moves)


if __name__ == "__main__":
    main()
