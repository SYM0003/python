from numpy import zeros
from g2unordered_graph import list_graph
visited=zeros(999,int)
def dfs(node,graph):
    if(visited[node] ==0):
        visited[node]=1
        print(node,end=" ")
    else:
        return
    
    for adj_node in graph[node]:
        dfs(adj_node,graph)
    

def main():
    nodes=int(input('Enter the no of nodes'))
    edges=int(input('Enter the no of edges'))
    graph=list_graph(nodes, edges)
    print('This is graph')
    print(graph)

    for node in range(1,nodes+1):
        # if the graph is disoconnected graph
        dfs(node,graph)


    
if __name__=='__main__':
    main()