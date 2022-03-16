from sys import stdin

def evaluador(x, y, z):
    if x+y > z and y+z>x and z+x>y:
        print ("OK")
    else:
        print("Wrong!")
    

def main():
    x, y, z = stdin.readline().strip().split(" ")
    z = int(z)
    x = int(x)
    y = int(y)
    evaluador(x, y, z)
main()
