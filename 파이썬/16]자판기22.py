name = input("이름 :")
print("-"*30)
print("%s의 아이스크림 자판기"%(name))
print ( "1. 사  과 맛 1400원\n2. 복숭아 맛 1600원\n3. 수  박 맛 1700원\n4. 딸  기 맛 1800원\n5. 멜  론 맛 1900원")
print("-"*30)
list = [1400, 1600, 1700, 1800, 1900]

number = int(input("번호를 입력해주세요 :"))

money= int(input("금액을 투입해주세요 :"))

charge = money - list[number -1]
print("거스름 돈 : %d 원" %(charge))

list = []
n = [5000, 1000, 500, 100]

c= 0
while(charge >= 5000) :
    charge = charge - 5000
    c += 1
list.append(c)


c= 0
while(charge >= 1000) :
    charge = charge - 1000
    c += 1
list.append(c)


c= 0
while(charge >= 500) :
    charge = charge - 500
    c += 1
list.append(c)


c= 0
while(charge >= 100) :
    charge = charge - 100
    c += 1
list.append(c)


n = [5000, 1000, 500, 100]
for i in range(0, 4):
    print("%d원 : %d매" %(n[i], list[i]))
