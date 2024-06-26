n = int(input()) # 입력할 정수의 개수
numList = list(map(int, input().split())) # 정수가 공백으로 구분되어 n개만큼 입력된다.
findNum = int(input()) # 찾으려는 정수가 입력됨
count = 0

for i in numList:
    if(i==findNum): # 찾으려는 정수와 현재 인덱스의 값이 같다면
        count += 1 # 카운트 1 증가
    else:
        pass
    
print(count)