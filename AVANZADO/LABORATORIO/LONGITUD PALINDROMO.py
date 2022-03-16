import sys

def Palindrome(numero):
    numero = list(numero)
    long = len(numero)
    numero2 = [[0 for i in range(long)] for j in range(long)]
    
    for i in range(long):
        
        numero2[i][i] = 1
        
    for j in range(1,long):
        
        for i in range(long-1):
            
            indice = i+j
            
            if indice>=long:
                continue
            if numero[i] == numero[indice]:
                if i+1==indice:
                    numero2[i][indice] = 2
                else:    
                    numero2[i][indice] = numero2[i+1][indice-1] + 2 
            else:
                if indice<long:
                    numero2[i][indice] = max(numero2[i+1][indice], numero2[i][indice-1])
    print(numero2)
    return numero2[0][long-1]                

def main():
    
    numero = sys.stdin.readline().strip()
    print(Palindrome(numero))
    
main()
