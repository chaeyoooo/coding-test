n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort(reverse=True)
b.sort()
k = 0
for i in range(n):
    k += a[i] * b[i]
print(k)

# 헷갈렸던 개념 정리 1
# sort()는 반환값이 없기 때문에 별도로 정렬된 결과를 저장하지 않아도 되고, 원본 리스트 자체를 정렬합니다. 
# 즉, sort()를 호출하면 원본 리스트가 바로 변경되므로, 정렬된 결과를 저장할 필요가 없음

# a = [3, 1, 4]
# a.sort()  # a 리스트 자체가 정렬됩니다.
# print(a)  # 출력: [1, 3, 4]

# sorted()는 정렬된 새로운 리스트를 반환하기 때문에, 원본 리스트는 그대로 유지됩니다.
# 정렬된 결과를 사용하려면 반드시 새로운 변수에 저장해야 합니다.

# a = [3, 1, 4]
# b = sorted(a)  # 새로운 리스트 b에 정렬된 결과 저장
# print(a)  # 출력: [3, 1, 4] (원본 리스트는 변경되지 않음)
# print(b)  # 출력: [1, 3, 4] (새로운 정렬된 리스트)

# 헷갈렸던 개념 정리 2
# k가 정수형(int)**인데, sum() 함수는 **iterable 객체(리스트, 튜플 등)**에서만 사용 가능합니다.
#  정수형은 iterable 객체가 아니기 때문에 TypeError가 발생합니다.