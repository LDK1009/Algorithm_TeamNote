s = input() # 입력 받은 문자열
s = s.upper() # 대문자로 변환

s_dict = dict.fromkeys(s) # 입력 받은 문자열을 중복 제거하여 딕셔너리로 저장 
uniq_list = list(''.join(s_dict)) # 중복 제거, 순서 유지된 리스트 생성

for element in uniq_list:
    s_dict[element] = s.count(element) # s_dict 각 알파벳 value에 해당 알파벳의 출현 빈도를 대입한다.

max_value = max(s_dict.values()) # 딕셔너리 value 중 최대값 구하기
max_keys = [key for key, value in s_dict.items() if value == max_value] # 최대값을 가진 모든 키 찾기

if (len(max_keys)>1): # 최대값을 가진 키가 여러개일 경우
    print("?")
else:
    print(max_keys[0])
    
