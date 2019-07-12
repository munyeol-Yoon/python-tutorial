import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("green")

#1
#t.pensize(3)
#t.forward(100)
#t.left(90)
#t.forward(100)
#t.right(90)
#t.forward(100)
#t.right(90)
#t.forward(100)
#t.left(90)
#t.forward(100)

#2
#t.width(10)
#t.forward(100)
#t.left(90)
#t.forward(100)

#3
#t.color("blue")
#t.forward(100)

#4
#t.shape("square")
#t.forward(100)

#5
#t.circle(100)
#t.up()
#t.goto(190, 0)
#t.down()
#t.circle(100)
#t.up()
#t.goto(-190, 0)
#t.down()
#t.circle(100)
#t.up()
#t.goto(95, -130)
#t.down()
#t.circle(100)
#t.up()
#t.goto(-95, -130)
#t.down()
#t.circle(100)

#6
#radius = 50
#n = 20
#t.goto(0,0)
#t.circle(radius)
#t.up()
#t.goto(100,0)
#t.down()
#t.circle(radius+n)
#t.up()
#t.goto(200,0)
#t.down()
#t.circle(radius+n*2)

#7
#side = 100
#for i in range(3):
#    t.forward(side)
#    t.left(120)

#8
#side = 100
#angle = 90
#for i in range(4):
#    t.forward(side)
#    t.right(angle)
#t.left(angle)
#for i in range(4):
#    t.forward(side)
#    t.right(angle)
#t.left(angle)
#for i in range(4):
#    t.forward(side)
#    t.right(angle)
#t.left(angle)
#for i in range(4):
#    t.forward(side)
#    t.right(angle)

#9
#num1 = str(input("색상 #1을 입력하시오"))
#num2 = str(input("색상 #2를 입력하시오"))
#num3 = str(input("색상 #3을 입력하시오"))

#t.fillcolor(num1)
#t.begin_fill()
#t.circle(50)
#t.end_fill()
#t.up()
#t.goto(100,0)
#t.down()
#t.fillcolor(num2)
#t.begin_fill()
#t.circle(50)
#t.end_fill()
#t.up()
#t.goto(200,0)
#t.down()
#.fillcolor(num3)
#t.begin_fill()
#t.circle(50)
#t.end_fill()

#10
"""def draw_hexa():
    for i in range(6):
        t.forward(50)
        t.right(60)

for j in range(6):
    t.forward(50)
    t.left(60)
    draw_hexa()"""

#11
def draw_line():
    sum = 0
    for i in range(12):
        sum += 30
        t.forward(100)
        t.backward(100)
        t.setheading(sum)

draw_line()

turtle.exitonclick()
