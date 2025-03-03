import sys
sys.stdin = open("switchb.txt", "r")
N = int(input())
start =list(map(int,input().split()))
stnum = int(input())
for _ in range(stnum):
    sex,num1 = map(int,input().split())
    gum = num1-1
    if sex == 1:
        for i in range(N):
            if (i+1) % num1 == 0:
                start[i] = 1-start[i]
    elif sex == 2:
    # 여학생: 중심 스위치와 좌우 대칭 구간 처리 (0-based로 변환)
        center = num1 - 1
        start[center] = 1 - start[center]  # 중심 스위치 반전
        offset = 1
        while center - offset >= 0 and center + offset < N and start[center - offset] == start[center + offset]:
            start[center - offset] = 1 - start[center - offset]
            start[center + offset] = 1 - start[center + offset]
            offset += 1

# 결과 출력 (문제 조건에 맞게 한 줄에 20개씩 출력 가능)
for i in range(N):
    print(start[i], end=' ')
    if (i + 1) % 20 == 0:
        print()