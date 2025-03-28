# def solution(sequence, k):
#     for i in range(len(sequence)):
#         for j in range(len(sequence)):
#             if (sum(sequence[i : i + j]) == k):
#                 print(sequence[i:i+j])

# def solution(sequence, k):
#     for i in range(len(sequence)): # 0 ~ 5 정도 길이 !
#         for j in range(1, len(sequence) -i +1): # 1부터 5-(0+1) , 2부터 5-(0-(1+1)) ,
#             if sum(sequence[i : i + j]) == k:
#                 print(sequence[i : i + j])

# def solution(sequence, k):
#     result = None  # 아직 답을 못 찾음

#     for i in range(len(sequence)):
#         for j in range(1, len(sequence) - i + 1):
#             if sum(sequence[i : i + j]) == k:
#                 if result is None or j < (result[1] - result[0] + 1):
#                     result = [i, i + j - 1]
    
#     return result

def solution(sequence, k):
    start = 0
    end = 0
    total = sequence[0]

    result = [0, len(sequence)-1]  
    while end < len(sequence):
        if total == k:
            if (end - start) < (result[1] - result[0]):
                result = [start, end]

            total -= sequence[start]
            start += 1

        elif total < k:
            end += 1
            if end < len(sequence):
                total += sequence[end]

        else:
            total -= sequence[start]
            start += 1

    return result

