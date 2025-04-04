# def solution(schedules, timelogs, startday):
#     #스케쥴 : 출근 희망시각
#     #timelogs : 일주일 동안 출근한 시각
#     #startday는 1부터 7까지 1~ 5까지 평일 / 6,7 은 주말
    
# #     for k in timelogs:
# #         k = k[0 :7-startday+1] + k[7-startday+2:]
# #         newtimelogs.append(k[:6])
        
# #     answer = 0
# #     return answer
#     newtimelogs =[]
    
#     for log in timelogs:
#         weekdaylog = []
        
#         for i in range(7):
#             day = (startday + i -1) % 7
#             if day < 5:
#                 weekdaylog.append(log[i])
                
#         newtimelogs.append(weekdaylog)
        
#     cnt = 0
#     for k in range(len(newtimelogs)):
#         for j in newtimelogs[k]:
#             if j > schedules[k] + 10:
#                 hour = schedule[k] // 100
#                 time = schedule[k] % 100
#                     if time >= 60:
#                         hour += 1
#                         break
#             else:
#                 cnt+=1
#     return cnt
def solution(schedules, timelogs, startday):
    newtimelogs = []
    for log in timelogs:
        weekdaylog = []
        for i in range(7):
            day = (startday + i - 1) % 7
            if day < 5:
                weekdaylog.append(log[i])
        newtimelogs.append(weekdaylog)
    
    cnt = 0
    for k in range(len(newtimelogs)):
        sch = schedules[k]
        allowed_hour = sch // 100
        allowed_min = sch % 100 + 10
        if allowed_min >= 60:
            allowed_hour += allowed_min // 60
            allowed_min %= 60
        allowed_time = allowed_hour * 100 + allowed_min

        for j in newtimelogs[k]:
            if j > allowed_time:
                break
        else:
            cnt += 1
    return cnt

            