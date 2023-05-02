from Components.Board import Board
from Components.Graph import Graph
from Util.file import File, MoveTypes, SearchAlgorithms, getAlgorithmFromInt
from Algorithms.AStar import a_star


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
    if algorithm == SearchAlgorithms.BFS:
        pass
        # RUN BFS

    elif algorithm == SearchAlgorithms.DFS:
        pass
        # RUN DFS

    elif algorithm == SearchAlgorithms.A_STAR:
        moves = a_star(board)

    elif algorithm == SearchAlgorithms.IDS:
        pass
        # RUN IDS

    elif algorithm == SearchAlgorithms.IDA_STAR:
        print("IDA* algorithm isn't supported currently, please try a different algorithm!")

    print(board)
    for move in moves:
        empty_item_pos = board.get_board_state().index(0)
        empty_row = empty_item_pos // board.length()
        empty_col = empty_item_pos % len(board[empty_row])

        if move == MoveTypes.LEFT:
            board.move_left(empty_row, empty_col + 1)
        elif move == MoveTypes.RIGHT:
            board.move_right(empty_row, empty_col - 1)
        elif move == MoveTypes.DOWN:
            board.move_down(empty_row - 1, empty_col)
        else:
            board.move_up(empty_row + 1, empty_col)
        print(board)

    File.write_output(moves=moves, algorithm=algorithm)


if __name__ == "__main__":
    main()
