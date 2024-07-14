n = int(input())
star_num = 1
space_num = n-1

for i in range(1, n*2):
    print(" " * space_num, end="")
    if(i<n):
        space_num -= 1
    else:
        space_num += 1
    print("*"*star_num)
    if(i<n):
        star_num += 2
    else:
        star_num -= 2