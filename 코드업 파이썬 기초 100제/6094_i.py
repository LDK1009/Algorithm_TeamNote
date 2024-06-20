n = int(input()) # 번호를 부른 횟수
k = list(map(int, input().split()))
minimum = k[0] 
# 이 때 minimum = 0 으로 설정하면 0보다 큰 숫자들만을 호명했을 때 호명한 번호 중 가장 빠른 번호가 아닌 0을 출력하는 버그가 발생한다.

# 부른 번호중 가장 빠른 번호 찾기
for i in k:
    if(i<minimum):
        minimum = i

# 가장 작은 수 출력
print(minimum)
