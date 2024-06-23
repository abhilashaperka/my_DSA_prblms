from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)    #default dictionary to store the graph
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.visited=[]
    
    def BFS(self,s):
        queue=[]
        queue.append(s)
        self.visited.append(s)

        while queue:
            s=queue.pop(0)
            print(s,end=" ")
            for i in self.graph[s]:
                if i not in self.visited:
                    queue.append(i)
                    self.visited.append(i)
g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,0)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,0)
g.addEdge(2,1)
g.addEdge(2,4)
g.addEdge(3,1)
g.addEdge(3,4)
g.addEdge(4,2)
g.addEdge(4,3)
"""testcase 2:
g.addEdge(0,1)
"""
print("following is the breadth first search traversal")
g.BFS(1) #starting from vertex 1
    