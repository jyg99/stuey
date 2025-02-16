import sys
sys.stdin = open("switch.txt", "r")
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    first = list(map(int,input().split()))
    goal = list(map(int,input().split()))
    start = 0
    for i in range(N):
        if first != goal:
            start += 1
            for j in range(start, N):
                if first[j] == 0:
                    first[j] = 1 - first[j]
                elif first[j] == 1:
                    first[j] = 1 - first[j]
        if first == goal:
            break
    print(f'#{tc}',start)
