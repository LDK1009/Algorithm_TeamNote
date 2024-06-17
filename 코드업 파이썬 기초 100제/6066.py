inputs = list(map(int,input().split()))
for i in range(len(inputs)):
    if(inputs[i]%2==0):
        print("even")
    elif(inputs[i]%2==1):
        print("odd")
