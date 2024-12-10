from collections import deque
queue = deque()
# 빈 deque 객체를 생성합니다.
# queue는 이제 큐처럼 동작할 수 있습니다.
queue.append(5)
queue.append(2)
queue.append(3)

queue.popleft()
# 큐의 가장 앞에 있는 요소를 제거하고 반환합니다.
# 큐는 선입선출(FIFO, First In First Out) 방식으로 작동하므로, 가장 먼저 추가된 5가 제거됩니다.
# 현재 큐의 상태: [2, 3]
