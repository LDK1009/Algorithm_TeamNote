f1 = float(input())
f2 = float(input())
f3 = f1 + f2
print(f3)


# 오답노트
"""
f1, f2 = map(float, input().split())
f3 = f1 + f2
print(f3)
"""
# 위 코드는 왜 오답처리 되었을까?
# 이유는 문제의 입력 예시를 살펴보면 알 수 있다.
# 입력 예시 - 2개의 실수가 줄을 바꿔 입력된다.
# 위와 같이 줄을 바꾸어 사용자의 입력을 받기 때문에
# 한 줄로 입력을 받는 map(float, input().split())은 오답처리 된다.