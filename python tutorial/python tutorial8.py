"""
from tkinter import *

window = Tk()
window.title("윈도창 연습")
window.geometry("400x380+800+200")
window.resizable(width = 1920, height = 1080)

window.mainloop()
"""
"""
from tkinter import *

root = Tk()

label = Label(root, text="Welcome, Please input your name", bg = "beige", font = "arial")
label.pack()

entry = Entry(root, text = "input here", bd = 8, cursor = "pirate")
entry.pack()

button = Button(root, text = "확인", fg = "red", cursor = "arrow", width = 10, height = 1)
button.pack()

root.mainloop()"""

"""
from tkinter import *

window = Tk()

label1 = Label(window, text = "COOKBOOK~~Python을")
label2 = Label(window, text = "열심히", font = ("궁서체", 30), fg = "blue")
label3 = Label(window, text = "공부중입니다.", bg = "magenta", width = 20, height = 5, anchor = SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()"""

'''
from tkinter import *
from tkinter import messagebox

window = Tk()

def myFunc():
    messagebox.showinfo("헤헤헤헤헤헤","동전이얌")

photo = PhotoImage(file = "C:/yeol/0_FW_ 파이썬에서사용할사진_190709/back.gif")
button1 = Button(window, image = photo, command = myFunc())

button1.pack()

window.mainloop()
'''
"""
import tkinter

window = tkinter.Tk()
window.title("YOON MUN YEOL")
window.geometry("640x400+100+100")
window.resizable(False, False)

b1 = tkinter.Button(window, text = "top")
b1_1= tkinter.Button(window, text = "top-1")
b2 = tkinter.Button(window, text = "bottom")
b2_1 = tkinter.Button(window, text = "bottom-1")
b3 = tkinter.Button(window, text = "left")
b3_1 = tkinter.Button(window, text = "left-1")
b4 = tkinter.Button(window, text = "right")
b4_1 = tkinter.Button(window, text = "right-1")
b5 = tkinter.Button(window, text = "center", bg = "red")

b1.pack(side = "top")
b1_1.pack(side = "top", fill = "x")
b2.pack(side = "bottom")
b2_1.pack(side = "bottom", anchor = "e")
b3.pack(side = "left")
b3_1.pack(side = "left", fill = "y")
b1.pack(side = "top")
b1_1.pack(side = "top", fill = "x")
b2.pack(side = "bottom")
b2_1.pack(side = "bottom", anchor = "e")
b3.pack(side = "left")
b3_1.pack(side = "left", fill = "y")
b4.pack(side = "right")
b4_1.pack(side = "right", anchor = "s")
b5.pack(expand=True, fill="both")

window.mainloop()
"""
'''
from tkinter import *
window = Tk()

button1 = Button(window, text = "파이썬 종료", fg = "red", command = quit)

button1.pack()

window.mainloop()'''
'''
from tkinter import *
from tkinter import messagebox

w = Tk()

def myFunc():
    if chk.get() == 0:
        messagebox.showinfo("", "ㅌㅌㅌ")
    else:
        messagebox.showinfo("", "아씨 말로하자")

chk = IntVar()
cd1 = Checkbutton(w, text = "쳐봐색기야", variable = chk, command = myFunc)

cd1.pack()

w.mainloop()
'''
'''
from tkinter import *
w = Tk()

def myFunc():
    if var.get() == 1:
        label1.configure(text = "파이썬")
    elif var.get() == 2:
        label1.configure(text = "C++")
    else:
        label1.configure(text = "java")

var = IntVar()
rb1 = Radiobutton(w, text = "파이썬", variable = var, value = 1, command = myFunc)
rb2 = Radiobutton(w, text = "C++", variable = var, value = 2, command = myFunc)
rb3 = Radiobutton(w, text = "Java", variable = var, value = 3, command = myFunc)
label1 = Label(w, text = "선택한 언어: ", fg = "red")

rb1.pack()
rb2.pack()
rb3.pack()

label1.pack()

w.mainloop()
'''
'''
from tkinter import *

w = Tk()
l1 = Label(w, text = "화씨")
l2 = Label(w, text = "섭씨")
l1.pack()
l2.pack()

e1 = Entry(w)
e2 = Entry(w)
e1.pack()
e2.pack()

b1 = Button(w, text = "화씨->섭씨")
b2 = Button(w, text = "섭씨->화씨")
b1.pack()
b2.pack()

w.mainloop()
'''
'''
from tkinter import *

w = Tk()
l1 = Label(w, text = "화씨")
l2 = Label(w, text = "섭씨")
l1.grid(row = 0, column = 0)
l2.grid(row = 1, column = 0)

e1 = Entry(w)
e2 = Entry(w)
e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)

b1 = Button(w, text = "화씨->섭씨")
b2 = Button(w, text = "섭씨->화씨")
b1.grid(row = 2, column = 0)
b2.grid(row = 2, column = 1)

w.mainloop()
'''
'''
from tkinter import *

w = Tk()

a = Label(w, text = "박스#1", bg = "red", fg = "white")
a.place(x=0, y=0)
a = Label(w, text = "박스#2", bg = "green", fg = "black")
a.place(x=20, y=20)
a = Label(w, text = "박스#3", bg = "blue", fg = "white")
a.place(x=40, y=40)

w.mainloop()
'''
'''
from tkinter import *
window = Tk()

button1 = Button(window, text = "버튼 1")
button2 = Button(window, text = "버튼 2")
button3 = Button(window, text = "버튼 3")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)

window.mainloop()
'''
'''
from tkinter import *

window = Tk()

btnList = [None] * 3

for i in range(0,3):
    btnList[i] = Button(window, text = '버튼' + str(i+1))

for btn in btnList:
    btn.pack(padx = 5, pady = 5)
    btn.pack(side = TOP, fill = X, ipadx = 10, ipady = 10)

window.mainloop()
'''
'''
from tkinter import *
from time import *

fnameList = ["back.GIF", "front.GIF", "rabbit.GIF", "turtle.GIF"]
photoList = [None]*4
num = 0

def clickNext():
    global num
    num +=1
    if num > 8:
        num = 0
    photo = PhotoImage(file = "C:/yeol/0_FW_ 파이썬에서사용할사진_190709/"+fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 3
    photo = PhotoImage(file = "C:/yeol/0_FW_ 파이썬에서사용할사진_190709/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<<이전", command = clickPrev)
btnNext = Button(window, text = "다음>>", command = clickNext)

photo = PhotoImage(file = "C:/yeol/0_FW_ 파이썬에서사용할사진_190709/"+fnameList[0])
pLabel = Label(window, image = photo)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x = 15, y = 50)

window.mainloop()
'''
'''
from tkinter import *

def clickMouse(event):
    txt = ""
    if event.num == 1:
        txt += "마우스 왼쪽 버튼이 ("
    elif event.num == 3:
        txt += "마우스 오른쪽 버튼이 ("
    txt += str(event.y) + "," + str(event.x) + ")에서 클릭됨"
    label1.configure(text = txt)

window = Tk()
window.geometry("400x400")
label1 = Label(window, text = "이곳이 바뀜")
window.bind("<Button>", clickMouse)
label1.pack(expand = 1, anchor = CENTER)

window.mainloop()
'''
'''
from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : "+ chr(event.keycode))

window = Tk()
window.bind("<key>", keyEvent)

window.mainloop()
'''
'''
from tkinter import *

def process():
    temperature = float(e1.get())
    mytemp = (temperature-32)*5/9
    e2.insert(0,str(mytemp))

w = Tk()
l1 = Label(w, text = "화씨", font = 'helvetica 16 italic')
l2 = Label(w, text = "섭씨", font = 'helvetica 16 italic')
l1.grid(row = 0, column = 0)
l2.grid(row = 1, column = 0)

e1 = Entry(w, bg = "yellow", fg = "black")
e2 = Entry(w, bg = "yellow", fg = "black")
e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)

b1 = Button(w, text = "화씨->섭씨", command = process)
b2 = Button(w, text = "섭씨->화씨")
b1.grid(row = 2, column = 0)
b2.grid(row = 2, column = 1)

w.mainloop()
'''

#1 ppt
'''
from tkinter import *

def hi():
    print("파이썬에 오신 것을 환영합니다.!")

w = Tk()
label = Label(w, text = "간단한 GUI 프로그램!")
label.pack()

button = Button(w, text = "환영합니다.", command = hi)
button.pack()

exit_button = Button(w, text = "종료", command = w.quit)
exit_button.pack()

w.mainloop()
'''
#2 ppt


#계산기

from tkinter import *
w = Tk()
w.title("계산기")
display = Entry(w, width = 33, bg = "white")
display.grid(row = 0, column = 0, columnspan = 5)

button_list = ['7','8','9','/','C',
               '4','5','6','*','계',
               '1','2','3','-','산',
               '0','.','=','+','기']

row_index = 1
col_index = 0
for button_text in button_list:
    def process(t=button_text):
        click(t)
    Button(w, text = button_text, width = 5, command = process).grid(row = row_index, column = col_index)
    col_index += 1

    if col_index > 4:
        row_index += 1
        col_index = 0

    def click(key):
        if key == "=":
            result = eval(display.get())
            s = str(result)
            display.insert(END, "="+s)
        elif key == "C":
            display.delete(0, int(display.get().__len__()))
        else:
            display.insert(END, key)

w.mainloop()

'''
from tkinter import *
from tkinter import messagebox



w = Tk()
lb1 = Label(w, text = "몸무게", width = 10)
lb2 = Label(w, text = "신장(cm)", width = 10)
lb1.grid(row = 0, column = 0)
lb2.grid(row = 1, column = 0)

e1 = Entry(w, bg = "white")
e2 = Entry(w, bg = "white")
e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)

message = IntVar()

button = Button(w, text = "결과확인", width = 20)
button.grid(row = 2, column = 0, columnspan = 2, ipadx =40)

lb3 = Label(w, text = "당신의 BMI 지수는 뭐시기입니다.", bg = "grey", width = 20, height = 0, anchor = SE)
lb3.grid(row = 3, column = 0)

w.mainloop()
'''
