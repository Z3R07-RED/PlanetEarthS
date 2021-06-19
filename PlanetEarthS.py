#!/usr/bin/env python3
# Name        : PlanetEarthS
# Author      : Z3R07-RED
# Last Change : Jun 19 2021 [16:37:08]
#
# dependencies
import turtle
import time
import random

Tmov = 0.1

univ = turtle.Screen()
univ.title("Planet Earth Simulator")
univ.bgcolor("black")
univ.setup(width=600, height=600)
univ.bgpic("spaceblack.gif")
univ.tracer(0)
# VARIABLES
soles = "Sol.gif"
# IMAGENES
univ.register_shape('Sol.gif')
univ.register_shape('Sol2.gif')
univ.register_shape('space.gif')
# TIERRA
tierra = turtle.Turtle()
tierra.speed(0)
tierra.shape("circle")
tierra.color("green")
tierra.penup()
tierra.goto(0, 160)
tierra.direction = "stop"
# SOL
sol = turtle.Turtle()
sol.speed(0)
sol.shape("Sol.gif")
sol.shapesize(3.2, 3.2)
sol.color("orange")
sol.penup()
sol.goto(0, 0)
# TEXTO SOL
solt = turtle.Turtle()
solt.speed(0)
solt.color("white")
solt.hideturtle()
solt.penup()
solt.goto(0, 40)
solt.write("SOL", align="center", font=("Courier", 24, "normal"))
sol.direction = "stop"
# colores = ["red", "magenta", "white", "yellow", "blue", "orange", "grey"]
# TEXTO
texto = turtle.Turtle()
texto.speed(0)
texto.color("cyan")
texto.hideturtle()
texto.penup()
texto.goto(0, 260)
texto.write("D X: 0    D Y: 0", align="center", font=("Courier", 24, "normal"))
# PLANETA GREY
planeta = turtle.Turtle()
planeta.shape("circle")
planeta.shapesize(0.6, 0.6)
planeta.color("gray")
planeta.penup()
planeta.speed(0)
planeta.setposition(random.randint(-280, 280), random.randint(-280, 280))


def animate_sol():
    global soles

    sol.shape(soles)

    if soles == "Sol.gif":
        soles = "Sol2.gif"
    else:
        soles = "Sol.gif"


def arriba():
    tierra.direction = "up"


def abajo():
    tierra.direction = "down"


def izquierda():
    tierra.direction = "left"


def derecha():
    tierra.direction = "right"


def mov():
    if tierra.direction == "up":
        y = tierra.ycor()
        tierra.sety(y + 20)
        tierra.direction = "stop"

    if tierra.direction == "down":
        y = tierra.ycor()
        tierra.sety(y - 20)
        tierra.direction = "stop"

    if tierra.direction == "left":
        x = tierra.xcor()
        tierra.setx(x - 20)
        tierra.direction = "stop"

    if tierra.direction == "right":
        x = tierra.xcor()
        tierra.setx(x + 20)
        tierra.direction = "stop"


univ.listen()
univ.onkeypress(arriba, "Up")
univ.onkeypress(abajo, "Down")
univ.onkeypress(izquierda, "Left")
univ.onkeypress(derecha, "Right")
while True:
    univ.update()
    animate_sol()
    planeta.forward(3)
    mov()
    time.sleep(Tmov)
    x = tierra.xcor()
    y = tierra.ycor()
    texto.clear()
    texto.write("D X: {}    D Y: {}".format(x, y), align="center", font=("Courier", 24, "normal"))
    if sol.distance(tierra) > 220:
        tierra.color("cyan")

    if sol.distance(tierra) < 160:
        tierra.color("green")

    if sol.distance(tierra) < 140:
        tierra.color("lightgreen")

    if sol.distance(tierra) < 120:
        tierra.color("lightblue")

    if sol.distance(tierra) < 90:
        tierra.color("grey")

    if sol.distance(tierra) < 80:
        tierra.color("magenta")

    if sol.distance(tierra) < 60:
        tierra.color("red")

    if sol.distance(tierra) < 50:
        tierra.color("red")
        univ.update()
        tierra.hideturtle()
        tierra.clear()
        texto.color("red")
        sol.color("red")
        sol.shape("Sol2.gif")
        univ.bgpic("space.gif")

    if planeta.distance(tierra) < 20:
        tierra.color("red")
        planeta.color("red")
        univ.update()
        time.sleep(2)
        tierra.hideturtle()
        planeta.hideturtle()
        tierra.clear()
        planeta.clear()
        texto.color("red")
        univ.bgpic("space.gif")


# PLANETA
    if planeta.xcor() > 300 or planeta.xcor() < -300:
        planeta.right(180)
        planeta.left(37)

    if planeta.ycor() > 300 or planeta.ycor() < -300:
        planeta.right(180)
        planeta.left(37)

    if sol.distance(planeta) < 100:
        planeta.color("grey")

    if sol.distance(planeta) < 80:
        planeta.color("magenta")

    if sol.distance(planeta) < 60:
        planeta.color("red")

    if sol.distance(planeta) < 40:
        planeta.color("red")
        sol.color("red")
        sol.shape("Sol2.gif")
        univ.update()
        time.sleep(1)
        planeta.color("magenta")
        planeta.setposition(random.randint(-280, 280), random.randint(-280, 280))
