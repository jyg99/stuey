def dfs(y,x):
    global result, visit
    if maze[y][x] == '3':
        result = 1
    for dy,dx in [[1,0], [-1,0], [0,1],[0,-1]]:
        ny = dy+y
        nx = dx+x
        if 0<=ny<N and 0<= nx < N:
            if maze[ny][nx] != '1' and visit[ny][nx] == 0:
                visit[ny][nx] = 1
                dfs(ny,nx)


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    maze = [list(input())for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                dfs(i,j)

    print(f'#{tc} {result}')