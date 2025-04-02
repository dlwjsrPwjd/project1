#https://www.acmicpc.net/problem/7576

from collections import deque

def bfs():
    # 방향 벡터 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에 있고 익지 않은 토마토일 경우
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))

# 입력 처리
M, N = map(int, input().split())  # M: 가로 칸 수, N: 세로 칸 수
box = [list(map(int, input().split())) for _ in range(N)]

# BFS를 위한 큐 초기화
queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:  # 익은 토마토 위치를 큐에 추가
            queue.append((i, j))

# BFS 실행
bfs()

# 결과 계산
max_days = 0
for row in box:
    for value in row:
        if value == 0:  # 익지 않은 토마토가 존재하면 -1 출력
            print(-1)
            exit()
        max_days = max(max_days, value)

# 최대 일수에서 초기값(1)을 빼고 출력
print(max_days - 1)