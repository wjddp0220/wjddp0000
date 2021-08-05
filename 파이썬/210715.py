# if elif else

a = "apple"
b = "banana"
c = 1
d = 2

if(a == "apple" and b == "lemon") :
    print("fruit")


#윤년 계산하기

name = input("이름 :")
print("-"*30)
print("%s's Leapyear Program"%(name))
print("-"*30)

n = 5
while(True) :

    year = int(input("연도 :"))

    if (year % 4 == 0) and not(year % 100 == 0) :
        print("%d년은 윤년입니다." %(year))
    elif (year % 400 == 0) :
        print("%d년은 윤년입니다." %(year))
    else :
        print("%d는 윤년이 아닙니다." %(year))
    n -= 1

    if(n == 0) :
        break

#while

fruit = 1
while(fruit < 10) :
    print(str(fruit) + "번째 사과 먹기")
    fruit += 1

print("끝")

while (True) :
    print(str(fruit) + "번째 사과 먹기")