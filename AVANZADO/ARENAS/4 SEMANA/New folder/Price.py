import sys
sys.setrecursionlimit(10**9)
def Evaluador(lon1,lon2):
    """Funcion implementada por un Ingeniero
    en la materia del grupo PIMO-1"""
    
    global memo
    if memo[lon1][lon2]==None:
        if lon1==0:
            Ans=1
        elif lon2==0:
            Ans=0    
        
        elif lon1>=lon2:
            Ans=Evaluador(lon1-lon2,lon2)+Evaluador(lon1,lon2-1)
        else:
            Ans = Evaluador(lon1,lon2-1)
        
        memo[lon1][lon2]=Ans+1
    return memo[lon1][lon2]-1

def main():
    global memo
    memo = [[None]*1010 for i in range(1010)]
    
    line = sys.stdin.readline().strip().split()
    
    while len(line)!= 0:
        entrada = [int(x) for x in line]
        if entrada==[]:break
        if len(entrada) == 1:
            print(Evaluador(entrada[0], entrada[0]))
            
        elif len(entrada)== 2:
            if entrada[0]==0 and entrada[1]== 0:
                print(1)   
            else:
                print(Evaluador(entrada[0], entrada[1]))
                
        elif len(entrada) == 3:
            if entrada[0]<entrada[1] and entrada[0]<entrada[2]:
                print(0)
                
            elif entrada[0]==0 and entrada[1]== 0:
                print(1)
            
            elif entrada[1]==0:
                b = Evaluador(entrada[0], entrada[2])
                print(b)
            else:
                a =Evaluador(entrada[0],entrada[1]-1)
                b = Evaluador(entrada[0], entrada[2])
                print(b-a)
        line = sys.stdin.readline().strip().split()

main()
