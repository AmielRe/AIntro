class Node:
    """Contains the information of the node and another nodes of the Decision Tree."""

    def __init__(self):
        self.value = None
        self.nextFeature = None
        self.childs = None
