from Components.Board import Board

class Edge:
    def __init__(self,
                 src_vertex,
                 dst_vertex):
        self.weight = 1
        self.src_vertex = src_vertex
        self.dst_vertex = dst_vertex


class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges: list[Edge] = []

    def add_edge(self, edge):
        self.edges.append(edge)


class Graph:
    def __init__(self,
                 board: Board):
        self.size = board.size()
        self.vertices: list[Vertex] = []
        self.edges = []
        self.generate_vertices(board=board)

    def generate_vertices(self,
                          board: Board):
        vertex = Vertex(value=board[0][0])
        self.vertices.append(vertex)
        self.generate_edges(board, vertex, 0, 0)

    def generate_neighbor(self,
                          board: Board,
                          vertex: Vertex,
                          row_index: int,
                          col_index: int):
        current_value = board[row_index][col_index]
        neighbor = [vertex for vertex in self.vertices if vertex.value == current_value]
        if neighbor:
            edge = Edge(vertex, neighbor[0])
            self.edges.append(edge)
            vertex.add_edge(edge)
        else:
            neighbor = Vertex(value=current_value)
            self.vertices.append(neighbor)
            edge = Edge(vertex, neighbor)
            self.edges.append(edge)
            vertex.add_edge(edge)
            self.generate_edges(board=board,
                                vertex=neighbor,
                                row_index=row_index,
                                col_index=col_index)

    def generate_edges(self,
                       board: Board,
                       vertex: Vertex,
                       row_index: int,
                       col_index: int):
        print(f"row :{row_index}, col: {col_index}")
        if board.have_item_up(row_index):
            self.generate_neighbor(board=board,
                                   vertex=vertex,
                                   row_index=row_index - 1,
                                   col_index=col_index)
        if board.have_item_down(row_index):
            self.generate_neighbor(board=board,
                                   vertex=vertex,
                                   row_index=row_index + 1,
                                   col_index=col_index)
        if board.have_item_left(col_index):
            self.generate_neighbor(board=board,
                                   vertex=vertex,
                                   row_index=row_index,
                                   col_index=col_index - 1)
        if board.have_item_right(col_index):
            self.generate_neighbor(board=board,
                                   vertex=vertex,
                                   row_index=row_index,
                                   col_index=col_index + 1)