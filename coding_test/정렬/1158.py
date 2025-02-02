N, K = list(map(int, input().split()))
stack = []

for i in range(1, N + 1):
    stack.append(i)

result = []

while stack:
    for i in range(K - 1):
        stack.append(stack.pop(0))
    result.append(stack.pop(0))

print("<" + ", ".join(map(str, result)) + ">")


#시간 초과 해결 : deque 사용
# pop(0)은 O(n)이므로 시간 초과가 발생한다.
# deque의 popleft()는 O(1)이므로 시간 초과가 발생하지 않는다.

from collections import deque

N, K = map(int, input().split())
stack = deque()

for i in range(1, N + 1):
    stack.append(i)

result = []

while stack:
    for i in range(K - 1):
        stack.append(stack.popleft())  # pop(0) 대신 popleft() 사용
    result.append(stack.popleft())  # pop(0) 대신 popleft() 사용

print("<" + ", ".join(map(str, result)) + ">")

