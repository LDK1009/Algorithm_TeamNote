n = int(input())
quarter = n//3
if(quarter==1):
    print("spring")
elif(quarter==2):
    print("summer")
elif(quarter==3):
    print("fall")
elif(quarter==4 or quarter==0):
    print("winter")

# quarter 변수에 입력받은 정수를 3으로 나눈 몫을 대입한다.
# n = 1,2 라면 quarter =1 이고 n=3,4,5 이라면 quater = 2 ... n=12 이면 quater=0이다.
# 겨울은 12, 1, 2월이라 quarter=0,1 에 속하기 때문에 or을 사용하여 quarter가 0또는 1일때 winter를 출력하도록 한다.