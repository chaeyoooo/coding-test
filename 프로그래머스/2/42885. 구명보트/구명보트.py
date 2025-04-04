def solution(people, limit):
    cnt = 0
    for i in range(len(people)):
        for j in range(i+1 , len(people)):
            if people[i] + people[j] <= limit:
                cnt +=1
            
    
    return len(people) - cnt
    # print(people[i] , people[j])
    
#투 포인터 활용
def solution(people , limit):
    people.sort()
    left = 0
    right = len(people)-1
    cnt = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left +=1
        right -= 1
        cnt +=1
        
    return cnt

# 50 50 70 80
            
            