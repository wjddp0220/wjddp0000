# for

a = [1, 2, 3, 4, 5] #리스트
for i in a :
    print(i)

a = ["a", "b", "c", "d", "e"]
for i in a :
    print(i) #문자열도 출력가능

score = [100, 90, 80, 70, 60, 50]

for s in score :
    if(s == 100):
        print("A")
    elif(s > 70):
        print("B")
    else :
        print("F")

number = 0
for i in range(0, 11):
    number += i
print(number)

