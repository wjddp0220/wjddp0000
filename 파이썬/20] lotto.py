import random
name = input("이름 :")
print("-"*30)
print("%s's lotto program"%(name))
print("-"*30)


n = int(input("몇 번 출력하시겠습니까? :"))


for i in range(0, n) :
    list = [0, 0, 0, 0, 0 ,0]
    list[0] = random.randrange(1, 40)
    list[1] = random.randrange(1, 40)
    list[2] = random.randrange(1, 40)
    list[3] = random.randrange(1, 40)
    list[4] = random.randrange(1, 40)
    list[5] = random.randrange(1, 40)
    
    while (list[0] == list[1]):
        list[1] = random.randrange(1, 40)
    while (list[0] == list[2] or list[1] == list[2]):
        list[2] = random.randrange(1, 40)
    while (list[0] == list[3] or list[1] == list[3] or list[2] == list[3]):
        list[3] = random.randrange(1, 40)
    while (list[0] == list[4] or list[1] == list[4] or list[2] == list[4] or list[3] == list[4]):
        list[4] = random.randrange(1, 40)
    while (list[0] == list[5] or list[1] == list[5] or list[2] == list[5] or list[3] == list[5] or list[4] == list[5]):
        list[5] = random.randrange(1, 40)
        
    list.sort()
    print("[%s]" %(list))