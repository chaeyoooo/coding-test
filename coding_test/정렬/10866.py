from collections import deque
import sys
input = sys.stdin.readline
queue = deque() 
N = int(input())

for _ in range(N):
    command = input().strip()
    if command == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    else:
        command, num = command.split()
        if command == 'push_front':
            queue.appendleft(num)
        else:
            queue.append(num)