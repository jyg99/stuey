import sys
sys.stdin = open("boom2.txt", "r")
def boom(y,x):
    summ = matrix[y][x]
    for i in range(4):
        for j in range(1,matrix[y][x]+1):
            dy = y+diry[i]*j
            dx = x+dirx[i]*j
            if dy<0 or dx<0 or dy>=N or dx>=M:
                continue
            summ += matrix[dy][dx]
    return summ
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split()))for _ in range(N)]
    maxx = -21e8
    diry = [-1,1,0,0]
    dirx = [0,0,1,-1]
    for i in range(N):
        for j in range(M):
            result = boom(i,j)
            if result > maxx:
                maxx = result
    print(f'#{tc} {maxx}')