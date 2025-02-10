def solution(phone_number):
    answer = phone_number[:-4]
    real = ["*" for i in answer]
    result = phone_number[-4:]
    real.extend(result)
    real = ''.join(real)
    return real