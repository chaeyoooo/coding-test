meeting = int(input()) 
list = []
for i in range(meeting):
    start , end = map(int, input().split())
    list.append((start, end))

# print(list)

list.sort(key = lambda x: (x[1], x[0]))

# print(list)

count = 0
end_time = 0

for start , end in list:
    if start >= end_time:
        count += 1
        end_time = end

print(count)