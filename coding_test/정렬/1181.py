
n = int(input())  
a = [input().strip() for _ in range(n)]  


a = list(set(a))


for i in range(len(a)):
    min_index = i  
    for j in range(i + 1, len(a)):  
        if len(a[min_index]) > len(a[j]) or (len(a[min_index]) == len(a[j]) and a[min_index] > a[j]):
            min_index = j  

   
    a[i], a[min_index] = a[min_index], a[i]


for word in a:
    print(word)

#시간 초과 

n = int(input()) 
words = set()  


for _ in range(n):
    words.add(input())


sorted_words = sorted(words, key=lambda x: (len(x), x))


for word in sorted_words:
    print(word)
