alpha_to_num=["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
s = list(input())
total_time = 0

for input_char in s:
    for index, string in enumerate(alpha_to_num):
        if(input_char in string):
            total_time += index + 3

print(total_time)