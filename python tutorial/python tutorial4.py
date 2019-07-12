
print("#1----------------------------------------------")
name = (str(input("이름>")))
def happyBirthday(name):
    print("Happy Birthday to you !")
    print("Happy Birthday to you !")
    print("Happy Birthday, dear {}".format(name))
    print("Happy Birthday to you !")
happyBirthday(name)

print("#2----------------------------------------------")
num1 = (int(input("첫 번째 정수>")))
num2 = (int(input("두 번째 정수>")))
def sum(num1,num2):
    print("정수 {} + {} 의 합은?".format(num1,num2))
    return num1+num2
print(sum(num1,num2))

print("#3----------------------------------------------")

def circleArea(radius):
    print("반지름이 {}인 원의 넓이: {}".format(radius, radius*radius*3.14))
    return radius*radius*3.14
def circleRound(radius):
    print("반지름이 {}인 원의 둘레: {}".format(radius,radius*2*3.14))
    return radius*2*3.14

circleArea(12)
circleRound(12)

print("#4----------------------------------------------")
def add(a,b):
    print("({} + {}) = {}".format(a,b,a+b))
    return a+b
def minus(a,b):
    print("({} - {}) = {}".format(a,b,a-b))
    return a-b
def double(a,b):
    print("({} X {}) = {}".format(a,b,a*b))
    return a*b
def mod(a,b):
    print("({} / {}) = {}".format(a,b,a/b))
    return a/b

add(20,10)
minus(20,10)
double(20,10)
mod(20,10)

print("#5----------------------------------------------")
number = (int(input("정수입력>")))

def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

print(is_odd(number))

print("#6----------------------------------------------")

def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1,3,4,7,8,9,10))

print("#9----------------------------------------------")
def myRange(start, end, hop =1):
    retVal = start
    while retVal <= end:
        yield retVal
        retVal += hop

hap = 0
for i in myRange(1,5,2):
    hap += i

print(hap)
print("#10----------------------------------------------")
cArea = lambda radius: radius*radius*3.14
result = cArea(12)
print(result)
cRound = lambda radius: radius*2*3.14
result = cRound(12)
print(result)

add = lambda a,b: a+b
result = add(20,10)
print(result)
minus = lambda a,b: a-b
result = minus(20,10)
print(result)
double = lambda a,b: a*b
result = double(20,10)
print(result)
mod = lambda a,b: a/b
result = mod(20,10)
print(result)
