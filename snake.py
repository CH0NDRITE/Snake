import turtle
import random
import time

so = turtle.Turtle()
window = turtle.Screen()
so.pendown()
so.pensize(20)
window.bgcolor('blue')
so.hideturtle()
window.setup(1.0, 1.0)
window.tracer(0)
nah = turtle.Turtle()
nah.hideturtle()
nah.color('white')
nah.shape('circle')
c = turtle.Turtle()
c.hideturtle()
c.speed(0)
c.color('lime')
c.penup()
c.setposition(-730, 350)
c.pendown()
bah = turtle.Turtle()
bah.hideturtle()
bah.color('red')
bah.shape('circle')
bah2 = turtle.Turtle()
bah2.hideturtle()
bah2.color('red')
bah2.shape('circle')
bah3 = turtle.Turtle()
bah3.hideturtle()
bah3.color('red')
bah3.shape('circle')
bah4 = turtle.Turtle()
bah4.hideturtle()
bah4.color('red')
bah4.shape('circle')
bah5 = turtle.Turtle()
bah5.hideturtle()
bah5.color('red')
bah5.shape('circle')

nah.penup()
nah.setpos(random.randint(-500, 500), random.randint(350, 350))
nah.showturtle()
bah.penup()
bah.setpos(random.randint(-500, 500), random.randint(350, 350))
bah.showturtle()
bah2.penup()
bah2.setpos(random.randint(-500, 500), random.randint(350, 350))
bah2.showturtle()
bah3.penup()
bah3.setpos(random.randint(-500, 500), random.randint(350, 350))
bah3.showturtle()
bah4.penup()
bah4.setpos(random.randint(-500, 500), random.randint(350, 350))
bah4.showturtle()
bah5.penup()
bah5.setpos(random.randint(-500, 500), random.randint(350, 350))
bah5.showturtle()

def goleft():
    so.left(30)
def goright():
    so.right(30)

window.onkeypress(goright,'Right')
window.onkeypress(goleft,'Left')
window.listen()

counter = 0
reset = time.time()
ss = 6.5
while True:
    so.color('black')
    so.forward(ss)
    so.color('red')
    so.forward(ss)
    so.color('yellow')
    so.forward(ss)
    so.color('red')
    so.forward(ss)
    window.update()
    if so.distance(nah) < 23:
        nah.hideturtle()
        nah.setpos(random.randint(-500, 500), random.randint(-350, 350))
        nah.showturtle()
        so.clear()
        counter += 1
        c.clear()
        c.write(counter, font=('arial', 50))
        ss += 1.5
    window.update()
    if so.distance(bah) < 23:
        window.bgcolor('red')
        c.penup()
        c.setposition(-300, 0)
        c.color('black')
        c.pendown()
        c.write('GAME OVER!', font=('arial', 80))
        turtle.done()
    window.update()
    if so.distance(bah2) < 23:
        window.bgcolor('red')
        c.penup()
        c.setposition(-300, 0)
        c.color('black')
        c.pendown()
        c.write('GAME OVER!', font=('arial', 80))
        turtle.done()
    window.update()
    if so.distance(bah3) < 23:
        window.bgcolor('red')
        c.penup()
        c.setposition(-300, 0)
        c.color('black')
        c.pendown()
        c.write('Game over!', font=('arial', 80))
        turtle.done()
    window.update()
    if so.distance(bah4) < 23:
        window.bgcolor('red')
        c.penup()
        c.setposition(-300, 0)
        c.color('black')
        c.pendown()
        c.write('GAME OVER!', font=('arial', 80))
        turtle.done()
    window.update()
    if so.distance(bah5) < 23:
        window.bgcolor('red')
        c.penup()
        c.setposition(-300, 0)
        c.color('black')
        c.pendown()
        c.write('GAME OVER!', font=('arial', 80))
        turtle.done()
    window.update()
    if so.xcor() > 750:
        so.penup()
        so.clear()
        so.setx(-750)
        so.pendown()
    window.update()
    if so.xcor() < -750:
        so.penup()
        so.clear()
        so.setx(750)
        so.pendown()
    window.update()
    if so.ycor() > 410:
        so.penup()
        so.clear()
        so.sety(-410)
        so.pendown()
    window.update()
    if so.ycor() < -410:
        so.penup()
        so.clear()
        so.sety(410)
        so.pendown()
    window.update()
    if time.time() - reset > 5:
        bah.hideturtle()
        bah.setpos(random.randint(-500, 500), random.randint(-350, 350))
        bah.showturtle()
        bah2.hideturtle()
        bah2.setpos(random.randint(-500, 500), random.randint(-350, 350))
        bah2.showturtle()
        bah3.hideturtle()
        bah3.setpos(random.randint(-500, 500), random.randint(-350, 350))
        bah3.showturtle()
        bah4.hideturtle()
        bah4.setpos(random.randint(-500, 500), random.randint(-350, 350))
        bah4.showturtle()
        bah5.hideturtle()
        bah5.setpos(random.randint(-500, 500), random.randint(-350, 350))
        bah5.showturtle()
        reset = time.time()
    window.update()
