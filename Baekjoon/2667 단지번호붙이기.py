from collections import deque

n = int(input())
graph = []
# 각 단지에 속하는 집의 수를 저장하는 리스트 
count = []

for _ in range(n):
    graph.append(list(map(int, input())))

# bfs 사용
def bfs(x, y):
    # 집의 갯수
    cnt = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))
	
    # 방문한 노드 처리
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        # 큐에 들어있는 노드는 집의 갯수와 같다
        cnt += 1
		
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
                                 
    return cnt

total = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count.append(bfs(i, j))
            total += 1

print(total)
print(*sorted(count), sep="\n")
