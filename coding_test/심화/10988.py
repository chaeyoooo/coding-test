a = input() 
#여기서 문자열 받으니까 a+1을 하면 문자열에 +1 (즉 12345+1 이 안되는 것 처럼)
for i in range(len(a)): #a+1이 아니라 len(a)로 해야함
    if a[i] != a[-(i+1)]: #a+1이 아니라 a[-(i+1)]로 해야함
     print(0)
     break #break 를 넣어야됨! 개별이 아니라 전체 해야하니까 
else:
 print(1)