# 정답 코드
n,m = map(int, input().split())

basket = [0]*n

for l in range(m):
  i,j,k = map(int,input().split())
  for x in range(i,j+1):
    basket[x-1] = k

for x in range(n):
  print(basket[x], end=" ")

# 내 코드
# n, m = map(int, input().split())

# basket = [0] * n
# print(basket)

# for _ in range(m):
#     i, j, k = map(int, input().split())
#     # 배열의 요소를 대체하기 위해서는 이터레이터가 대입되어야 한다.
#     # 대체할 요소 개수만큼의 k 값을 배열에 담아 대체한다
#     basket[i-1:j] = [k] * (j-i+1) 


# for i in range(n):
#     print(basket[i], end = ' ')
    
    