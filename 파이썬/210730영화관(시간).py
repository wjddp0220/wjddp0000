import datetime
now = datetime.datetime.now()

time1 = [now.replace(hour=7, minute=30, second=0, microsecond=0), now.replace(hour=9, minute=40, second=0, microsecond=0), 
        now.replace(hour=12, minute=20, second=0, microsecond=0), now.replace(hour=14, minute=30, second=0, microsecond=0),
        now.replace(hour=18, minute=10, second=0, microsecond=0), now.replace(hour=20, minute=20, second=0, microsecond=0)]
        
time2 = [now.replace(hour=10, minute=30, second=0, microsecond=0), now.replace(hour=12, minute=00, second=0, microsecond=0), 
        now.replace(hour=12, minute=20, second=0, microsecond=0), now.replace(hour=13, minute=50, second=0, microsecond=0),
        now.replace(hour=14, minute=10, second=0, microsecond=0), now.replace(hour=15, minute=40, second=0, microsecond=0)]

list1 = [["0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0"]]
list2 = [["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
list3 = [["0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0"]]
list4 = [["0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0"]]
list5 = [["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
list6 = [["0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0"]]

movie = []
seatrow = []
seatline = []
movietime = []

name = input("이름 : ")

while(True):
    print("\n", "-*" * 8, "%s의 영화예매기" %(name), "-*" *8)
    print(" "*20, "<영 화>", " "*20)
    print(" 1. 닥터 스트레인지", "\n 2. 어벤져스 5", "\n 3. 예매 완료(티켓출력)")
    print("-*" * 23)

    num = int(input("번호를 선택해주세요 : "))
    while(num >= 4):
        print("잘못 입력하셨습니다.")
        num = int(input("번호를 선택해주세요 : "))

    if(num == 1):
        movie.append("닥터 스트레인지")
        print("-" * 20, "시간 대", "-" *20)
        if(now > time1[0] or now > time1[1]):
            print("2. %s ~ %s" %(time1[2],time1[3]), "\n3. %s ~ %s"% (time1[4],time1[5]))
            print("-" * 40)
            time = int(input("시간 대를 선택해주세요 : "))
            while(time == 1 or time >= 4):
                print("잘못입력하셨습니다.")
                time = int(input("시간 대를 선택해주세요 : "))

        elif(now > time1[2] or now > time1[3]):
            print("3. %s ~ %s" % (time1[4],time1[5]))
            print("-" * 40)
            time = int(input("시간 대를 선택해주세요 : "))
            while(time == 2 or time == 1 or time >= 4):
                print("잘못입력하셨습니다.")
                time = int(input("시간 대를 선택해주세요 : "))
            
        elif(now > time1[0]):
            print("1. %s ~ %s"% (time1[0],time1[1]), "\n2. %s ~ %s"% (time1[2],time1[3]), "\n3. %s ~ %s"% (time1[4],time1[5]))
            print("-" * 40)
            time = int(input("시간 대를 선택해주세요 : "))
            while(time >= 4):
                print("잘못입력하셨습니다.")
                time = int(input("시간 대를 선택해주세요 : "))

        while(now > time2[4] or now > time2[5]):
            print("예매 가능한 시간이 없습니다. 이전 단계로 돌아갑니다.")
            print("\n", "-*" * 8, "%s의 영화예매기" %(name), "-*" *8)
            print(" "*20, "<영 화>", " "*20)
            print(" 1. 닥터 스트레인지", "\n 2. 어벤져스 5", "\n 3. 예매 완료(티켓출력)")
            print("-*" * 23)
            num = int(input("번호를 선택해주세요 : "))


        print("\n","*-" * 8, "좌 석", "*-" *8)
        row = 0
        line = 0
        if(time == 1):
            movietime.append("%s ~ %s"% (time2[0],time2[1]))
            print("1열",list1[0], "\n2열",list1[1], "\n3열",list1[2], "\n4열",list1[3], "\n5열",list1[4])
            print("*-" *20)
            print("좌석을 입력해주세요.")
            row = int(input("열 : "))
            line = int(input("행 : "))

            while(row > len(list1) or line > len(list1[0])):
                print("잘못 입력하셨습니다. 다시 좌석을 입력해주세요.")
                row = int(input("열 : "))
                line = int(input("행 : "))

            if(list1[row-1][line-1] == "X"):
                print("이미 선택된 좌석입니다. 다시 좌석을 입력해주세요.")
                row = int(input("열 : "))
                line = int(input("행 : "))

            while(row > len(list1[0]) or line > len(list1)):
                print("잘못 입력하셨습니다. 다시 좌석을 입력해주세요.")
                row = int(input("열 : "))
                line = int(input("행 : "))

            if (list1[row-1][line-1] == "0"):
                list1[row-1][line-1] = "X"

        elif(time == 2):
            movietime.append("%s ~ %s"% (time2[2],time2[3]))
            print("1열",list2[0], "\n2열",list2[1], "\n3열",list2[2], "\n4열",list2[3], "\n5열",list2[4] ,"\n6열",list2[5])
            print("*-" * 20)
            print("좌석을 입력해주세요.")

            row = int(input("열 : "))
            line = int(input("행 : "))

            while(row > len(list2) or line > len(list2[0])):
                print("잘못 입력하셨습니다. 다시 좌석을 입력해주세요.")
                row = int(input("열 : "))
                line = int(input("행 : "))
            
            if(list2[row-1][line-1] == "X"):
                print("이미 선택된 좌석입니다. 다시 좌석을 입력해주세요.")
                row = int(input("열 : "))
                line = int(input("행 : "))

            while(row > len(list2[0]) or line > len(list2)):
                print("잘못 입력하셨습니다. 다시 좌석을 입력해주세요.")
                row = int(input("열 : "))
                line = int(input("행 : "))

            if (list2[row-1][line-1] == "0"):
                list2[row-1][line-1] = "X"

        elif(time == 3):
            movietime.append("%s ~ %s" % (time2[4],time2[5]))
            print("1열",list3[0], "\n2열",list3[1], "\n3열",list3[2], "\n4열",list3[3], "\n5열",list3[4])
            print("*-" *20)
            print("좌석을 입력해주세요.")
            row = int(input("열 : "))
            line = int(input("행 : "))

            while(row > len(list3) or line > len(list3[0])):
                print("잘못 입력하셨습니다. 다시 좌석을 입력해주세요.")
                row = int(input("열 : "))
                line = int(input("행 : "))

            if(list3[row-1][line-1] == "X"):
                print("이미 선택된 좌석입니다. 다시 좌석을 입력해주세요.")
                row = int(input("열 : "))
                line = int(input("행 : "))

            while(row > len(list3[0]) or line > len(list3)):
                print("잘못 입력하셨습니다. 다시 좌석을 입력해주세요.")
                row = int(input("열 : "))
                line = int(input("행 : "))

            if (list3[row-1][line-1] == "0"):
                list3[row-1][line-1] = "X"


    elif(num == 2):
        movie.append("어벤져스 5")
        print("-" * 20, "시간 대", "-" *20)
        if(now > time1[0] or now > time1[1]):
            print("2. %s ~ %s" %(time1[2],time1[3]), "\n3. %s ~ %s" %(time1[4],time1[5]))
            print("-" * 40)
            time = int(input("시간 대를 선택해주세요 : "))
            while(time == 1 or time >= 4):
                print("잘못입력하셨습니다.")
                time = int(input("시간 대를 선택해주세요 : "))

        elif(now > time1[2] or now > time1[3]):
            print("3. %s ~ %s" % (time1[4],time1[5]))
            print("-" * 40)
            time = int(input("시간 대를 선택해주세요 : "))
            while(time == 1 or time ==2 or time >= 4):
                print("잘못입력하셨습니다.")
                time = int(input("시간 대를 선택해주세요 : "))

        elif(now > time1[0]):
            print("1. %s ~ %s"% (time1[0],time1[1]), "\n2. %s ~ %s"% (time1[2],time1[3]), "\n3. %s ~ %s"% (time1[4],time1[5]))
            print("-" * 40)
            time = int(input("시간 대를 선택해주세요 : "))
            while(time >= 4):
                print("잘못입력하셨습니다.")
                time = int(input("시간 대를 선택해주세요 : "))

        while(now > time1[4] or now > time1[5]):
            print("예매 가능한 시간이 없습니다. 이전 단계로 돌아갑니다.")
            print("\n", "-*" * 8, "%s의 영화예매기" %(name), "-*" *8)
            print(" "*20, "<영 화>", " "*20)
            print(" 1. 닥터 스트레인지", "\n 2. 어벤져스 5", "\n 3. 예매 완료(티켓출력)")
            print("-*" * 23)

            num = int(input("번호를 선택해주세요 : "))

        print("\n","*-" * 8, "좌 석", "*-" *8)
        row = 0
        line = 0
        if(time == 1):
            movietime.append("%s ~ %s"% (time2[0],time2[1]))
            print("1열",list4[0], "\n2열",list4[1], "\n3열",list4[2], "\n4열",list4[3], "\n5열",list4[4])
            print("*-" *20)
            print("좌석을 입력해주세요.")
            row = int(input("열 : "))
            line = int(input("행 : "))

            while(row > len(list4) or line > len(list4[0])):
                print("잘못 입력하셨습니다. 다시 좌석을 입력해주세요.")
                row = int(input("열 : "))
                line = int(input("행 : "))

            if(list4[row-1][line-1] == "X"):
                print("이미 선택된 좌석입니다. 다시 좌석을 입력해주세요.")
                row = int(input("열 : "))
                line = int(input("행 : "))

            while(row > len(list4[0]) or line > len(list4)):
                print("잘못 입력하셨습니다. 다시 좌석을 입력해주세요.")
                row = int(input("열 : "))
                line = int(input("행 : "))


            if (list4[row-1][line-1] == "0"):
                list4[row-1][line-1] = "X"


        elif(time == 2):
            movietime.append("%s ~ %s"% (time2[2],time2[3]))
            print("1열",list5[0], "\n2열",list5[1], "\n3열",list5[2], "\n4열",list5[3], "\n5열",list5[4] ,"\n6열",list5[5])
            print("*-" * 20)
            print("좌석을 입력해주세요.")

            row = int(input("열 : "))
            line = int(input("행 : "))

            while(row > len(list5) or line > len(list5[0])):
                print("잘못 입력하셨습니다. 다시 좌석을 입력해주세요.")
                row = int(input("열 : "))
                line = int(input("행 : "))
            
            if(list5[row-1][line-1] == "X"):
                print("이미 선택된 좌석입니다. 다시 좌석을 입력해주세요.")
                row = int(input("열 : "))
                line = int(input("행 : "))

            while(row > len(list5[0]) or line > len(list5)):
                print("잘못 입력하셨습니다. 다시 좌석을 입력해주세요.")
                row = int(input("열 : "))
                line = int(input("행 : "))

            if (list5[row-1][line-1] == "0"):
                list5[row-1][line-1] = "X"

        elif(time == 3):
            movietime.append("%s ~ %s" % (time2[4],time2[5]))
            print("1열",list6[0], "\n2열",list6[1], "\n3열",list6[2], "\n4열",list6[3], "\n5열",list6[4])
            print("*-" *20)
            print("좌석을 입력해주세요.")
            row = int(input("열 : "))
            line = int(input("행 : "))

            while(row > len(list6) or line > len(list6[0])):
                print("잘못 입력하셨습니다. 다시 좌석을 입력해주세요.")
                row = int(input("열 : "))
                line = int(input("행 : "))

            if(list6[row-1][line-1] == "X"):
                print("이미 선택된 좌석입니다. 다시 좌석을 입력해주세요.")
                row = int(input("열 : "))
                line = int(input("행 : "))

            while(row > len(list6[0]) or line > len(list6)):
                print("잘못 입력하셨습니다. 다시 좌석을 입력해주세요.")
                row = int(input("열 : "))
                line = int(input("행 : "))

            if (list6[row-1][line-1] == "0"):
                list6[row-1][line-1] = "X"

    elif(num == 3):
        break

    print("-" * 40)
        
    print("%d열 %d행을 선택하셨습니다." %(row, line))

    if(list1[row-1][line-1] == "X"):
        seatrow.append(str(row) + "열")
        seatline.append(str(line) + "행")

    elif(list2[row-1][line-1] == "X"):
        seatrow.append(str(row) + "열")
        seatline.append(str(line) + "행")

    elif(list3[row-1][line-1] == "X"):
        seatrow.append(str(row) + "열")
        seatline.append(str(line) + "행")

print("-"*15, "영화 관람표", "-"*15)

for i in range(0, len(seatrow)):
    print("영화 : %s \n상영시간 : %s \n좌석 : %s %s \n" %(movie[i], movietime[i], seatrow[i], seatline[i]))

print("-"*40)


while(True):
    print("팝콘을 구매하시겠습니까?")
    print("1. 예", "2.아니오")
    popnum = int(input("번호를 입력해주세요 : "))
    if(popnum == 1):
        print("*"*10, "MENU", "*"*10)
        print("1. 오리지널 팝콘(L) : 5,100원", "\n2. 오리지널 팝콘(M) : 3,100원", "\n3. 어니언 팝콘(L) : 6,100원", "\n4. 어니언 팝콘(M) : 4,100원"
                "\n5. 카라멜 팝콘(L) : 6,100원", "\n6. 카라멜 팝콘(M) : 4,100원", "\n7. 초콜릿 팝콘(L) : 6,600원", "\n8. 초콜릿 팝콘(M) : 4,600원" )
        print("*"*25)

        popcorn = [5000, 6000, 6000, 6500, 3000, 4000, 4000, 4500]

        number = int(input("번호를 입력해주세요 : "))

        money = int(input("금액을 넣어주세요 : "))

        charge = money - popcorn[number-1]

        print("-"*20)
        print("거스름돈 : ")
        
        c = 0
        while(charge >= 5000):
            c += 1
            charge = charge - 5000
            print("5000원 : %d매" %(c))

        c = 0
        while(charge >= 1000):
            c += 1
            charge = charge - 1000
            print("1000원 : %d매" %(c))

        c = 0
        while(charge >= 500):
            c += 1
            charge = charge - 500
            print("500원 : %d매" %(c))

        c = 0
        while(charge >= 100):
            c += 1
            charge = charge - 100
            print("100원 : %d매" %(c))

        print("-"*20)
        
    if(popnum == 2):
        break

