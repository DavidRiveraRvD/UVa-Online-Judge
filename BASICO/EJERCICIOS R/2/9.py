from sys import stdin
import math

def lados(a, b, C):
    c = math.sqrt((b**2)+(a**2)-((2*a*b)*(math.cos(C))))
    return c

def triangulo(c, a, b):
    if a == c and c == b:
        return "Triangulo Equilatero"
    elif a == c or c == b or b == a:
        return "Triangulo Isosceles"
    else:
        return "Triangulo Escaleno"

def perimetro(a, b, c):
    per = a+b+c
    return per

def diferencia(a, b, c):
    if a == b:
        l = (a+b)-c
        return l
    elif c == a:
        l = (c+a)-b
        return l
    else:
        l = (b+c)-a
        return l
    
def ladmax(a, b, c):
    if a>b and a>c:
        return a
    elif b > a and b>c:
        return b
    else:
        return c
    
def main():
    a = float(stdin.readline())
    b = float(stdin.readline())
    C = float(stdin.readline())
    if a>0 and b>0 and 0<C<180 :
        lados(a, b, C)
        c = lados(a, b, C)
        if (c+a)>b and (a+b)>c and (c+b)>a:
            print("Tercer lado: ", c)
            triangulo(c, a, b)
            tipo= (triangulo(c, a, b))
            print(tipo)
            if tipo == "Triangulo Equilatero":
                perimetro(a, b, c)
                y = perimetro(a, b, c)
                print(y)
            elif tipo == "Triangulo Isosceles":
                diferencia(a, b, c)
                k = diferencia(a, b, c)
                print("Su diferencia entre el producto de los dos lados iguales y el otro lado: ", k)
            else:
                ladmax(a, b, c)
                p = ladmax(a, b, c)
                print("La medida del lado más largo: ", p)            

        else:
            print("Triangulo imposible")
            
    else:
        print("Triangulo imposible")
main()
