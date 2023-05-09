from enum import Enum
from heapq import heappush, heappop
from Components.Board import Board
from Util.utils import MoveTypes, MovePriority, manhattan_distance


class HeapItem:
    def __init__(self,
                 priority: int,
                 board: Board,
                 moves: list[MoveTypes]):
        self.priority: int = priority
        self.board: Board = board
        self.moves: list[MoveTypes] = moves

    def __lt__(self, other: "HeapItem"):
        if self.priority == other.priority:
            other_move_index = 0

            # Got the first different move
            my_first_different_move = None
            other_first_different_move = None
            for move in self.moves:
                if other_move_index == len(other.moves):
                    return False

                if move.name != other.moves[other_move_index]:
                    my_first_different_move = move
                    other_first_different_move = other.moves[other_move_index]
                    break
                other_move_index += 1

            my_move_value = 0
            other_move_value = 0

            # Check the order of boards that has same priority and same father according to the first different moves
            for move_priority_name in MovePriority.__members__:
                if my_first_different_move.name == move_priority_name:
                    my_move_value = MovePriority[move_priority_name].value
                if other_first_different_move.name == move_priority_name:
                    other_move_value = MovePriority[move_priority_name].value

            return my_move_value < other_move_value

        return self.priority < other.priority


def AStar(board_start: Board, layer = None):
    goal: list[int] = board_start.get_goal_state()
    heap = [HeapItem(0, board_start, [])]
    visited = set()
    while heap:
        current_item: HeapItem = heappop(heap)
        cost: int = len(current_item.moves)
        current_board: Board = current_item.board
        priority: int = current_item.priority
        moves: list[MoveTypes] = current_item.moves
        if(layer != None and layer < len(moves)):
            return None
        if current_board.get_board_state() == goal:
            return moves

        visited.add(tuple(current_board.get_board_state()))
        for new_board, move in current_board.get_new_boards():
            # Calculate the priory according to Manhattan_distance
            priority = cost + 1
            for i, item in enumerate(new_board.get_board_state()):
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
            should_add = True
            for heap_item in heap:
                if heap_item.board.get_board_state() == new_board.get_board_state():
                    should_add = priority <= heap_item.priority
                    if should_add:
                        heap.remove(heap_item)
                    break

            # check if the new board should added to the open list according to his priority or the new board is not is open list
            # and the new board is not in the close list
            if should_add and tuple(new_board.get_board_state()) not in visited:
                heappush(heap, HeapItem(priority, new_board, moves + [move]))
