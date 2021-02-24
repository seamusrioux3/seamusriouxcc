class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight=None):
        self.neighbors[neighbor] = weight

    def __str__(self):
        return '{} neighbors: {}'.format(
            self.key,
            [x.key for x in self.neighbors]
        )

    def get_connections(self):
        return self.neighbors.keys()

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex.key] = vertex

    def get_vertex(self, key):
        if key in self.vertices[key]:
            return self.vertices[key]
        else:
            return None

    def __contains__(self, key):
        """
        Overload the in operator to support:
          >>> g = Graph()
          >>> g.add_vertex(Vertex(42))
          >>> 42 in g
          True
        """
        return key in self.vertices

    def add_edge(self, from_key, to_key, weight=None):
        if from_key not in self.vertices:
            self.add_vertex(Vertex(from_key))
        if to_key not in self.vertices:
            self.add_vertex(Vertex(to_key))
        self.vertices[from_key].add_neighbor(
            self.vertices[to_key],
            weight
        )

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())