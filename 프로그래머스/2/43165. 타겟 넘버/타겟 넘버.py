# [1, 2, 3] 이라는 숫자가 있을 때,
# 모든 숫자를 더하거나 빼서 만들 수 있는 **모든 결과**를 출력해보자.
# 예를 들면: # +1 +2 +3 = 6 , +1 +2 -3 = 0, -1 +2 +3 = 4


# def solution(numbers, target):
#     answer = 0
#     def dfs(index , current_sum):
#         nonlocal answer
#         if index == len(numbers):
#             if current_sum == target:
#                 answer +=1
#             return
#         dfs(index +1 , current_sum + numbers[index])
#         dfs(index +1 , current_sum - numbers[index])
        
#     dfs(0,0)
#     return answer

def solution(numbers, target):
    answer = 0
    def dfs(index, result):
        nonlocal answer
        if index == len(numbers):
            if result == target:
                answer +=1
            return #인덱스랑 길이랑 같으면 멈춤
        dfs(index +1 , result + numbers[index])
        dfs(index +1 , result - numbers[index])
        
    dfs(0,0) #solution내부에 실행 , 첫 시작
    return answer
    