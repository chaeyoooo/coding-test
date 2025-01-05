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

