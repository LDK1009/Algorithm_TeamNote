n = int(input()) # 출석번호를 부른 횟수
rollCalls = list(map(int, input().split())) # 무작위로 부른 번호를 리스트에 담는다.

students = 23 # 학생수
callCounts = [0] * students # 전체 학생 수만큼 번호를 부여한 출석부 생성, 현재는 누구도 호명받지 않았으므로 전부 0으로 초기화한다.

# 호명한 번호들이 담긴 리스트를 순회한다.
for i in rollCalls: # i에는 호명한 번호가 담긴다.
    callCounts[i-1] += 1 # 호명한 번호의 호명횟수를 1만큼 증가시킨다.

# 출석 번호별 호명 횟수 출력
for i in callCounts:
    print(i, end=' ')


# callCounts = [0] * students
# 위 코드를 통해 동적인 개수만큼 0으로 채워진 리스트를 간단하게 생성하는 방법을 알 수 있다