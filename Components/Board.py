import itertools


class Board:
    def __init__(self, length, values):
        self.length = length
        self.values = [[values[i * self.length + j]
                        for j in range(self.length)] for i in range(self.length)]

    def __str__(self):
        s = ""
        for i in range(self.length):
            for j in range(self.length):
                s += str(self.values[i][j]) + "\t"
            s += "\n"
        return s

    def get_board_state(self):
        return list(itertools.chain(*self.values))

    def get_goal_state(self):
        sorted_list = sorted(self.get_board_state())
        first_item = sorted_list.pop(0)
        sorted_list.append(first_item)

        return sorted_list

    def length(self):
        return self.length

    def width(self):
        return self.length

    def size(self):
        return self.length**2

    def __getitem__(self, row_index):
        return self.values[row_index]

    def have_item_left(self, col):
        return col != 0

    def have_item_right(self, col):
        return col != self.length - 1

    def have_item_up(self, row):
        return row != 0

    def have_item_down(self, row):
        return row != self.length - 1

    def can_move_left(self, row, col):
        return self.values[row][col - 1] == 0 if self.have_item_left(col) else False

    def can_move_right(self, row, col):
        return self.values[row][col + 1] == 0 if self.have_item_right(col) else False

    def can_move_up(self, row, col):
        return self.values[row - 1][col] == 0 if self.have_item_up(row) else False

    def can_move_down(self, row, col):
        return self.values[row + 1][col] == 0 if self.have_item_down(row) else False

    def move_left(self, row, col):
        self.values[row][col], self.values[row][col -
                                                1] = self.values[row][col - 1], self.values[row][col]

    def move_right(self, row, col):
        self.values[row][col], self.values[row][col +
                                                1] = self.values[row][col + 1], self.values[row][col]

    def move_up(self, row, col):
        self.values[row][col], self.values[row -
                                           1][col] = self.values[row - 1][col], self.values[row][col]

    def move_down(self, row, col):
        self.values[row][col], self.values[row +
                                           1][col] = self.values[row + 1][col], self.values[row][col]
