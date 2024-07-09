s = input()
c = [chr(i) for i in range(ord('a'), ord('z') + 1)]  # a ~ z 배열
result = [-1] * 26

for i, char1 in enumerate(c):  # a부터 z까지 순회
    for j, char2 in enumerate(s): 
        if char1 == char2:  # 만약 알파벳이 문자열에 존재한다면
            result[i] = j  # 해당 알파벳의 위치 저장
            break  # 처음 등장한 인덱스만 필요하므로 루프 탈출

for i in result:
    print(i, end=' ')

            
'''
1. 문자열을 순회하며 각 문자의 알파벳 위치(0~25)를 구한다.
2. 문자열 내 문자의 인덱스를 구한다.
3. result 리스트에서 알파벳 위치 인덱스의 값에 문자의 인덱스를 대입한다.
4. 처음 등장한 문자의 인덱스만 찾아야하므로 알파벳 리스트에서 해당 알파벳을 다른 수로 변경한다.

ex) 문자열이 change이고 찾는 문자가 'c'일 때
문자열 내 문자의 인덱스는 0이다.
알파벳 순서는 2이다.
result 리스트의 인덱스 2의 값을 0으로 바꾼다
'''