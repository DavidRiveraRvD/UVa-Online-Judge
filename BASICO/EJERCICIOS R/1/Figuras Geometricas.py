from sys import stdin
import turtle
wn = turtle.Screen()
t = turtle.Turtle()
print ("MENU\n1. Cuadrado\n2. Circulo\n3. Triangulo\n4.Pentagono")
var_1 = int(input("Opcion que va a tomar para calcular: "))

if var_1 == (1):
    lado = int(input("Lado a calcular: "))
    t.pensize(10)
    t.pencolor("red")
    t.forward(lado)
    t.left(90)
    t.forward(lado)
    t.left(90)
    t.forward(lado)
    t.left(90)
    t.forward(lado)
elif var_1 == 2:
    radio = int(input("Digite el radio: "))
    t.pensize(10)
    t.pencolor("orange")
    t.circle(radio)
elif var_1 == 3:
    trian_1 = int(input("Digite el lado del triangulo N° 1: "))
    trian_2 = int(input("Digite el lado del triangulo N° 2: "))
    ang = int(input("Digite el angulo del triangulo: "))
    t.pensize(10)
    t.pencolor("yellow")
    t.forward(trian_1)
    t.left(180-ang)
    t.forward(trian_2)
    t.goto(0, 0)
elif var_1 == 4:
    lado = int(input("Lado a calcular: "))
    t.pensize(10)
    t.pencolor("blue")
    t.forward(lado)
    t.left(72)
    t.forward(lado)
    t.left(72)
    t.forward(lado)
    t.left(72)
    t.forward(lado)
    t.left(72)
    t.forward(lado)
else:
    print("ERROR!!!")
    
