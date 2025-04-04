# def convertdays(date):
#     year, month, day = map(int, date.split("."))
#     return (year * 12 * 28 ) + (month * 28) + day

# def solution(today, terms, privacies):
#     #딕셔너리로 만들기
#     terms_dict ={}
    
#     for k in terms:
#         newalpha , month = k.split()
#         terms_dict[newalpha] = int(month)
#     print(terms_dict)
        
#     for i in privacies:
#         datetime , alpha = i.split()
#         if alpha == newalpha:
#             if convertdays(datetime) + terms_dict[alpha] * 28 < convertdays(today):
#                 result.append(index(i))
#             else:
#                 break
      
#     return result

def convert_to_days(date): 
    year, month, day = map(int, date.split("."))
    return (year * 12 * 28) + (month * 28) + day

def solution(today, terms, privacies):
    terms_dict = {}
    for k in terms:
        newalpha, month = k.split()
        terms_dict[newalpha] = int(month)  

    result = []  

    for idx, i in enumerate(privacies):
        datetime, alpha = i.split()

        if convert_to_days(datetime) + (terms_dict[alpha] * 28) <= convert_to_days(today):
            result.append(idx + 1)  

    return result

# def convert_to_days(date): 
#     year, month, day = map(int, date.split("."))
#     return (year * 12 * 28) + (month * 28) + day

# def solution(today, terms, privacies):
#     terms_dict = {}
#     for k in terms:
#         newalpha, month = k.split()
#         terms_dict[newalpha] = int(month)  

#     result = []  
#     today_days = convert_to_days(today)  # 오늘 날짜 변환

#     for idx, i in enumerate(privacies):
#         datetime, alpha = i.split()
#         privacy_days = convert_to_days(datetime)
#         expire_days = privacy_days + (terms_dict[alpha] * 28)  # 유효기간 추가된 날짜

#         # 🔥 디버깅용 출력 (값이 정확한지 확인)
#         print(f"개인정보 {idx + 1}: 수집일({datetime}) → {privacy_days}, 만료일({expire_days}), 오늘({today_days})")

#         if expire_days < today_days:  # 만료된 경우
#             result.append(idx + 1)  

#     return result


        