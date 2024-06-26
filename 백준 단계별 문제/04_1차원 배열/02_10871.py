n, x = map(int, input().split()) # n은 입력받을 정수의 개수, x는 비교할 정수
a = list(map(int, input().split())) # n개만큼 정수를 공백으로 구분해 입력 받는다.
smallerList = []

for i in a:
    if(x>i): # x보다 현재 인덱스 값이 작으면
        smallerList.append(i) # 더 작은 값들을 리스트에 따로 담는다
    else:
        pass

for i in smallerList:
    print(i, end=' ') # 작은 값들을 공백으로 구분하여 출력한다.