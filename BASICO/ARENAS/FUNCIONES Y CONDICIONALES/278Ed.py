from sys import stdin

def evaluador(x, y, z):
    if x == "k":
        if (y%2)!=0 and (z%2)!=0:
            s = ((y * z)+1)//2
          
            return s

        else:
            s = (y*z)//2
            return s
        
    elif x == "r" or x == "Q":
        if y>z:
            return z
        elif y<z:
            return y
        else:
            return y
    else:
        if y %2 == 0 and z % 2 ==0:
            s=((y//2)*(z//2))
            return s
        elif y %2 != 0 and z%2 != 0:
            s = ((y//2)*(z//2)) +1
            return s
        elif y%2 !=0:
            s= ((z//2))*((y+1)//2)
            return s
        else:
            s= ((z+1)//2)*((y)//2)

def main():
    
    x = stdin.readline().strip()
    y = int(stdin.readline())
    z = int(stdin.readline())
    print(evaluador(x, y, z))
    evaluador(x, y, z)
    
main()
    
