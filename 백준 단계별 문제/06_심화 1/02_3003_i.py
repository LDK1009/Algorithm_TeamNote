nums = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]
needs = [a - b for a, b in zip(chess, nums)]

for i in needs:
    print(i, end=" ")
    
# zip 함수를 통해 두 배열을 병렬로 연결할 수 있다.
# 이후 리스트 컴프리헨션을 사용해 새로운 배열을 생성한다.