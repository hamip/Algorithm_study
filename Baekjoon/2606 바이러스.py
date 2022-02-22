# 컴퓨터의 갯수
com = int(input())
# 간선의 갯수
n = int(input())

graph = [[] for _ in range(com + 1)]

# 인접 리스트
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 작은 수의 노드부터 방문
for i in range(1, com + 1):
    graph[i].sort()

visited = [False] * (com + 1)
# 감염된 컴퓨터 갯수
infected_com = 0

# dfs
def dfs(start):
    global infected_com
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            infected_com += 1
            dfs(i)

# 1번 컴퓨터와 연결된 컴퓨터들만 감염
dfs(1)
print(infected_com)
