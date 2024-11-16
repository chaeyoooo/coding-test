N = int(input())
weight_items = [5,3]
count = 0

for weight_item in weight_items:
    count += N//weight_item
    N %= weight_item
    if N == 0:
        print(count)
        break
        