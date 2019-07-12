'''
from tkinter import *
window = Tk()
mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "열기")
fileMenu.add_separator()
fileMenu.add_command(label = "종료")
window.mainloop()
'''
'''
from tkinter import *
from tkinter import messagebox

def fun_open():
    messagebox.showinfo("메뉴 선택", "열기 메뉴 선택함")
def fun_exti():
    window.quit()
    window.destroy()

window = Tk()
mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(window)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "열기", command = fun_open)
fileMenu.add_separator()
fileMenu.add_command(label = "종료", command = fun_exti)

window.mainloop()
'''
'''
from tkinter import *
from tkinter import simpledialog
import random

rd = random

def fun_out():
    value = simpledialog.askinteger("확대배수", "주사위 숫자(1~6)을 입력하세요", minvalue = 1 , maxvalue = 6)
    label1.configure(text = str(value))
def computer():
    label2.configure(text = str(rd))



window = Tk()
window.geometry("200x100")
label1 = Label(window, text = "입력된 값")
label1.pack()

btn = Button(window, text = "입력창 열기", command = fun_out)
btn.pack()

window.mainloop()
'''
'''
from tkinter import *
from tkinter.filedialog import *

def fun_out():
    filename = askopenfilename(parent = w, filetype = ("GIF 파일", "*.gif", ("모든파일", "*.*")))
    label1.configure(text = str(filename))
def fun_save():
    saveFp = asksaveasfile(parent = w, mode="w", defaultextension = ".jpg",
                           filetype = (("JPG 파일", "*.jpg;*.jpeg"), ("모든 파일","*.*")))
    label1.configure(text = str(saveFp))
    saveFp.close()

w = Tk()
w.geometry("400x100")
label1 = Label(w, text = "선택된 파일 이름")
label1.pack()

btn = Button(w, text = "파일열기", command = fun_out)

w.mainloop()
'''
'''
from tkinter import *
from tkinter.filedialog import *

def func_open():
    filename = askopenfilename(parent = w, filetypes = (("GIF 파일", "*.gif"),
                                                             ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo
def func_exit():
    w.quit()
    w.destroy()

w = Tk()
w.geometry("400x400")
w.title("명화 감상하기")
photo = PhotoImage()
pLabel = Label(w, image = photo)
pLabel.pack(expand = 1 ,anchor = CENTER)
mainMenu = Menu(w)
w.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)
w.mainloop()
'''
from tkinter import *
mycolor = "blue"
def paint(event):
    x1, y1 = (event.x-1), (event.y+1)
    x2, y2 = (event.x-1), (event.y+1)
    canvas.create_oval(x1, y1, x2, y2, fill = mycolor)
def change_color():
    global mycolor
    mycolor = "red"

w = Tk()
canvas = Canvas(w)
canvas.pack()
canvas.bind("<B1-Motion>", paint)
button = Button(w, text = "빨강색", command = change_color)
button.pack()
w.mainloop()
