basket = []

# 바구니 개수(n), 순서 바꾸는 횟수(m) 입력받기
n, m = map(int, input().split())

# 바구니에 번호 부여
for i in range(1, n+1):
    basket.append(i)

# 좌측에서부터 1번째 바구니는 0번 인덱스의 바구니를 의미함을 유의해야한다.
for _ in range(m):
    i, j = map(int, input().split())
    if(i>j): # i=4 j=2
        basket[i-1:j-2:-1] = basket[i-1:j-2:-1][::-1]
    else: # i=2 j=4
        basket[i-1:j:1] = basket[i-1:j:1][::-1]

for i in basket:
    print(i, end=' ')