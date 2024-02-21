from collections import deque

n, m, v = map(int , input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
queue = deque()

for i in range(m):
    node, sub = map(int, input().split())
    graph[node][sub] = graph[sub][node] = 1

# node number 1 to n
visited1 = [0] * (n+1)
visited2 = visited1.copy()

def dfs(node):
    visited1[node] = 1
    print(node, end = ' ' )
    
    # n scope global
    for i in range(1, n+1):
        # sub node search
        if graph[node][i] == 1 and visited1[i] == 0:
            dfs(i)

def bfs(node):
    queue.append(node)
    visited2[node] = 1
    
    while queue:
        node = queue.popleft()
        print(node, end = ' ')
        for i in range(1, n+1):
            if graph[node][i] == 1 and visited2[i] == 0:
                queue.append(i)
                visited2[i] = 1
                
dfs(v)
print()
bfs(v)