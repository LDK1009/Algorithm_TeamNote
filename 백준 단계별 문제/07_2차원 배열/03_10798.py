matrix = []  # 행렬
len_col = 0  # 행렬의 열 길이
result = ''  # 최종 문자열

# 입력 (5행 y열)
for i in range(5):
    row = list(input())
    matrix.append(row)

# 행렬의 최대 열 길이 찾기
for element in matrix:
    if (len(element) > len_col):
        len_col = len(element)


# 열을 순회한다.
for i in range(len_col):
    str_col = ''  # 세로 문자열
    for j in range(len(matrix)):
        if (i > len(matrix[j]) - 1):  # 현재 순회중인 열의 크기가 해당 행의 최대 인덱스보다 크다면
            continue
        str_col += matrix[j][i]  # 문자 붙이기
    result += str_col

print(result)
