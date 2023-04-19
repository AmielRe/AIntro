class Node:
    def __init__(self, data=None):
        self.data = [] if data is None else data
        self.up = None
        self.down = None
        self.right = None
        self.left = None
