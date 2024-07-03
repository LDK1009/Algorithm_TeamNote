n = int(input()) # 시험 본 과목의 개수
score = list(map(int, input().split()))

max_score = max(score)
score = [item * 100 / max_score for item in score]

new_avg = sum(score) / len(score)
print(new_avg)