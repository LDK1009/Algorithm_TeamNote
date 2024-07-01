attendance = [0] * 30

for i in range(28):
    num = int(input())
    attendance[num - 1] = 1

# 값이 0인 인덱스 모두 찾기
zeroValueIndexes = [index for index, value in enumerate(attendance) if value == 0]
Min = min(zeroValueIndexes)
print(Min+1)
print(zeroValueIndexes[1]+1)