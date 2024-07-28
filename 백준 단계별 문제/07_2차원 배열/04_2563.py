paper_row = 100
paper_col = 100
paper = [[0 for _ in range(paper_col)] for _ in range(paper_row)]
count = 0

# 10*10 색종이 그리기
def draw_paper(row, col):
    paper_end_idx = len(paper) - 1
    start_row = paper_end_idx - row
    end_row = start_row - 10

    # 범위만큼 색종이 그리기
    for i in range(start_row, end_row, -1):
        for j in range(col, col + 10, 1):
            paper[i][j] = 1


# 도화지 내 1의 개수 세기
def count_draw_pixel():
    global count
    for row in paper:
        count += row.count(1)


# 입력받기
n = int(input())
for i in range(n):
    row_start, col_start = map(int, input().split())
    draw_paper(row_start, col_start)


count_draw_pixel()
print(count)