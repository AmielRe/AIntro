from heapq import heappush, heappop
from Components.Board import Board
from Util.utils import MoveTypes, manhattan_distance

class HeapItem:
    def __init__(self,
                 priority: int,
                 board: Board,
                 moves: list[MoveTypes]):
        self.priority: int = priority
        self.board: Board = board
        self.moves: list[MoveTypes] = moves

    def __lt__(self, other):
        return self.priority < other.priority

def get_new_boards(board: Board):
    possible_moves = []
    empty_item_pos = board.get_board_state().index(0)
    empty_row = empty_item_pos // board.length()
    empty_col = empty_item_pos % len(board[empty_row])

    if empty_row + 1 < board.length() and board.can_move_up(empty_row + 1, empty_col):  # move empty item up
        new_board = Board(board.length(), board.get_board_state())
        new_board.move_up(empty_row + 1, empty_col)
        possible_moves.append((new_board, MoveTypes.UP))

    if board.can_move_down(empty_row - 1, empty_col):  # move empty item down
        new_board = Board(board.length(), board.get_board_state())
        new_board.move_down(empty_row - 1, empty_col)
        possible_moves.append((new_board, MoveTypes.DOWN))

    if empty_col + 1 < len(board[empty_row]) and board.can_move_left(empty_row, empty_col + 1):  # move empty item left
        new_board = Board(board.length(), board.get_board_state())
        new_board.move_left(empty_row, empty_col + 1)
        possible_moves.append((new_board, MoveTypes.LEFT))

    if board.can_move_right(empty_row, empty_col - 1):  # move empty item right
        new_board = Board(board.length(), board.get_board_state())
        new_board.move_right(empty_row, empty_col - 1)
        possible_moves.append((new_board, MoveTypes.RIGHT))

    return possible_moves

def a_star(board_start: Board):
    goal: list[int] = board_start.get_goal_state()
    heap = [HeapItem(0, board_start, [])]
    visited = set()
    while heap:
        current_item: HeapItem = heappop(heap)
        cost: int = len(current_item.moves)
        current_board: Board = current_item.board
        moves: list[MoveTypes] = current_item.moves
        if current_board.get_board_state() == goal:
            return moves

        visited.add((cost, tuple(map(tuple, current_board))))
        for new_board, move in get_new_boards(current_board):
            # check if the new board is not in the close list
            if tuple(map(tuple, new_board)) not in visited:

                # Calculate the priory according to Manhattan_distance
                new_cost = cost + 1
                priority = new_cost
                for i, item in enumerate(current_board.get_board_state()):
                    goal_index = current_board.get_goal_state().index(item)
                    goal_row = (goal_index // current_board.length()) + 1
                    goal_col = (goal_index % len(current_board[goal_row - 1])) + 1

                    current_row = (i % current_board.length()) + 1
                    current_col = (i % len(current_board[current_row - 1])) + 1

                    priority += manhattan_distance(p1=(current_row, current_col),
                                                   p2=(goal_col, goal_row))

                    # Search the new board in the open list and
                    # if it in the open list check the priority to remove from the heap and update the priory
                    for heap_item in heap:
                        if heap_item.board == new_board:
                            if priority < cost:
                                heap.remove(heap_item)
                            break

                    heappush(heap, HeapItem(priority, new_board, moves + [move]))
