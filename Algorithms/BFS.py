from collections import deque
from Components.Board import Board
from Util.utils import MoveTypes

def BFS(board: Board):
    
    start = board
    goal = board.get_goal_state()
    queue = deque()
    visited = set()

    # Add the start state to the queue
    queue.append((start, []))

    while queue:
        
        current_board, current_path = queue.popleft()

        if tuple(current_board.get_board_state()) not in visited:
            # Add current state to close list
            visited.add(tuple(current_board.get_board_state()))

            # If current state is the goal, return the path
            if current_board.get_board_state() == goal:
                return current_path

            # Get all new possible moves from the current state
            for new_board, move in current_board.get_new_boards():
                # add the move to the path
                new_path = list(current_path)
                new_path.append(move)
                # Add the new state to the queue
                queue.append((new_board, new_path))
    
    # No solution found
    return None
