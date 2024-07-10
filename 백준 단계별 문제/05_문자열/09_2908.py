a, b = map(list, input().split())

a.reverse()
b.reverse()

# 리스트 > 문자열 > 숫자형으로 변환
a = int(''.join(map(str, a)))
b = int(''.join(map(str, b)))

c = max(a,b)

print(c)