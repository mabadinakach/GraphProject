class Vertex:
    def __ini__(self, id=None, data=None):
        self.id = id
        self.data = data
        self.neighbors = {} #dictionary of vertices I'm connected to.

    def add_neighbor(self, vertex):
        self.neighbors[vertex.id] = vertex

    