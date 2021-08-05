import random

name = input("이름 : ")
print("-"*30)
print("%s's 숫자게임 program"%(name))
print("-"*30)

print("서로 다른 세 자리 수를 입력하세요. 9번의 기회가 있습니다.")


c100 = random.randrange(0,9)
c10 = random.randrange(0,9)
c1 = random.randrange(0,9)

while(c100 == c10 or c100 == c1 or c10 == c1) :
    c100 = random.randrange(0,9)
    c10 = random.randrange(0,9)
    c1 = random.randrange(0,9)

print("%d%d%d" %(c100, c10, c1))


num = 9
while(num > 0):
    
    n100 = int(input("\n백의 자리 수: "))
    n10 = int(input("십의 자리 수: "))
    n1 = int(input("일의 자리 수: "))


    while(n100 == n10 or n100 == n1 or n10 == n1) :
        print("\n중복되었습니다. 다시 입력해주세요.")

        print("\n서로 다른 세 자리 수를 입력하세요.")
        n100 = int(input("백의 자리 수: "))
        n10 = int(input("십의 자리 수: "))
        n1 = int(input("일의 자리 수: "))


    S = 0
    if(n100 == c100):
        S += 1

    if(n10 == c10):
        S += 1

    if(n1 == c1):
        S += 1

    B = 0
    if(n100 == c10 or n100 == c1):
        B += 1

    if(n10 == c100 or n10 == c1):
        B += 1

    if(n1 == c100 or n1 == c10):
        B += 1

    print("Strike %d , Ball %d " %(S, B))
    num -= 1


    if(S == 3):
        print("정답입니다.")
        break
    elif():
        print(str(num) + "번의 기회가 남았습니다.")
    elif(num == 0):
        print("9번의 기회가 모두 소진되었습니다.")