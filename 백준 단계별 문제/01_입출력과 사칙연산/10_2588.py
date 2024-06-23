n1 = int(input())
n2 = int(input())
Hundred = n2//100
ten = (n2%100)//10
one = n2%10

print(n1*one)
print(n1*ten)
print(n1*Hundred)
print(n1*n2)