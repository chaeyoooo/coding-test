def solution(a, b):
    weekdays = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month_days = [ 0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = sum(month_days[1: a]) + b
    result = weekdays[(days-1) % 7]
    return result
    