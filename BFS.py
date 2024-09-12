from collections import deque
def add_edge(adj,s,t):
    adj[s].append(t)
    adj[t].append(s)

def bfs(adj,visited,s):
    visited[s]=True
    q=deque()
    q.append(s)
    
    while q:
        curr=q.popleft()
        print(curr)
        for x in adj[curr]:
            if not visited[x]:
                visited[x]=True
                q.append(x)



if __name__ == "__main__":
    V = 5
    adj = [[] for _ in range(V)]
    edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]
    for e in edges:
        add_edge(adj, e[0], e[1])
    visited=[False]*len(adj)
    source = 0
    print("BFS from source:", source)
    bfs(adj, visited, source)