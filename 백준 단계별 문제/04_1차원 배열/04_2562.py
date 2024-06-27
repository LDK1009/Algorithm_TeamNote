nums = []

for _ in range(9):
    next_data = int(input())
    nums.append(next_data)
    

print(max(nums))
print(nums.index(max(nums))+1)