def solution(numbers):
    result = [i for i in range (0, 10)] # in range 
    for k in range(len(numbers)):
        result.remove(numbers[k])
    return sum(result)