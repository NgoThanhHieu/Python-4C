from screen import s
from snakee import snakes
from screen import food
from screen import casti_tela
from screen import delay
import random
import time
import turtle


def posunN():
        if snakes.direction != "down":
            snakes.direction = "up"

def posunD():  
        if snakes.direction != "up":
            snakes.direction = "down"
    
def posunL():   
        if snakes.direction != "right":
            snakes.direction = "left"
    
def posunP():
        if snakes.direction != "left":
            snakes.direction = "right"

def move():
    if snakes.direction == "up":
        y = snakes.ycor()
        snakes.sety(y + 20)
    if snakes.direction == "down":
        y = snakes.ycor()
        snakes.sety(y - 20)
    if snakes.direction == "left":
        x = snakes.xcor()
        snakes.setx(x - 20)
    if snakes.direction == "right":
        x = snakes.xcor()
        snakes.setx(x + 20)

s.listen()
s.onkeypress(posunN, "w")
s.onkey(posunD, "s")
s.onkey(posunL, "a")
s.onkey(posunP, "d")

while True:
    s.update()

    if snakes.xcor()>210 or snakes.xcor()<-210 or snakes.ycor()>210 or snakes.ycor()<-210:
        time.sleep(1)
        snakes.goto(0,0)
        snakes.direction = "stop"

    if snakes.distance(food) < 20:

        x = random.randint(-210, 210)
        y = random.randint(-210, 210)
        food.goto(x,y)

        new_casti_tela = turtle.Turtle()
        new_casti_tela.speed(0)
        new_casti_tela.shape("circle")
        new_casti_tela.color("green")
        new_casti_tela.penup()
        casti_tela.append(new_casti_tela)

        delay -= 0.001

    for index in range(len(casti_tela)-1, 0, -1):
        x = casti_tela[index-1].xcor()
        y = casti_tela[index-1].ycor()
        casti_tela[index].goto(x, y)

    if len(casti_tela) > 0:
        x = snakes.xcor()
        y = snakes.ycor()
        casti_tela[0].goto(x,y)

    move()    
  
    time.sleep(delay)