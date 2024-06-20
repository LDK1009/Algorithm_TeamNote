boardSize = 19
board = []
n = 0

# 바둑판 행 뒤집기
def changeRow(arr, index):
    for i in range(len(arr[index])):
        if arr[index][i] == 0:
            arr[index][i] = 1
        elif arr[index][i] == 1:
            arr[index][i] = 0

# 바둑판 열 뒤집기
def changeCol(arr, index):
    for i in range(boardSize):
        if arr[i][index] == 0:
            arr[i][index] = 1
        elif arr[i][index] == 1:
            arr[i][index] = 0

# 바둑판의 바둑알 배치 현황 입력 받기
def setBoard():
    for i in range(boardSize):
        board.append(list(map(int, input().split())))

# 뒤집기 횟수 입력 받기
def setFlipCount():
    global n
    n = int(input())

# 해당 좌표 행, 열 뒤집기
def flipCoordinate(board, x, y):
    changeRow(board, x-1)
    changeCol(board, y-1)

# 바둑판 출력
def printBoard(board):
    for row in board:
        for elem in row:
            print(elem, end=' ')
        print()

# 실행 함수
def main():
    setBoard()  # 바둑판의 바둑알 배치 현황 입력 받기
    setFlipCount()  # 뒤집기 횟수 입력 받기
    for _ in range(n):
        x, y = map(int, input().split())
        flipCoordinate(board, x, y)
    printBoard(board)

main()


# 2차원 배열에 대한 정확한 이해에 도움을 준다.