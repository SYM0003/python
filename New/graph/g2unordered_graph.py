from numpy import zeros
import test
def mat_graph(n,m):
    # using matrix
    graph=zeros((n+1,n+1),int)
    for i in range(m):
        u=int(input())
        v=int(input())
        graph[u][v]=1
        graph[v][u]=1
    return graph
def list_graph(n,m):
    # using list
    graph=test.zeros(n+1)
    for i in range(m):
        u=int(input())
        v=int(input())
        graph[v].append(u)
        graph[u].append(v)
    return graph
if __name__=='__main__':
    n=int(input('Enter the number of nodes'))
    m=int(input('Enter the number of edges'))

    graph=mat_graph(m)
    graph2=list_graph(m)
    print(graph)
    print(graph2)


