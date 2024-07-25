#입력
# 과목명 학점 평점
# 전공 평점 = (학점 * 등급)총합 / 학점 총합

# (학점 * 등급)총합
total_unit_mult_grade = float(0)
# 학점 총합
total_unit = float(0)
# 입력값들을 담는 리스트
subject_infos = []

# 등급(A+)을 숫자(4.5)로 변환
def grade_to_num(str):
    if(str=="A+"):
        return 4.5
    elif(str=="A0"):
        return 4.0
    elif(str=="B+"):
        return 3.5
    elif(str=="B0"):
        return 3.0
    elif(str=="C+"):
        return 2.5
    elif(str=="C0"):
        return 2.0
    elif(str=="D+"):
        return 1.5
    elif(str=="D0"):
        return 1.0
    elif(str=="F"):
        return 0.0
    elif(str=="P"):
        return "P"

# 입력 : 20줄에 걸쳐 과목명, 학점, 등급이 공백으로 구분되어 주어진다.
for _ in range(20):
    next_subject_info = {}
    
    # 딕셔너리에에 입력 정보 담기(과목명, 학점, 등급)
    name, unit, grade = input().split()
    next_subject_info["name"] = name
    next_subject_info["unit"] = float(unit)
    next_subject_info["grade"] = grade_to_num(grade)
    
    # 딕셔너리를 리스트에 추가
    subject_infos.append(next_subject_info)


# subject_infos 리스트 순회
for element in subject_infos:
    # 등급이 P이면 계산에서 제외한다.
    if(element["grade"] == "P"):
        continue
    # (학점 * 등급)총합 반영
    total_unit_mult_grade += element["unit"] * element["grade"]
    # 학점 총합 반영
    total_unit += element["unit"]

# 평점 (출력 결과물)
total_grade = total_unit_mult_grade / total_unit

print(total_grade)


    
    