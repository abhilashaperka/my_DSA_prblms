#adjacency list representation of a graph

class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None

class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = None
        else:
            print(f"Vertex {vertex} already exists.")
            
    def add_edge(self, src, dest):
        if src in self.graph and dest in self.graph:
            new_node = Node(dest)
            new_node.next = self.graph[src]
            self.graph[src] = new_node
        else:
            print("One or both vertices do not exist.")
            
    def display(self):
        for vertex in self.graph:
            print(f"Vertex {vertex}:", end="")
            temp = self.graph[vertex]
            while temp:
                print(f"{temp.vertex} -> ", end="")
                temp = temp.next
            print("None")
            
    def remove_edge(self, src, dest):
        if src in self.graph:
            current = self.graph[src]
            prev = None
            while current:
                if current.vertex == dest:
                    if prev:
                        prev.next = current.next
                    else:
                        self.graph[src] = current.next
                    break
                prev = current
                current = current.next
        
        if dest in self.graph:
            current = self.graph[dest]
            prev = None
            while current:
                if current.vertex == src:
                    if prev:
                        prev.next = current.next
                    else:
                        self.graph[dest] = current.next
                    break
                prev = current
                current = current.next
    def remove_vertex(self,vertex):
        if vertex in self.graph:
            for v in self.graph:
                self.remove_edge(v,vertex)
            del self.graph[vertex]
        else:
            print(f"vertex{vertex} doesn't exist.")

# Example usage
graph = Graph()
for i in range(1, 6):
    graph.add_vertex(i)
    
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 1)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(4, 2)
graph.add_edge(4, 1)
graph.add_edge(4, 5)
graph.add_edge(5, 4)

print("Graph:")
graph.display()

print("Removing edge between 4 and 5")
graph.remove_edge(4, 5)
graph.display()

print("after removing vertex 5:")
graph.remove_vertex(5)
graph.display()
