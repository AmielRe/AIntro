from Components.Board import Board
from Components.Graph import Graph
from Util.file import File, MoveTypes
from Algorithems.AStar import a_star
def main():
    algorithm, length, board_values = File.read_input(r'Files/input.txt')

    # Check graph is created and format is valid
    if not File.isValidInput(algorithm, length, board_values):
        print("Invalid input, please check format!")
        return

    board = Board(length, board_values)
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
