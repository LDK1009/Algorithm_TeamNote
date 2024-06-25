total = int(input())
types = int(input())
sum = 0

for _ in range(types):
    a, b = map(int, input().split())
    sum += a*b
    
if(total==sum):
    print("Yes")
else:
    print("No")