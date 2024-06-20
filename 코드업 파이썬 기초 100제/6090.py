a, m, d, n = map(int, input().split())
current = a
count = 0

for i in range(n-1):
    count += 1
    current = current * m + d
    

print("{:}".format(current))
