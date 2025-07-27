def add_edge(adj,i,j):
    adj[i].append(j)
    adj[j].append(i)
def display_adj_list(adj):
    for i in range(len(adj)):
        print(f"{i}: ",end="")
        for j in adj[i]:
            print(j,end=" ")
        print()
def remove_vertex(adj,vertex_remove):
    nums_vertex=len(adj)
    if not (0 <= vertex_remove < nums_vertex):
        print(f"error:vertex{vertex_remove} is out of bound")
        return
    adj[vertex_remove].clear()  #remove the vertex
    for i in range(nums_vertex):
        if i == vertex_remove:
            continue
        adj[i][:]=[neighbor for neighbor in adj[i] if neighbor != vertex_remove]
    print(f"vertex {vertex_remove} and its incident edges removes")
def remove_edge(adj,u,v):
    if 0<=u<len(adj) and 0<=v <len(adj):
        removed_successfully=False
        if v in adj[u]: #remove v from u's adjacent list
            adj[u].remove(v)
            removed_successfully=True
        if u in adj[v]: #remove u from v's adjacent list
            adj[v].remove(u)
            removed_successfully=True
        
        else:
            print(f"edge {u} <-> {v} does not exit or vertices not found.")
    else:
        print(f"error: vertices {u} or {v} are out of bounds.")
    
v=4
adj=[[] for _ in range(v)]
add_edge(adj,0,1)
add_edge(adj,0,2)
add_edge(adj,1,2)
add_edge(adj,2,3)
print("adjacency list representation:")
display_adj_list(adj)
remove_vertex(adj,2)
display_adj_list(adj)

