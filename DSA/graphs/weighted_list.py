
def addEdge(adj, u, v, wt):
    
    adj[u].append([v, wt])
    adj[v].append([u, wt])
    return adj
def removeedge(adj,u,v,wt):
    removed_successful=False
    if 0<=len(adj) and [v,wt] in adj[u]: #to remove edge and wt in u's list
        adj[u].remove([v,wt])
        removed_successful=True
    if 0<=len(adj) and [u,wt] in adj[v]:#remove edge and wt in v's list
        adj[v].remove([u,wt])
        removed_successful=True
    if removed_successful:
        print(f"edge removed: {u}<-> {v} (weight {wt})")
    else:
        print(f"edge {u}<-> {v} (weight{wt}) does not exit")
    return adj
def remove_vertex(adj,vertex_remove):
    nums_vertex=len(adj)
    if not 0<= vertex_remove<nums_vertex:
        print(f"error:vertex {vertex_remove} is out of bounds")
        return adj
    adj[vertex_remove].clear() #clear adjlist of vertex_remove
    for i in range(nums_vertex):
        if i == vertex_remove:
            continue
        adj[i][:]=[[neighbor,wt] for neighbor,wt in adj[i] if neighbor != vertex_remove]
    print(f"vertex {vertex_remove} and its edges removed")
    return adj
                



    
# Print adjacency list representation of graph
def printGraph(adj, V):
    
    #v, w = 0, 0
    for u in range(V):
        print("Node", u, "makes an edge with")

        for it in adj[u]:
            v = it[0]
            wt = it[1]
            print("\tNode", v, "with edge weight =", wt)
            
        print()

# Driver code
if __name__ == '__main__':
    
    V = 5
    adj = [[] for i in range(V)]

    adj = addEdge(adj, 0, 1,10)
    adj = addEdge(adj, 0, 4, 20)
    adj = addEdge(adj, 1, 2, 30)
    adj = addEdge(adj, 1, 3, 40)
    adj = addEdge(adj, 1, 4, 50)
    adj = addEdge(adj, 2, 3, 60)
    adj = addEdge(adj, 3, 4, 70)

    printGraph(adj, V)
    adj=removeedge(adj,1,2,20)
    adj=remove_vertex(adj,3)
    printGraph(adj, V)

# This code is contributed by mohit kumar 29