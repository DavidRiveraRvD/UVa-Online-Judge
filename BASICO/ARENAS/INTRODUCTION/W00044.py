from sys import stdin

x = float(stdin.readline())
y = float(stdin.readline())

if x != 0 and 0<=x and 0<=y :
    op = y/x
    area = (op * y) / 2
    per = ((op**2 + y **2)**0.5) + op + y
    print("El area es:", round(area, 2), "y el perimetro es:", round(per, 2))
elif x!=0 and x<0 and y<0:
    x = -(x)
    y= -(y)
    op = y/x
    area = (op * y) / 2
    per = ((op**2 + y **2)**0.5) + op + y
    print("El area es:", round(area, 2), "y el perimetro es:", round(per, 2))
elif x!=0 and x>0 and y<0:
    y= -(y)
    op = y/x
    area = (op * y) / 2
    per = ((op**2 + y **2)**0.5) + op + y
    print("El area es:", round(area, 2), "y el perimetro es:", round(per, 2))
elif x!=0 and x<0 and y>0:
    x = -(x)
    op = y/x
    area = (op * y) / 2
    per = ((op**2 + y **2)**0.5) + op + y
    print("El area es:", round(area, 2), "y el perimetro es:", round(per, 2))
else:
    print("Triangulo Imposible")
