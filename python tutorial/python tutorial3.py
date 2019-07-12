list1 = []
list2 = []
value = 0
for i in range(0,4):
    for k in range(0,5):
        list1.append(value)
        value+=3
    list2.append(list1)
    list1 = []

for i in range(0,4):
    for k in range(0,5):
        print("%3d"% list2[i][k], end = " ")
    print( )

dictionary = {}

print("요소 추가 이전:", dictionary)

dictionary["name"] = "새로운 이름"
dictionary["head"] = "새로운 정신"
dictionary["body"] = "새로운 몸"

print("요소 추가 이후:", dictionary)

dictionary = {
    "name": "7D 건조 망고", "type": "당절임"
}
print("요소제거이전",dictionary)
del dictionary["name"]
del dictionary["type"]
print("요소제거이후",dictionary)

import operator

singer = {}

singer['이름'] = '트와이스'
singer['구성원수'] = 9
singer['데뷔'] = '서바이벌 식스틴'
singer['대표곡'] = 'SIGNAL'

for k in singer.keys():
    print(' %s --> %s' %(k,singer[k]))

singer = sorted(singer.items(),key=operator.itemgetter(0))

print("#1------------------------------------")
hong = {'ko':80, 'en':75, 'math':55}
print(sum(hong.values())/len(hong))

print("#2------------------------------------")
hong = "881120-1068234"
year = hong[:6]
number = hong[7:]
print(year)
print(number)

print("#3------------------------------------")
pin = "881120-1068234"
se = pin[:1]
print(se)

print("#4------------------------------------")
a = "a:b:c:d"
b = a.replace(":","#")
print(b)

print("#5------------------------------------")
mylist = [1,3,5,4,2]
mylist.sort()
print(mylist)

print("#6------------------------------------")
life = ['Life', 'is', 'too', 'short']
print(" ".join(life))


print("#7------------------------------------")
t1 = (1,2,3)
t2 = (4,)
print(t1+t2)

print("#9------------------------------------")
a = {'A':90, 'B':80, 'C':70}
print(a.pop('B'))

print("#10-----------------------------------")
a = [1,1,1,2,2,3,3,3,4,4,5]
print(set(a))

print("#12-----------------------------------")
list = []
s = 0
for i in range(0,5):
    a = int(input("정수>"))
    list.append(a)
    s+=list[i]

min_v, max_v = list[0], list[0]

for i in range(5):
    if min_v>list[i]:min_v=list[i]
    if max_v<list[i]:max_v=list[i]

print(list)
print("합 %d, 평균 %.2f" % (s, s/len(list)))
print("최대값 = %d, 최소값 = %d" % (max_v, min_v))

print("#13-----------------------------------")
import  math
myData = [ int(math.pow(2,num)) for num in range(0,5) if num%2 != 0]
print(myData)

