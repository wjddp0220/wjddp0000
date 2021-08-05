name = input("이름 :")
print("-"*30)
print("%s의 학기 성적 프로그램"%(name))
print("-"*30)


subject = ["국어", "수학", "영어", "과학"]

score = []
for i in subject :
    x = int(input("%s 점수 :" %(i)))
    if(x > 95):
        score.append("A+")

    elif(x > 75):
        score.append("B+")

    elif(x > 55):
        score.append("C+")

    else:
        score.append("F")
for i in range(0, 4) :
    print("%s과목 : %s점" %(subject[i], score[i]))