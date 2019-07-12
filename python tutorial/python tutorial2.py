# 1 번
#sum=0
#for i in range(11):
#    sum+=i
#print("1부터 10까지합 = "+str(sum))
# 2 번 
#sum2 = 0
#n = int(input("정수입력>"))
#for i in range(n+1):
#    sum2+=i
#print(sum2)
# 3 번 구구단
#dan = int(input("단입력>"))
#for i in range(1,10):
#    print("{}*{}={}".format(dan,i,dan*i))
#3 all
#i, k = 0,0
#for i in range(2,10,1):
#    for k in range(1,10,1):
#        print("%d X %d = %2d" % (i,k,i*k))
#        print("")

# 6번 카페주문
#while True:
#    print("손님 주문하시겠습니까? ")
#    order = (int(input("<1>카페라떼 <2>카푸치노 <3>아메리카노 <4>그만시킬래요 ==>")))
#    if order == 1: print("#카페라떼를 주문하셨습니다.")
#    elif order == 2: print("#카푸치노를 주문하셨습니다.")
#    elif order == 3: print("#아메리카노를 주문하셨습니다.")
#    elif order == 4: break
#print("주문하신 커피 준비하겠습니다.")

# 7번 가위바위보 게임
import random

print("*****가위바위보게임*****")
while True:
    print("다음 중 하나를 선택하세요.")
    user = (int(input("가위(0), 바위(1), 보(2), 종료(3)")))
    com = random.randint(0, 2)
    if user == 3:
        break
    elif com == 0:
        print("컴퓨터는 가위를 냈습니다.")
        if user == 0:
            print("비겼습니다.")
        elif user == 1:
            print("이겼습니다.")
        elif user == 2:
            print("졌습니다.")
    elif com == 1:
        print("컴퓨터는 바위를 냈습니다.")
        if user == 0:
            print("졌습니다.")
        elif user == 1:
            print("비겼습니다.")
        elif user == 2:
            print("이겼습니다.")
    elif com == 2:
        print("컴퓨터는 보를 냈습니다.")
        if user == 0:
            print("이겼습니다.")
        elif user == 1:
            print("졌습니다.")
        elif user == 2:
            print("비겼습니다.")
print("종료합니다")
