maximun = int(input())
total = 0
i = 0

while True:
    if(total >= maximun):
        break
    else:
        i += 1
        total += i
   
print(i)