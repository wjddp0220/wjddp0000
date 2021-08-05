#연산프로그램
name = input("이름 :")
print("*"*20)
print("%s의 첫 번째 연산 프로그램" %(name))
print("*"*20)

a = 10
b = 12

print("%d - %d = %d" %(a, b, a-b)) #뺄셈
print("%d + %d = %d" %(a, b, a+b)) #덧셈
print("%d * %d = %d" %(a, b, a*b)) #곱셈
print("%d / %d = %d" %(a, b, a/b)) #나눗셈
print("%d // %d = %d" %(a, b, a//b)) #몫
print("%d ** %d = %d" %(a, b, a**b)) #제곱
print("%d"%(a), "%", "%d = %d" %(b, a%b)) #나머지



# 연산 2

# int 정수 / float 실수 / str 문자열
a = int(input("첫 번째 인자 :"))
b = float(input("두 번째 인자 :"))
print(a - b)

# 문자열 연산
a1 = "apple"
b1 = "banana"
print(a1 + b1)
print(a1*3)

# 문자열 길이
print(a1[1])
print(a1[1:4])
print(b1[:4])

# ...
print(b1.count('b')) #count = find
print(a1.find('p'))
print(a1.upper()) #대문자로 변환
print(b1.upper())
print(b1.replace("a", "b")) #a를 b로 변환
