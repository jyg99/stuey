import sys
sys.stdin = open("coin.txt", "r")
T = int(input())
for tc in range(1, 1+T):
    N,M = map(int,input().split())
    first = list(map(int,input().split()))
    for _ in range(M):
        i,j = map(int,input().split())
        i = i-1
        for num in range(1,j+1):
            right = i+num
            left = i-num
            if right >= len(first) or left < 0:
                break
            if first[right] == first[left]:
                first[right] = 1-first[right]
                first[left] = 1-first[left]
            elif first[right] != first[left]:
                continue
    print(f'#{tc}',*first)