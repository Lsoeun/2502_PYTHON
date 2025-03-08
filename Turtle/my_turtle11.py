import turtle as t
t.shape("turtle")

# 터틀 그래픽 창 설정
window = t.Screen()
window.bgcolor("black")

# 눈사람 얼굴
t.pensize(10)
t.goto(0,0)
t.begin_fill()
t.color("white")
t.circle(50)
t.end_fill()

# 눈사람 몸통
t.penup()
t.goto(0,0)
t.pendown()
t.setheading(180)
t.color("white")
t.begin_fill()
t.circle(80)
t.end_fill()

# 눈 그리기
t.pensize(3)
t.pencolor("brown")
t.penup()
t.goto(-20, 65)
t.begin_fill()
t.fillcolor("brown")
t.pendown()
t.circle(7)
t.end_fill()

t.penup()
t.goto(20, 65)
t.begin_fill()
t.pendown()
t.circle(7)
t.end_fill()

t.hideturtle()
t.done()