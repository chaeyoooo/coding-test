# def solution(numbers):
#     result = []
#     for num in numbers:
#         for digit in str(num): #문자열은 한글자씩 접근 가능함
#             result.append(int(digit))
            
#     result.sort(reverse= True)
#     return "".join(map(str, result))

from functools import cmp_to_key
def solution(numbers):
    str_nums = list(map(str, numbers))
    sorted_nums = sorted(str_nums, key=cmp_to_key(compare))
    
    answer = ''.join(sorted_nums)
    return '0' if answer[0] == '0' else answer

def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0


