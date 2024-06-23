import networkx as nx
import matplotlib.pyplot as plt
adj_matrix=[
    [0,1,1,0],
    [1,0,1,0],
    [1,1,0,1],
    [0,0,1,0]
]
g=nx.Graph()
for i in range(len(adj_matrix)):
    for j in range(len(adj_matrix[i])):
        if adj_matrix[i][j]==1:
            g.add_edge(i,j)
labels={0:'A',1:'B',2:'C',3:'D'}
pos=nx.spring_layout(g)
nx.draw(g, pos, with_labels=True, labels=labels, node_size=700, node_color='lightblue', font_size=17, font_color='black')
plt.show()
