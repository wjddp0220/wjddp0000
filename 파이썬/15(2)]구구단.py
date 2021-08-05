name = input("이름 :")
print("-"*30)
print("%s의 구구단 프로그램"%(name))
print("-"*30)

for f in range(1, 10):
    print("----%d 단----" %(f))
    for i in range(1, 10):
        print("%d*%d = %d"%(f, i, f*i) )