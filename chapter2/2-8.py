#함수
def open_account():  #전달값이 없는 함수
    print("새로운 계좌가 생성되었습니다.")

open_account()

def deposit(balance, money): #전달값이 있는 함수
    print(f"입금이 완료 되었습니다. 잔액은 {balance + money}원 입니다.")
    return balance + money #반환값이 있는 함수

def withdraw(balance, money): #출금
    if balance >= money:
        print(f"출금이 완료 되었습니다. 잔액은 {balance - money}원 입니다.")
        return balance - money
    else:
        print(f"출금이 완료되지 않았습니다. 잔액은 {balance}원 입니다.")
        return balance
    
def withdraw_night(balance, money): #저녁에 출금
    commission = 100 #수수료 100원
    return commission, balance - money - commission

balance = 0 #잔액
balance = deposit(balance,1000) #함수를 호출해서 잔액에 1000원을 입금하고 이를 balance에 저장
# balance = withdraw(balance,500)
commission, balance = withdraw_night(balance, 500)
print(f"수수료 {commission}원이며, 잔액은 {balance}원 입니다.")