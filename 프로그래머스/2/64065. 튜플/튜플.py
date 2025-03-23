def solution(s):
    # 문자열을 리스트로 변환
    s = s[2:-2]  # 바깥 "{{ }}" 제거
    s = s.split("},{")  # "},{" 기준으로 split
    
    
    # 문자열 > 리스트 변환
    real = [list(map(int, x.split(','))) for x in s]
    
    # 정렬
    real.sort(key=len)
    
    
    #추가
    answer = []
    for i in real:
        for j in i:
            if j not in answer:
                answer.append(j)

    return answer



