h = 0
w = 0
n = 0
sticks = []

def init():
    global h, w, n, board, sticks
    h, w = map(int, input().split())  # 격자판 세로(h), 가로(w) 입력 받기
    board = [[0] * w for _ in range(h)]  # 격자판 만들기
    n = int(input())  # 놓을 수 있는 막대의 개수 입력 받기
    sticks = []
    
    # 각 막대의 길이(l), 방향(d), 좌표(x,y) 입력 받기(막대 개수만큼 입력 받기)
    for _ in range(n):
        l, d, x, y = map(int, input().split())
        sticks.append({'l': l, 'd': d, 'x': x, 'y': y})

def putOnStick(stick):
    l = stick['l']
    d = stick['d']
    x = stick['x'] - 1  # 인덱스는 0부터 시작하므로 1을 빼줌
    y = stick['y'] - 1  # 인덱스는 0부터 시작하므로 1을 빼줌
    
    if d == 0:  # 가로 방향
        for i in range(l):
            board[x][y + i] = 1
    elif d == 1:  # 세로 방향
        for i in range(l):
            board[x + i][y] = 1

def main():
    init()
    for stick in sticks:
        putOnStick(stick)
    
    # 2차원 배열 출력
    for row in board:
        print(' '.join(map(str, row)))
    
main()



# 글로벌 변수 사용방법에 대해 익힌다.
# 딕셔너리 사용법에 대해 이해한다.
# enumerate를 사용하여 인덱스와 아이템을 추출   

