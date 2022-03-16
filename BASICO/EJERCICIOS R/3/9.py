from sys import stdin
import turtle

def arbol(tam,prof,var):
    '''Funcion que dibuja el arbol'''
    if prof==0:
        var.forward(0)
    else:
        var.color("black")
        var.pensize(3)
        var.forward(tam)
        var.pensize(2)
        var.color("green")
        var.left(30)
        arbol(tam*2/3, prof-1,var)
        var.right(60)
        arbol(tam*2/3, prof-1,var)
        if prof>3:
            var.color ("black")
            var.left(30)
            var.back(tam)
        else:
            var.color("green")
            var.left(30)
            var.back(tam)
def main():
    '''Funcion que recibe el n de ramas'''
    b= stdin.readline()
    b = int(b)
    var= turtle.Turtle()
    var.speed(50)
    wn = turtle.Screen()
    var.left (90)
    arbol(100,b,var)
    var.speed(50)
main()
