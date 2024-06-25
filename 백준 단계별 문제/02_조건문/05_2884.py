h, m = map(int, input().split())
nextH = h
nextM = m
if ((m-45) < 0):
    if (nextH <= 0):
        nextH = 23
    else:
        nextH -= 1
    nextM += 15
else:
    nextM -= 45
print(nextH, nextM)
