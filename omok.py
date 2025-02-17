import sys
sys.stdin = open("omok.txt", "r")

def omok(y,x):
    diry = [1,1,0,-1]
    dirx = [0,1,1,1]

    for i in range(4):
        cnt = 0
        for j in range(5):
            dy = y+diry[i]*j
            dx = x+dirx[i]*j
            if dy < 0 or dx < 0 or dy >= N or dx >= N:
                continue
            if matrix[dy][dx]== 'o':
                cnt += 1
        if cnt == 5:
            return 1
T = int(input())
for tc in range(1,1+T):
    N = int(input())
    matrix = [input()for _ in range(N)]
    ans = 'NO'
    for i in range(N):
        for j in range(N):
            mok = omok(i,j)
            if mok == 1:
                ans = 'YES'
                break
        if ans =='yes':
            break

    print(ans)