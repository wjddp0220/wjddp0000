#1. 이름 입력 -> 프로그램 제목
#2. 나의 점수 입력 받기
#3. 나머지 9명의 점수를 리스트로
#4. 리스트에 내 점수 추가
#5. 리스트 정렬(순서대로)
#6. 내 점수 등수 출력(몇번째, index)(위치반환)
#<등수 알아내기>

name = input("이름 :")
print("-"*30)
print("%s's ranking program"%(name))
print("-"*30)

score = int(input("점수 :")) #int 정수니까 꼭!
list = [50, 48, 49, 44, 30, 25, 19, 32, 40]

list.append(score)
list.sort()
list.reverse()
list.index(score)
print("%s님의 등수 : %d" %(name, list.index(score)))