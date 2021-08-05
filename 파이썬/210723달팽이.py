A = int(input("낮에 올라간 길이 : "))
B = int(input("밤에 내려간 길이 : "))
V = int(input("막대기 길이 : "))

day = 1

while(True):
    snail = (A*day)-(B*(day - 1))

    if(snail >= V):
        print("%d일" %(day))
        break

    day += 1





#(2 - 1)*4 + 2 