name = input("이름 :")
print("-"*30)
print("%s의 반복 계산기 프로그램"%(name))
print("-"*30)


num = int(input("몇 번 반복하겠습니까? :"))

while(num > 0) :
    print(str(num) + "번째 반복 중입니다.")
    
    a = int(input("첫 번째 인자"))
    b = int(input("두 번째 인자"))
    print("a+b = %d"%(a+b))
    print("a-b = %d"%(a-b) )
    print("a*b = %d"%(a*b) )
    print("a/b = %d"%(a/b) )
    print("a**b = %d"%(a**b) )
    print("a %" + "b = %d" %(a%b))
    print("a//b = %d"%(a//b) )
    num -= 1