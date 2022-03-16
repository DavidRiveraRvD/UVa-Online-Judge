from sys import stdin

x = stdin.readline().strip().split()
y = stdin.readline().strip().split()
z = stdin.readline().strip().split()
r = stdin.readline().strip()
t = int(stdin.readline())

def main():
    if r == "u":
        if ((int(x[0]))<=t and int(x[1])>=t) or ((int(y[0]))<=t and (int(y[1])>=t)) or ((int(z[0]))<=t and (int(z[1]))>=t):
            print("Pertenece")
        else:
            print("No pertenece") 
    elif r == "n":
         if ((int(x[0]))<=t and (int(x[1]))>=t) and ((int(y[0]))<=t and (int(y[1]))>=t) and ((int(z[0]))<=t and (int(z[1])>=t)):
            print("Pertenece")
         else:
            print("No pertenece")
    else:
        if ((int(x[0]))<=t and (int(x[1]))>=t) and not ((int(y[0]))<=t and (int(y[1]))>=t) and not ((int(z[0]))<=t and (int(z[1])>=t)):
            print ("Pertenece")
        else:
            print("No pertenece")
main()

