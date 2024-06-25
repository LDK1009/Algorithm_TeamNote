a, b, c = map(int, input().split())
prizeMoney = 0
if( a==b==c ):
    prizeMoney = 10000 + a * 1000
elif(a==b or a==c):
    prizeMoney = 1000 + a *100
elif(b==c):
    prizeMoney = 1000 + b *100
else:
    Max = max(a, b, c)
    prizeMoney = Max * 100

print(prizeMoney)