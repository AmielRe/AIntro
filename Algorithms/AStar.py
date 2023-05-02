from enum import Enum
from heapq import heappush, heappop
from Components.Board import Board
from Util.utils import MoveTypes, manhattan_distance

class MovePriority(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class HeapItem:
    def __init__(self,
                 priority: int,
                 board: Board,
                 moves: list[MoveTypes]):
        self.priority: int = priority
        self.board: Board = board
        self.moves: list[MoveTypes] = moves

    def __lt__(self, other: "HeapItem"):
        if self.priority == other.priority and self.moves == other.moves:
            my_move_value = 0
            other_move_value = 0

            for move_priority_name in MovePriority.__members__:
                if self.moves[-1].name == move_priority_name:
                    my_move_value = MovePriority[move_priority_name]
                if other.moves[-1].name == move_priority_name:
                    other_move_value = MovePriority[move_priority_name]

                if my_move_value != 0 and other_move_value != 0:
                    break

            return my_move_value < other_move_value

        return self.priority < other.priority

def get_new_boards(board: Board):
    possible_moves = []
    empty_row, empty_col = board.find_zero_index()

    if board.can_move_up(empty_row + 1, empty_col):  # move empty item up
        new_board = Board(board.length(), board.get_board_state())
        new_board.move_up(empty_row + 1, empty_col)
        possible_moves.append((new_board, MoveTypes.UP))

    if board.can_move_down(empty_row - 1, empty_col):  # move empty item down
        new_board = Board(board.length(), board.get_board_state())
        new_board.move_down(empty_row - 1, empty_col)
        possible_moves.append((new_board, MoveTypes.DOWN))

    if board.can_move_left(empty_row, empty_col + 1):  # move empty item left
        new_board = Board(board.length(), board.get_board_state())
        new_board.move_left(empty_row, empty_col + 1)
        possible_moves.append((new_board, MoveTypes.LEFT))

    if board.can_move_right(empty_row, empty_col - 1):  # move empty item right
        new_board = Board(board.length(), board.get_board_state())
        new_board.move_right(empty_row, empty_col - 1)
        possible_moves.append((new_board, MoveTypes.RIGHT))

    return possible_moves

def AStar(board_start: Board):
    goal: list[int] = board_start.get_goal_state()
    heap = [HeapItem(0, board_start, [])]
    visited = set()
    while heap:
        current_item: HeapItem = heappop(heap)
        cost: int = len(current_item.moves)
        current_board: Board = current_item.board
        priority: int = current_item.priority
        moves: list[MoveTypes] = current_item.moves
        if current_board.get_board_state() == goal:
            return moves

        visited.add((priority, tuple(map(tuple, current_board))))
        for new_board, move in get_new_boards(current_board):
            # Calculate the priory according to Manhattan_distance
            priority = cost + 1
            for i, item in enumerate(current_board.get_board_state()):
                if item:
                    goal_index = current_board.get_goal_state().index(item)
                    goal_row = (goal_index // current_board.length())
                    goal_col = (goal_index % len(current_board[goal_row - 1]))

                    current_row = (i // current_board.length())
                    current_col = (i % len(current_board[current_row - 1]))

                    priority += manhattan_distance(p1=(current_row, current_col),
                                                   p2=(goal_row, goal_col))

                # Search the new board in the open list and
                # if it in the open list check the priority to remove from the heap and update the priory
            for heap_item in heap:
                if heap_item.board.get_board_state() == new_board.get_board_state():
                    if priority < cost:
                        heap.remove(heap_item)
                    break

            # check if the new board is not in the close list
            if tuple((priority, tuple(map(tuple, new_board)))) not in visited:
                heappush(heap, HeapItem(priority, new_board, moves + [move]))
