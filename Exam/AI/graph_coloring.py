class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def is_valid_color(self, v, color, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def graph_color_util(self, m, color, v):
        if v == self.V:
            return True

        for c in range(1, m+1):
            if self.is_valid_color(v, color, c):
                color[v] = c
                if self.graph_color_util(m, color, v+1):
                    return True
                color[v] = 0

    def graph_coloring(self):
        for m in range(1, self.V + 1):
            color = [0] * self.V
            if self.graph_color_util(m, color, 0):
                print(f"Solution exists with {m} colors: {' '.join(map(str, color))}")
                return True
        return False

g = Graph(4)
g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
g.graph_coloring()
