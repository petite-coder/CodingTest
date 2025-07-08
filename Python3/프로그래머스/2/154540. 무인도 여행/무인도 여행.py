from collections import deque

def solution(maps):
    answer = []

    row, col = len(maps), len(maps[0])
    visited = [[False] * col for _ in range(row)]
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    grid = [list(row) for row in maps]
    
    def bfs(i, j):
        q = deque()
        q.append((i,j))
        visited[i][j] = True
        total = int(grid[i][j])
        
        while q:
            x, y = q.popleft()  # 현재 위치
            for dx, dy in directions:
                # 이웃 탐색
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < row and 0 <= ny < col:
                    if not visited[nx][ny] and grid[nx][ny] != "X": 
                        # 새로운 이웃 값 더하기
                        visited[nx][ny] = True
                        total += int(grid[nx][ny])
                        q.append((nx, ny))
        return total
    
    for i in range(row):
        for j in range(col):
            if not visited[i][j] and grid[i][j] != "X":
                answer.append(bfs(i,j))
        
    return sorted(answer) if answer else [-1]


'''
BFS (Breadth-First Search, 너비 우선 탐색)
- 현재 위치의 이웃부터 먼저 모두 탐색, 그 다음 이웃의 이웃으로 확장
- queue 기반
- 최단 경로 탐색

1. 시작점 큐에 넣음: q.append(start)
2. while q:
3.     현재 위치 꺼냄: q.popleft()
4.     이웃들 중 방문 안 한 거 q.append()
5.     반복
'''