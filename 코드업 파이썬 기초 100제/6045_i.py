a, b, c = map(int, input().split())

total=sum([a,b,c])
average = total / len([a,b,c])

print("{:} {:.2f}".format(total, average))

# sum 함수에는 배열을 전달한다.
# 만약 처음 입력받을 때부터 배열로 받고 싶다면 아래 코드처럼 작성한다.
# list(map(int, input().split())) 해당 코드와 위 코드의 차이점은
# map은 이터러블 객체를 반환하지만 리스트가 아니기 때문에 len함수와 같은 곳에 인수로 전달할 수 없습니다.
# 하지만 sum 함수에는 이터러블 객체를 인수로 전달할 수 있습니다.