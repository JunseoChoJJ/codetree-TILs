n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x] += [y]

print(len(graph[1]))