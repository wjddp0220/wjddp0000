A = int(input("기본 고정 비용 : ")) 
B = int(input("한 대의 기계를 생산할 때 드는 비용 : ")) 
C = int(input("기계 1개 당 판매되는 가격 : ")) 



count = A/(C-B) + 1

if(B>C):
    print("-1")
else:
    print(int(A/(C-B) + 1))