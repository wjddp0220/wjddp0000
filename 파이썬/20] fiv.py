name = input("이름 : ")
print("-"*30)
print("%s's fib program"%(name))
print("-"*30)

n = int(input("몇 번째 것을 출력하시겠습니까? : "))
def f(n) :
    if(n<=2):
        return 1
    elif(n>2):
        return f(n-2) + f(n-1)

print(f(n))