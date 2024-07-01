remainList = []

for i in range(10):
    num = int(input())
    remainList.append(num % 42)    

# 고유 값의 종류 개수 구하기(집합은 중복을 허용하지 않는다.)
unique_values_count = len(set(remainList))
        

print(unique_values_count)