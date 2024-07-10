n = int(input())

for i in range(n):
    r, s = input().split()
    r = int(r)
    s = list(s)
    
    for j in range(len(s)):
        s[j] *= int(r)
        print(s[j], end='')
    
    print()
    
