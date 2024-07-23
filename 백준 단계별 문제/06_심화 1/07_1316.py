n = int(input())
group_word_count = 0


def group_word_checker(s):  # >> aabbbcca
    uniq_s = set(s)  # 문자열 중복 제거 >> {'b', 'a', 'c'}

    for element in uniq_s:  # 고유 문자들을 순회한다
        start_idx = s.find(element)  # 문자열 내 문자의 시작 인덱스
        end_idx = s.rfind(element)  # 문자열 내 문자의 종료 인덱스
        group_s = s[start_idx:end_idx+1]  # 고유 문자 그룹
        uniq_num = len(set(group_s))  # 그룹 문자열 내 고유 문자의 개수

        # 그룹 문자열 내 고유 문자의 개수를 통해 그룹 판어 판별
        if (uniq_num >= 2):
            return False
        else:
            continue
    return True


for i in range(n):
    s = input()
    is_group_word = group_word_checker(s)  # >> True || False

    if (is_group_word == True):
        group_word_count += 1
    else:
        pass

print(group_word_count)
