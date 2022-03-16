from sys import stdin
    
            
    
def main():
    global m, n, t, memo
    cad = stdin.readline().strip().split()
    while cad != []:
        lista = [int(x) for x in cad]
        m, n, t = lista[0], lista[1], lista[2]
        memo = [None for i in range(t+1)]
        memo[0]=0

        if m<=t:
            memo[m]=1
        if n<=t:
            memo[n]=1
        for j in range(1,t+1):
            if memo[j]>=0:
                if j+m<=t:
                    memo[j+m] = max(memo[j+m],memo[j]+1)
                if j+n<=t:
                    memo[j+n] =max(memo[j+n], memo[j]+1)

        if memo[t]<0:
            poker = 1
            while memo[t-poker]== None:
                poker+=1
            print('{} {}'.format(memo[t-poker],poker))
        else:
            print(memo[t])
                    

        cad = stdin.readline().strip().split()

main()
