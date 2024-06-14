# 입력 형식 - "2024.06.14"
year, month, day = input().split('.') 
print(day, month, year, sep='-')

# 코드해석 - year, month, day = input().split('.')
# 입력받은 문자열("2024.06.14")을 문자열('.')을 기준으로 분리하여 리스트(["2024", "06", "14"])로 변경 후
# 리스트 각 요소를 순서대로 year, month, day에 대입합니다.

# 코드해석 - print(day, month, year, sep='-')
# 저장한 변수들을 일 월 년도 순으로 출력합니다.
# 이 때 sep='-'을 통해 출력될 값 사이에 '-'을 삽입합니다.
