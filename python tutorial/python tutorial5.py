#outFp = None
#outStr = ""

#outFp = open("C:\yeol/data.txt", "w")

#while True:
#    outStr = input("내용입력>")
#    if outStr != "":
#        outFp.writelines(outStr + "\n")
#    else:
#        break

#outFp.close()
#print("--- 정상적으로 파일에 씀 ---")

#inFp, outFp = None, None
#inStr = ""

#inFp = open("C:/Windows/win.ini","r")
#outFp = open("C:\yeol/data.txt", "w")

#inList = inFp.readlines()
#for inStr in inList:
#    outFp.writelines(inStr)

#inFp.close()
#outFp.close()
#print("--- 파일이 정상적으로 복사되었슴 ---")

#hp = 280
#hit = ""
#try:
#    sf = open("C:\yeol/save.txt","r")
#    hp = int(sf.read())
#    sf.close()
#    print("세이브 파일 불러오는중")
#except:
#    print("세이브 파일이 없습니다.")
#
#print("현재 체력은 {} 입니다".format(hp))
#while hit != "save" and hp > 0:
#    hit = input("데미지를 몇 입었습니까 :")
#    if hit == "save":
#        f = open("C:\yeol/save.txt", "w")
#        f.write(str(hp))
#        f.close()
#    else:
#       hit = int(hit)
#        hp = hp - hit
#        print("체력이 {} 남았습니다.".format(hp))




a,b = input("숫자 2개 입력>").split()
a,b = map(int,input("숫자 2개 입력>").split())
print(a+b)

#2
#f = open('C:\yeol/replace.txt', 'r')
#b = f.read()
#f.close()
#b = b.replace('삐', '빠')
#f = open('C:\yeol/replace.txt', 'w')
#f.write(body)
#f.close()

#3
#birth = {"홍길동":"2000년 3월 1일", "김춘추":"604년", "김유신":"595년"}
#a = ""

#while a != "q":
#    a = input("생일을 알고 싶은 사람을 입력하세요 : ")
#    try:
#        print(birth[a])
#    except KeyError:
#        print("데이터베이스에 존재하지 않는 이름입니다.")

#6
#f1 = open("C:\yeol/test.txt", 'w')
#f1.write("Life is too short!")
#f1.close()
#
#f2 = open("C:\yeol/test.txt", 'r')
#print(f2.read())
#f2.close()

#7
#user_input = input("저장할 내용을 입력하세요:")
#f = open('C:\yeol/test.txt', 'a')
#f.write(user_input)
#f.write("\n")
#f.close()

#8
#f = open('C:\yeol/test.txt', 'r')
#body = f.read()
#f.close()

#body = body.replace('java', 'python')
#
#f = open('C:\yeol/test.txt', 'w')
#f.write(body)
#f.close()

#9
#f = open('C:\yeol/loop.txt', 'at')
#for i in range(1,101):
#    f.write("%d " %i)
#f.write("\n")
#f.close()

#10
#f = open('C:\yeol/practice.txt', 'w')
#for i in range(1,6):
#    f.write("제%d원소 " %i)
#f.close()
