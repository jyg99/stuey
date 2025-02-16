import sys
sys.stdin = open("boom.txt", "r")
def boom(y,x):

    Sum = matrix[y][x]
    for i in range(4):
        for j in range(1,N):
            dy = y+diry[i]*j
            dx = x+dirx[i]*j

            if dy >= N or dx >= N or dy < 0 or dx < 0:
                continue
            Sum += matrix[dy][dx]
    return Sum

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int,input().split()))for _ in range(N)]

    diry = [-1,1,0,0]
    dirx = [0,0,1,-1]

    Max = -21e8
    Min = 21e8

    for i in range(N):
        for j in range(N):
            result = boom(i,j)
            if result > Max:
                Max = result
            if result < Min:
                Min = result
    print(f'#{tc} {Max - Min}')