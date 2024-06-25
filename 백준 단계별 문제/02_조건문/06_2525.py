h, m = map(int, input().split())
needTime = int(input())
needH = needTime//60
needM = needTime%60
completeH = h + needH
completeM = m + needM

if(completeM >= 60):
    completeH += 1
    completeM %= 60

if(completeH>=24):
    completeH %= 24

print(completeH, completeM)