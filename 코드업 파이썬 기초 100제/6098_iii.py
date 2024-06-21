board = []
boardSize = 10
currentX = 1  # 개미의 현재 위치
currentY = 1  # 개미는 (1, 1) 좌표에서 먹이 찾기 활동을 시작한다.
lastX = boardSize - 2 # 미로 상자 마지막 X 인덱스(-2를 하는 이유는 -1은 테두리 벽의 위치이기 때문이다.)
lastY = boardSize - 2 # 미로 상자 마지막 Y 인덱스

# 미로 상자 생성 함수


def makeBoard():
    global board, boardSize
    for _ in range(boardSize):
        row = list(map(int, input().split()))
        board.append(row)

# 현재 좌표 마킹 함수
def markCurrentCoordinates():
    global board,currentX, currentY
    board[currentX][currentY] = 9

# 이동 및 각종 탐지
def checkWallAndMove():
    global board, currentX, currentY, lastX, lastY
    while True:
        if(board[currentX][currentY]==2): # 현재 위치에 먹이가 있다면 마킹 후 이동 중지
            markCurrentCoordinates()
            break
        elif(currentX==lastX and currentY == lastY): # 현재 위치가 미로 상자의 마지막 위치라면
            markCurrentCoordinates()
            break
        elif(board[currentX][currentY+1]==1): # 현재 좌표의 오른쪽(x+1) 위치가 벽이라면 아래로 이동
            markCurrentCoordinates()
            currentX += 1 # 아래로 이동
        else: # 우측에 벽도 없고 먹이도 찾지 못했다면 마킹 후 우측으로 이동
            markCurrentCoordinates()
            currentY += 1 # 아래로 이동

# 미로 상자 출력
def printBoard():
    global board
    for row in board:
        for item in row:
            print(item, end=' ')
        print()             


# 프로그램 실행
makeBoard()
checkWallAndMove()
printBoard()

