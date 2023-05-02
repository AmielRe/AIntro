from Components.Board import Board
from Components.Graph import Graph
from Util.file import File, MoveTypes
from Algorithms.AStar import a_star
def main():
    algorithm, length, board_values = File.read_input(r'Files/input.txt')

    # Check graph is created and format is valid
    if not File.isValidInput(algorithm, length, board_values):
        print("Invalid input, please check format!")
        return

    board = Board(length, board_values)

    moves = a_star(board)
    print(moves)
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

    graph = Graph(board)

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

    moves: list[MoveTypes] = a_star(board_start=board)

    print("---------------------------------------------")

    print("-------------------- IDS --------------------")

    # RUN IDS

    # Output IDS result

    print("---------------------------------------------")

    File.write_output(moves=moves)


if __name__ == "__main__":
    main()
