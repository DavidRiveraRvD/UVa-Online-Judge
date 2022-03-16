from sys import stdin
import turtle
def fun(n,lon,var):
    '''Funcion que dibuja el copo de nieve'''
    if n==0:
        var.color("red")
        var.forward(lon)
    else :
        fun (n-1,lon/3,var)
        var.left(60)
        var.color("red")
        fun (n-1,lon/3,var)
        var.right(120)
        var.color("red")
        fun (n-1,lon/3,var)
        var.left(60)
        var.color("red")
        fun (n-1,lon/3,var)

def main():
    '''Funcion que recibe la entrada de picos del copo'''
    n=stdin.readline()
    n = int(n)
    var= turtle.Turtle()
    var.speed(50)
    fun(n,250,var)
    wn = turtle.Screen()
main()
