n,m = map(int, input().split())
basket = []

for i in range(1,n+1):
    basket.append(i)

# print(basket)

for _ in range(m):
    a,b = map(int,input().split())
    temp = basket[a-1]
    basket[a-1] = basket[b-1]
    basket[b-1] = temp
    
for i in basket:
    print(i, end=' ')