c = ord(input())
startCharacter = ord('a')
while True:
    if(startCharacter>c):
        break
    print(chr(startCharacter), end=' ')
    startCharacter += 1

# 입력받은 문자열을 유니코드로 변환하는 방법,
# 유니코드 값끼리 비교,
# 유니코드를 문자로 변환 후 출력 방법,
# 줄바꿈 없이 출력값 사이에 공백(' ')을 삽입해 출력하는 방법
# 등에 대해 살펴볼 수 있다.