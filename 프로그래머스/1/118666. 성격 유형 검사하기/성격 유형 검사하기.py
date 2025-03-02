# def solution(survey, choices):
#     choicesdict = {"1" : 3, "2" : 2 , "3" : 1, "4" : 0 , "5" : 1 , "6" : 2, "7" : 3}
    
#     for i in range(len(survey)):
#         survey[i][0] = 0
#         survey[i][0] = 0
#         if 1 <= choices[i] <= 3:
#             survey[i][0] += 1
#         elif choices[i] == 4:
#             break
#         elif 5<= choices[i] <= 7:
#             survey[i][1] += 1
            
#     answer = ""        
#     if R < T :
#         answer += "T"
#     else:
#         answer += "R"
#     if C < F :
#         answer += "F"
#     else:
#         answer += "C"
#     if J < M :
#         answer += "M"
#     else:
#         answer += "J"
#     if A < N:
#         answer +="N"
#     else:
#         answer += "A"


# def solution(survey, choices):
#     score_map = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
#     scores = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    
#     for i in range(len(survey)):
#         first, second = survey[i][0], survey[i][1]
#         choice = choices[i]
#         if choice < 4:
#             # 비동의 계열
#             scores[first] += score_map[choice]
#         elif choice > 4:
#             # 동의 계열
#             scores[second] += score_map[choice]
#         # choice가 4면 아무 점수도 추가하지 않음

#     answer = ""
#     if scores["R"] >= scores["T"]:
#         answer += "R"
#     else:
#         answer += "T"
#     if scores["C"] >= scores["F"]:
#         answer += "C"
#     else:
#         answer += "F"
#     if scores["J"] >= scores["M"]:
#         answer += "J"
#     else:
#         answer += "M"
#     if scores["A"] >= scores["N"]:
#         answer += "A"
#     else:
#         answer += "N"
    
#     return answer

def solution(survey, choices):
    scores = {"A":0, "N":0, "C":0, "F":0, "M":0, "J":0, "R":0, "T":0}
    for idx, choice in enumerate(choices):
        if choice - 4 > 0:
            scores[survey[idx][1]] += choice - 4
        elif choice - 4 < 0:
            scores[survey[idx][0]] += 4 - choice

    type = ""
    if scores["R"] >= scores["T"]:
        type += "R"
    else:
        type += "T"

    if scores["C"] >= scores["F"]:
        type += "C"
    else:
        type += "F"

    if scores["J"] >= scores["M"]:
        type += "J"
    else:
        type += "M"

    if scores["A"] >= scores["N"]:
        type += "A"
    else:
        type += "N"

    return type
        
                