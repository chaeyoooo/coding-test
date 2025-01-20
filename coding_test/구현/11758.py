def ccw(x1, x2, x3, y1, y2, y3):
    cross = (x2 - x1) *  (y3- y1) - (x3 - x1) * (y2 - y1)

    if cross > 0:
        return 1
    elif cross < 0:
        return -1
    else:
        return 0
    
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

print(ccw(x1, x2, x3, y1, y2, y3))