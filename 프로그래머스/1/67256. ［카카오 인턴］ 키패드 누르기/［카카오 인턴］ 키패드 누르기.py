def solution(numbers, hand):
    answer = ""
    left = "*"
    right = "#"
    array = [[1,2,3],
            [4,5,6,],
            [7,8,9,],
            ["*" , 0 , "#"]]
    a = {array[row][col]: (row, col) for row in range(len(array)) for col in range(len(array[row]))}
    print(a)
    
    def distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    for i in numbers:
        if i in [1,4,7]:
            answer += "L"
            left = i
        elif i in [3,6,9]:
            answer += "R"
            right = i
        elif i in [2,5,8,0]:
            leftdist = distance(a[i], a[left])
            rightdist = distance(a[i], a[right])
            if leftdist == rightdist:
                if hand == "right":
                    answer += "R"
                    right = i
                else:
                    answer += "L"
                    left = i  
            elif leftdist < rightdist:
                answer += "L"
                left = i
            elif leftdist > rightdist:
                answer += "R"
                right = i    
                
    return answer
            
            