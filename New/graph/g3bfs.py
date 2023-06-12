import g2unordered_graph
from numpy import zeros

class Graph:
    def __init__(self,nodes,edges):
        self.nodes=nodes
        self.edges=edges
        self.graph=g2unordered_graph.list_graph(nodes,edges)
        self.bfs_req()
    
    def bfs_req(self):
        self.visited=zeros(self.nodes+1,int)
        self.ds=[]
    def bfs(self,node):
        if self.visited[node]==0:
            self.visited[node]=1
            self.ds.append(node)
 
        while len(self.ds)>0:
            cur_node=self.ds[0]
            self.ds.pop(0)
            print(cur_node,end=" ")
            for adj in self.graph[cur_node]:
                if(self.visited[adj]==0):
                    self.visited[adj]=1
                    self.ds.append(adj)
            pass  
        print()
        for remaining_node in range(1,self.nodes+1):
            if(self.visited[remaining_node]==0):
                self.bfs(graph,remaining_node,n)


nodes=int(input('Enter the number of nodes'))
edges=int(input('Enter the number of edges'))
graph=Graph(nodes, edges)
print('this is the graph')
print(graph.graph)

graph.bfs(1)
