matrix = []  # 행렬
Max = 0  # 행렬의 최대값
find_row = 0  # 최대값 행 위치
find_col = 0  # 최대값 열 위치

# 행렬 입력받기
for _ in range(9):
    row = list(map(int, input().split()))
    matrix.append(row)

# 행을 순회하며 최대값 찾기
for i in range(len(matrix)):
    row_max = max(matrix[i])  # 행렬의 i번째 행의 요소중 최대값
    if (row_max >= Max):  # 현재 행의 최대값이 기존 최대값보다 크다면
        Max = row_max  # 최대값 갱신
        find_row = i + 1  # 최대값의 행 위치 갱신
        find_col = matrix[i].index(row_max) + 1  # 최대값의 열 위치 갱신

# 출력
print(Max)
print(find_row, find_col)
