name = input("이름 :")
print("-"*30)
print("%s's score program"%(name))
print("-"*30)

score =int(input("점수 :"))
if (score == 100):
    print("A+")

elif(score > 75):
    print("B+")

elif(score > 55):
    print("C+")

else:
    print("F")