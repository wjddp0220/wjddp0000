name = input("이름 : ")


list1 = [["0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0"]]

list2 = [["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]]

movie = []
theater = []
seatrow = []
seatline = []

while(True):
    print("\n", "-*" * 8, "%s의 영화예매기" %(name), "-*" *8)
    print(" 1. 일반상영관 : 닥터 스트레인지", "\n 2. 특별상영관 : 어벤져스 5", "\n 3. 예매 완료(티켓출력)")
    print("-*" * 23)

    num = int(input("번호를 선택해주세요 : "))
    
    while(num >= 4):
        print("\n잘못 선택하셨습니다. 다시 입력해주세요.")
        num = int(input("번호를 선택해주세요 : "))


    if(num == 1):
        movie.append("닥터 스트레인지")
        theater.append("일반상영관")
        print("1열",list1[0], "\n2열",list1[1], "\n3열",list1[2], "\n4열",list1[3], "\n5열",list1[4])
        print("*-" *20)
        print("좌석을 입력해주세요.")
        row = int(input("열 : "))
        line = int(input("행 : "))

        while(row > len(list1) or line > len(list1[0])):
            print("잘못 입력하셨습니다. 다시 좌석을 입력해주세요.")
            row = int(input("열 : "))
            line = int(input("행 : "))

    elif(num == 2):
        movie.append("어벤져스 5")
        theater.append("특별상영관")
        print("1열",list2[0], "\n2열",list2[1], "\n3열",list2[2], "\n4열",list2[3], "\n5열",list2[4] ,"\n6열",list2[5])
        print("*-" * 20)
        print("좌석을 입력해주세요.")
        row = int(input("열 : "))
        line = int(input("행 : "))

        while(row > len(list2[0]) or line > len(list2)):
            print("잘못 입력하셨습니다. 다시 좌석을 입력해주세요.")
            row = int(input("열 : "))
            line = int(input("행 : "))

    elif(num == 3):
        break

    
    while(True):
        if(list1[row-1][line-1] == "X"):
            print("이미 선택된 좌석입니다. 다시 좌석을 입력해주세요.")
            row = int(input("열 : "))
            line = int(input("행 : "))

            while(row > len(list1[0]) or line > len(list1)):
                print("잘못 입력하셨습니다. 다시 좌석을 입력해주세요.")
                row = int(input("열 : "))
                line = int(input("행 : "))
            

        elif(list2[row-1][line-1] == "X"):
            print("이미 선택된 좌석입니다. 다시 좌석을 입력해주세요.")
            row = int(input("열 : "))
            line = int(input("행 : "))

            while(row > len(list2[0]) or line > len(list2)):
                print("잘못 입력하셨습니다. 다시 좌석을 입력해주세요.")
                row = int(input("열 : "))
                line = int(input("행 : "))

        else:
            break


    if (list1[row-1][line-1] == "0"):
        list1[row-1][line-1] = "X"
        
    elif (list2[row-1][line-1] == "0"):
        list2[row-1][line-1] = "X"

    
    print("%d열 %d행을 선택하셨습니다." %(row, line))


    if(list1[row-1][line-1] == "X"):
        seatrow.append(str(row) + "열")
        seatline.append(str(line) + "행")

    elif(list2[row-1][line-1] == "X"):
        seatrow.append(str(row) + "열")
        seatline.append(str(line) + "행")


print("-"*15, "영화 관람표", "-"*15)

for i in range(0, len(seatrow)):
    print("영화 : %s \n상영관 : %s \n좌석 : %s %s \n" %(movie[i], theater[i], seatrow[i], seatline[i]))

print("-"*40)
