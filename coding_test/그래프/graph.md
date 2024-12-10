스택의 특징
선입후출(FILO, First In Last Out):

먼저 들어간 데이터가 나중에 나옵니다.
예: 접시를 쌓는 것처럼, 마지막에 올려놓은 접시를 먼저 꺼낼 수 있습니다.
후입선출(LIFO, Last In First Out):

나중에 들어간 데이터가 먼저 나옵니다.
예: 책을 쌓는 경우, 가장 위의 책을 먼저 뺄 수 있습니다.

ex ) 세로로 긴 막대기 안에 음료수 들어있다고 가정 , 이러면 먼저 들어간게 나중에 나오고 나중에 들어간게 먼저 나옴
나중에 들어간 데이터를 가장 먼저 뺄 수 있는 것 : pop()

큐
먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조 
ex ) 이건 가로로 된 막대기에 음료수 들어있다고 가정 한 상태임!!

# def dfs(graph, start):
#     visited = []          # 방문한 노드 저장
#     stack = [start]       # 시작 노드를 스택에 추가

#     while stack:          # 스택이 비어있지 않으면 계속 반복
#         node = stack.pop()  # 스택에서 가장 위의 노드를 꺼냄
#         if node not in visited:  # 아직 방문하지 않았다면
#             visited.append(node)  # 방문 처리
#             stack.extend(reversed(graph[node]))  # 연결된 노드들을 스택에 추가
#     return visited

# graph = {
#     1: [2, 4],
#     2: [1, 3, 5],
#     3: [2],
#     4: [1],
#     5: [2]
# }

# # 노드 1에서 탐색을 시작
# dfs(graph, 1)


# 헷갈린 개념 정리 
#extend
# my_list = [1, 2, 3]

# # append 사용
# my_list.append([4, 5])
# print(my_list)  # 출력: [1, 2, 3, [4, 5]] (리스트 자체가 추가됨)

# # extend 사용
# my_list = [1, 2, 3]  # 초기화
# my_list.extend([4, 5])
# print(my_list)  # 출력: [1, 2, 3, 4, 5] (리스트의 요소가 각각 추가됨)

# graph[node]
# graph[node]는 현재 탐색 중인 **노드(node)**와 연결된 인접 노드들의 리스트를 가져옵니다.
# 예를 들어:
# graph = {
#     1: [2, 4],
#     2: [1, 3, 5]
# }
# print(graph[1])  # 출력: [2, 4] (1번 노드에 연결된 노드들)


# reversed(graph[node])
# 역순으로 탐색하기 위해 연결된 노드들의 순서를 뒤집습니다.
# 예를 들어, graph[1]이 [2, 4]라면:
# reversed(graph[1])  # 결과: [4, 2]
