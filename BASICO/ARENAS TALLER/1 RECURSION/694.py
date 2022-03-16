from sys import stdin

def primera(a,b,cont):
    if a != 1 and a <=b and a>0 and b>0:
        if a % 2 == 0:
            return(primera(a//2, b, cont+1))
        else:
            return(primera(a*3+1, b, cont+1))
    else:
        if a==1:
            return cont + 1
        else:
            return cont

def main(cont1=1):
    a, b = stdin.readline().split(" ")

    a = int(a)
    b = int(b)
    cont = 0
    
    if a<0 and b<0: return
    else:
        print("Case " + str(cont1) +  ": A = " + str (a)   +", limit = " + str(b) +", number of terms = " + str(primera(a,b,cont)))
        return main(cont1 +1)
main()

