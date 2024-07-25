n, m = map(int, input().split())
matrix1 = []
matrix2 = []

# 첫번째 행렬 입력받기
for _ in range(n):
    row = list(map(int, input().split()))  # >> [1, 1, 1]
    matrix1.append(row)  # >> [ [1,1,1] ]

# 두번째 행렬 입력받기
for _ in range(n):
    row = list(map(int, input().split()))  # >> [1, 1, 1]
    matrix2.append(row)  # >> [ [1,1,1] ]

# 행 횟수만큼 반복하여 각 행렬의 n번째 행의 아이템 간 덧셈하기
for i in range(len(matrix1)):
    result1 = [a+b for a, b in zip(matrix1[i], matrix2[i])]
    for element in result1:
        print(element, end=' ')
    print()
