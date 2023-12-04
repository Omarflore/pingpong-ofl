import turtle
import random
import time

wn = turtle.Screen()
wn.title("pinpong de omar :3")
wn.bgcolor("green")
wn.setup(width = 800, height = 600)
wn.tracer(0) 

marcadorA = 0
marcadorB = 0

jugadorA = turtle.Turtle()
jugadorA.speed(0) 
jugadorA.shape("square")
jugadorA.color("blue")
jugadorA.penup() 
jugadorA.goto(-350, 0) 
jugadorA.shapesize(stretch_wid=5, stretch_len = 1) 

jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("light green")
jugadorB.penup()
jugadorB.goto(350, 0) 
jugadorB.shapesize(stretch_wid=5, stretch_len = 1) 

pelota = turtle.Turtle()
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0,0) 
pelota.dx = 0.5 
pelota.dy = 0.5 

division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() 
pen.goto(0,260)
pen.write("Jugador A: 0		Jugador B: 0", align = "center", font=("Courier", 24, "normal"))

movimientoA = 0
movimientoB = 0

def jugadorA_up():
    global movimientoA
    movimientoA = 1

def jugadorA_down():
    global movimientoA
    movimientoA = -1

def jugadorA_stop():
    global movimientoA
    movimientoA = 0

def jugadorB_up():
    global movimientoB
    movimientoB = 1

def jugadorB_down():
    global movimientoB
    movimientoB = -1

def jugadorB_stop():
    global movimientoB
    movimientoB = 0

wn.listen()
wn.onkeypress(jugadorA_up, 'w') 
wn.onkeyrelease(jugadorA_stop, 'w') 
wn.onkeypress(jugadorA_down, 's') 
wn.onkeyrelease(jugadorA_stop, 's') 
wn.onkeypress(jugadorB_up, 'Up') 
wn.onkeyrelease(jugadorB_stop, 'Up') 
wn.onkeypress(jugadorB_down, 'Down') 
wn.onkeyrelease(jugadorB_stop, 'Down') 

bolita = turtle.Turtle()
bolita.shape("square")
bolita.color("red")
bolita.penup()
bolita.speed(0)
bolita.goto(0, 0)

bolita_activa = False
tiempo_bolita = 0
bolita.dx = 0.2
bolita.dy = -0.2

bolita_morada = turtle.Turtle()
bolita_morada.shape("triangle")
bolita_morada.color("purple")
bolita_morada.penup()
bolita_morada.speed(0)
bolita_morada.goto(0, 0)

bolita_morada_activa = False
tiempo_bolita_morada = 0
bolita_morada.dx = 0.4  
bolita_morada.dy = -0.4  

contador_pen = turtle.Turtle()
contador_pen.speed(0)
contador_pen.color("white")
contador_pen.penup()
contador_pen.hideturtle() 
contador_pen.goto(0, 0)

contador = 0  

while True:
    wn.update()
    contador += 1  
    contador_pen.clear()
    contador_pen.write(f"Contador: {contador}", align="center", font=("Courier", 24, "normal")) 

    jugadorA.sety(jugadorA.ycor() + movimientoA)
    jugadorB.sety(jugadorB.ycor() + movimientoB)

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1

    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        marcadorA += 1
        pen.clear()
        pen.write("Jugador A: {}		Jugador B: {}".format(marcadorA, marcadorB), align = "center", font=("Courier", 24, "normal"))
        if marcadorA == 10:
            pen.clear()
            pen.write("¡El Jugador A ha ganado!", align = "center", font=("Courier", 24, "normal"))
            break

    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        marcadorB += 1
        pen.clear()
        pen.write("Jugador A: {}		Jugador B: {}".format(marcadorA, marcadorB), align = "center", font=("Courier", 24, "normal"))
        if marcadorB == 10:
            pen.clear()
            pen.write("¡El Jugador B ha ganado!", align = "center", font=("Courier", 24, "normal"))
            break

    if ((pelota.dx > 0) and (350 > pelota.xcor() > 340) and (jugadorB.ycor() + 50 > pelota.ycor() > jugadorB.ycor() - 50)):
        pelota.color("blue")
        pelota.dx *= -1

    elif ((pelota.dx < 0) and (-350 < pelota.xcor() < -340) and (jugadorA.ycor() + 50 > pelota.ycor() > jugadorA.ycor() - 50)):
        pelota.color("red")
        pelota.dx *= -1

    elif (pelota.xcor() > 390):
        pelota.color("green")

    elif (pelota.xcor() < -390):
        pelota.color("green")

    if not bolita_activa:
        tiempo_bolita += 1

    if tiempo_bolita > 100:
        bolita_activa = True
        bolita.goto(random.randint(-390, 390), random.randint(-290, 290))
        tiempo_bolita = 0

    if bolita_activa:
        bolita.setx(bolita.xcor() + bolita.dx)
        bolita.sety(bolita.ycor() + bolita.dy)

    if abs(bolita.xcor()) > 390 or abs(bolita.ycor()) > 290:
        bolita_activa = False
        bolita.goto(1000, 1000)  
        wn.ontimer(lambda: activar_bolita(bolita), 7000)  

    if pelota.distance(bolita) < 20 and bolita_activa:
        marcadorA += 1
        pen.clear()
        pen.write("Jugador A: {}		Jugador B: {}".format(marcadorA, marcadorB), align = "center", font=("Courier", 24, "normal"))
        bolita_activa = False
        bolita.goto(1000, 1000)  

    if not bolita_morada_activa:
        tiempo_bolita_morada += 1

    if tiempo_bolita_morada > 100:
        bolita_morada_activa = True
        bolita_morada.goto(random.randint(-390, 390), random.randint(-290, 290))
        tiempo_bolita_morada = 0

    if bolita_morada_activa:
        bolita_morada.setx(bolita_morada.xcor() + bolita_morada.dx * random.choice([-1, 1]))
        bolita_morada.sety(bolita_morada.ycor() + bolita_morada.dy * random.choice([-1, 1]))

    if abs(bolita_morada.xcor()) > 390 or abs(bolita_morada.ycor()) > 290:
        bolita_morada_activa = False
        bolita_morada.goto(1000, 1000) 
        wn.ontimer(lambda: activar_bolita(bolita_morada), 10000)  

    if pelota.distance(bolita_morada) < 20 and bolita_morada_activa:
        marcadorA -= 3
        pen.clear()
        pen.write("Jugador A: {}		Jugador B: {}".format(marcadorA, marcadorB), align = "center", font=("Courier", 24, "normal"))
        bolita_morada_activa = False
        bolita_morada.goto(1000, 1000)  

    if not bolita_activa:
        tiempo_bolita += 1

    if tiempo_bolita > 100:
        bolita_activa = True
        bolita.goto(random.randint(-390, 390), random.randint(-290, 290))
        tiempo_bolita = 0

    if bolita_activa:
        bolita.setx(bolita.xcor() + bolita.dx)
        bolita.sety(bolita.ycor() + bolita.dy)

    if abs(bolita.xcor()) > 390 or abs(bolita.ycor()) > 290:
        bolita_activa = False
        bolita.goto(1000, 1000) 
        wn.ontimer(lambda: activar_bolita(bolita), 7000)  

    if pelota.distance(bolita) < 20 and bolita_activa:
        marcadorA += 1
        pen.clear()
        pen.write("Jugador A: {}		Jugador B: {}".format(marcadorA, marcadorB), align = "center", font=("Courier", 24, "normal"))
        bolita_activa = False
        bolita.goto(1000, 1000)  