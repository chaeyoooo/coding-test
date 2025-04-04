def solution(N, stages): #N은 전체 스테이지 갯수 / stages 는 사용자가 멈춰 있는 스테이지 번호
    # 실패율 = 스테이지 도달 but 클리어 x / 스테이지 도달
    answer = []
    reached = len(stages)
    #for문을 돌면서 N개를 돈다 그리고 stages에 1이 있다면 빼고 그 숫자를
    for i in range(1, N+1): #1번 부터 5번까지
        if i in stages:
            stopped = stages.count(i) #1의 갯수
            failure = stopped / reached
            reached -= stopped
            answer.append((i, failure))
        else:
            answer.append((i, 0))
    


#count의 쓰임 , 실패율을 기준으로 i 정렬 하는거 애먹음
    answer.sort(key = lambda x: -x[1]) #x1을 가지고 정렬
    return [real for real, failure in answer]
            
    