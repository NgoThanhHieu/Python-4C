import turtle

s = turtle.Screen()
s.title("Snake Game🐍")
s.screensize(bg="black")
s.setup(width=500, height=500)

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

casti_tela = []

delay = 0.1