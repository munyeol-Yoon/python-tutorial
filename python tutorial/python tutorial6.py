class Car:
    count = 2
    def __init__(self, name ,color, speed):
        self.name = name
        self.color = color
        self.speed = speed
        if Car.count == 0:
            print("남아있는차가 없습니다.")
        else:
            Car.count -= 1
    def show_info(self):
        print("{} {}을 구매했습니다.".format(self.name, self.color))
        print("{}는 {}의 속도로 달리고있습니다.".format(self.name, self.speed))
    def upSpeed(self, speed):
        if self.speed >= 150:
            print("{}이상 속도를 올릴수 없습니다!! 벌금좀쌜걸".format(self.speed))
        if self.speed < 150:
            self.speed += speed
            print("{}의 속도 : {}".format(self.name ,self.speed))
    def set_name(self, name):
        self.name = name
    def get_name(self, name):
        return self.name
class Sedan(Car):
    def upSpeed(self, speed):
        self.speed += speed
        if self.speed > 150:
            self.speed = 150
        print("현재 속도(서브 클래스) : {} ".format(self.speed))


car1 = Car("소나타", "빨간색", 0)
print(Car.count)
car2 = Sedan("아방띠", "노란색", 0)
print(Car.count)
car3 = Car("펠리셰이드", "검정색", 0)
print(Car.count)
print(car1.name)
print(car1.color)
print("속도",car1.speed)
car1.show_info()
car1.upSpeed(10)
car1.upSpeed(20)
car1.upSpeed(120)
car1.upSpeed(10)
car1.show_info()
car2.upSpeed(130)
car2.upSpeed(20)
car2.upSpeed(10)
car2.show_info()

class A:
    def __init__(self):
        print("A.__init__()")
        self.message = "HELLO"
class B(A):
    def __init__(self):
        print("B.__init__()")
        super().__init__()
        print("self.message : "+self.message)

obj = B()

class SuperClass:
    def method(self):
        pass
class SubClass1(SuperClass):
    def method(self):
        print("SubClass1에서 method()를 오버라이딩함")
class SubClass2(SuperClass):
    pass

sub1 = SubClass1()
sub2 = SubClass2()
sub1.method()
sub2.method()

print("#1---------------------------------------------------------------")
class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year
    def print(self):
        print("제목 : {} ".format(self.name))
        print("제작년도 : {}년".format(self.year))

my_movie1 = Movie("스파이더맨", 2019)
my_movie1.print()

print("#2---------------------------------------------------------------")
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
    def show(self):
        print("제목 : {}".format(self.name))
        print("저자 : {}".format(self.author))

my_book1 = Book("사피엔스", "유발하라리")
my_book1.show()

print("#3---------------------------------------------------------------")
class Rect:
    def __init__(self, width, column):
        self.width = width
        self.column = column
    def area(self):
        result = 0
        result = self.width * self.column
        print("넓이 : {}".format(result))
    def around(self):
        result = 0
        result = (self.width+self.width)+(self.column+self.column)
        print("둘레 : {}".format(result))

num1 = Rect(10,20)
num1.area()
num1.around()

print("#4---------------------------------------------------------------")
class Point:
    def __init__(self, x=10, y=10):
        self.__x = x
        self.__y = y
    def set(self, x, y):
        self.__x = x
        self.__y = y
    def setX(self, x):
        self.__x = x
    def getX(self):
        return self.__x
    def setY(self, y):
        self.__y = y
    def getY(self):
        return self.__y
    def show_info(self):
        print("(x,y)=({},{})".format(self.__x, self.__y))

my_point = Point()
my_point.show_info()
my_point.set(10,20)
my_point.show_info()


print("#5---------------------------------------------------------------")
class Dog:
    def __init__(self, name, type, age):
        self.__name = name
        self.__type = type
        self.__age = age
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setType(self, type):
        self.__type = type
    def getType(self):
        return self.__type
    def setAge(self, age):
        self.__age = age
    def getAge(self):
        return self.__age
    def show_info(self):
        print("이름 : {} \n종류 : {} \n나이 : {}".format(self.__name, self.__type, self.__age))

my_dog1 = Dog("이쁜이", "푸들", "1살")
my_dog1.show_info()
my_dog1.setName("★강형욱★")
my_dog1.setType("애완동물마스터(애완동물의 경계대상)")
my_dog1.setAge("34살")
my_dog1.show_info()

print("#6---------------------------------------------------------------")
class Box:
    def __init__(self, width, column, deep):
        self.__width = width
        self.__column = column
        self.__deep = deep
    def empty(self):
        if Box(0,0,0) == Box(0,0,0):
            return True
        else:
            return False
    def setWidth(self, width):
        self.__width = width
    def setColumn(self, column):
        self.__column = column
    def setDeep(self, deep):
        self.__deep = deep
    def getWidth(self):
        return self.__width
    def getColumn(self):
        return self.__column
    def getDeep(self):
        return self.__deep
    def show_info(self):
        print("가로>{} 세로>{} 깊이>{} empty>{}".format(self.__width, self.__column,
                                                  self.__deep, self.empty()))

my_box = Box(1,1,1)
my_box.show_info()

print("#7---------------------------------------------------------------")
class Rect:
    def __init__(self, width=1, column=1):
        self.__width = width
        self.__column = column
    def area(self):
        return self.__width * self.__column
    def around(self):
        return 2*(self.__width + self.__column)

num1 = Rect(10,20)
print("넓이 : {}".format(num1.area()))
print("둘레 : {}".format(num1.around()))

class Vol(Rect):
    def __init__(self, width = 1, column = 1, vol = 1):
        super().__init__(width, column)
        self.__vol = vol
    def volum(self):
        return self.area()*self.__vol
    def around(self):
        return 2*(super().around() + 2 * self.__vol)

obj = Vol()
print("부피 : {}".format(obj.volum()))
print("둘레 : {}".format(obj.around()))

print("#8---------------------------------------------------------------")
class People:
    def __init__(self, name = "", tel = ""):
        self.__name = name
        self.__tel = tel
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setTel(self, tel):
        self.__tel = tel
    def getTel(self):
        return self.__tel

class Customer(People):
    def __init__(self, name = "", tel = "", mile = 0):
        super().__init__(name, tel)
        self.__mile = mile
    def setMile(self, mile):
        self.__mile = mile
    def getMile(self):
        return self.__mile
    def show_info(self):
        print("이름 : {}".format(self.getName()))
        print("전화번호 : {}".format(self.getTel()))
        print("마일리지 : {}".format(self.getMile()))
    def __str__(self):
        out = "이름 : "+ self.getName()
        out += "\n전화번호 : "+ self.getTel()
        out += "\n마일리지 : "+ str(self.getMile())
        return out

obj = Customer("홍길동", "010-0000-0000", 100)
print(obj)
