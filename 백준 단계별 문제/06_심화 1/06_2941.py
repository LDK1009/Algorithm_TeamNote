arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
answer = 0

# 문자열 내에 해당 크로아티아 문자가 없을 때까지 계속 찾고 삭제한다.
for e in arr:
  while s.find(e) > -1: # 해당 크로아티아 문자가 문자열 내에 있는가?
    find_idx = s.find(e) # 해당 문자의 인덱스 반환
    s = s[:find_idx] +' '+ s[find_idx + len(e):] # 문자열 내 해당 크로아티아 문자 제거(제거를 완료한 문자열끼리 또다른 크로아티아 문자가 될 수 있기 때문에 사이에 공백을 추가한다.)
    answer += 1

answer += len(s.replace(' ', '')) # 남은 문자열 즉, 크로아티아 아닌 일반 알파벳의 개수를 센다.(이전에 추가한 공백 제거)

print(answer)
