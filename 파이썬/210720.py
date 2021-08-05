import random
print(random.random)
print(random.randrange(1,10))

import random
list = [1, 2, 3, 4, 5]
for i in list :
    print(random.randrange(1,10))

import random
abc = ["a", "b", "c", "d", "e"]
random.shuffle(list)
print(list)

def function() :
    print("함수 입니다.")

function()
#a = 10 #문자열도 가능function(a)

def function():
    return 10

function()


#def 함수명 (매개변수) :
    #함수가 해야할 일
    #return 돌려줄 것
