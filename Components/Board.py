import itertools


class Board:
    def __init__(self, length, values):
        self._length = length
        self._values = [[values[i * self._length + j]
                         for j in range(self._length)] for i in range(self._length)]

    def __str__(self):
        s = ""
        for i in range(self._length):
            for j in range(self._length):
                s += str(self._values[i][j]) + "\t"
            s += "\n"
        return s

    def find_zero_index(self):
        empty_item_pos = self.get_board_state().index(0)
        row = empty_item_pos // self.length()
        col = empty_item_pos % len(self[row])
        return row, col

    def get_board_state(self):
        return list(itertools.chain(*self._values))

    def get_goal_state(self):
        sorted_list = sorted(self.get_board_state())
        first_item = sorted_list.pop(0)
        sorted_list.append(first_item)

        return sorted_list

    def length(self):
        return self._length

    def width(self):
        return self._length

    def size(self):
        return self._length ** 2

    def __getitem__(self, row_index):
        return self._values[row_index]

    def have_item_left(self, col):
        return col != 0

    def have_item_right(self, col):
        return col != self._length - 1

    def have_item_up(self, row):
        return row != 0

    def have_item_down(self, row):
        return row != self._length - 1

    def can_move_left(self, row, col):
        return self._values[row][col - 1] == 0 if self.have_item_left(col) and col < self.length() else False

    def can_move_right(self, row, col):
        return self._values[row][col + 1] == 0 if self.have_item_right(col) and col >= 0 else False

    def can_move_up(self, row, col):
        return self._values[row - 1][col] == 0 if self.have_item_up(row) and row < self.length() else False

    def can_move_down(self, row, col):
        return self._values[row + 1][col] == 0 if self.have_item_down(row) and row >= 0 else False

    def move_left(self, row, col):
        self._values[row][col], self._values[row][col - 1] = self._values[row][col - 1], self._values[row][col]

    def move_right(self, row, col):
        self._values[row][col], self._values[row][col + 1] = self._values[row][col + 1], self._values[row][col]

    def move_up(self, row, col):
        self._values[row][col], self._values[row - 1][col] = self._values[row - 1][col], self._values[row][col]

    def move_down(self, row, col):
        self._values[row][col], self._values[row + 1][col] = self._values[row + 1][col], self._values[row][col]
