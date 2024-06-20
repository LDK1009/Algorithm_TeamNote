n = int(input()) # 번호를 부른 횟수
k = list(map(int, input().split()))

# k를 역순으로 순회
for i in range(len(k)-1, -1, -1):
    print(k[i], end = ' ')
