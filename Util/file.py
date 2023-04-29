import math
from Util.utils import MoveTypes, SearchAlgorithms, getAlgorithmFromInt


class File:
    @staticmethod
    def read_input(filename: str):
        with open(filename, 'r') as f:
            algorithm_type = int(f.readline().strip())
            length = int(f.readline().strip())
            board_values = f.readline()
            board_values = [int(x) for x in board_values.strip().split('-')]
        return algorithm_type, length, board_values

    @staticmethod
    def write_output(moves: list[MoveTypes], algorithm: SearchAlgorithms):
        with open(r'Files/output.txt', 'w') as f:
            f.write(f'-------------------- {algorithm} --------------------')
            for move in moves:
                f.write(move.value)
            f.write('---------------------------------------------')

    @staticmethod
    def isValidInput(algorithm_type: int,
                     length: int,
                     board_values: list[int]):
        matching_algorithm = None

        matching_algorithm = getAlgorithmFromInt(algorithm_type)

        return not ((matching_algorithm is None) or
                    (length <= 0) or
                    (math.sqrt(len(board_values)) != length))
