#creating and displaying an undirected graph
class graph:
    def __init__(self):
        self.graph={}
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    def add_edge(self,vertex1,vertex2):
        if vertex1 and vertex2 in graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
    def display_graph(self,vertex):
