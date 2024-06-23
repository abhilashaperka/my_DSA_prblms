class graph:
    def __init__(self):
        self.graph={}
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
    def display_graph(self):
        for vertex in self.graph:
            print(vertex,"->->".join(map(str,self.graph[vertex])))
g=graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_edge(1,3)
g.add_edge(1,2)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(4,3)
g.display_graph()

