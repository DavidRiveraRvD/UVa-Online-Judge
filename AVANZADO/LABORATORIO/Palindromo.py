from sys import stdin
def pali(lista , n):
    sal = len(lista) // 2 -1
    if dp[n] != None:
        return dp[n]
    elif len(lista) == 1:
        dp[n] = 1
        return dp[n]
    elif n < sal:
        dp[n] = 0
        return dp[n]
    else:
        if (lista[n]) == (lista[n+1]):
            cont = 2
            salir = 0
            k = n
            while salir ==0 and k > 0:
                if lista[k-1] == lista[n]:
                    cont+=1
                    k+=-1

                else:
                    salir+= 1
            der = lista[n+2:]
            print(k,n)
            print(der)
            lim = k-len(der)
            if k >= len(der):
                izq = lista[lim:k]
                izq = izq[::-1]
                if izq == der:
                    a = cont + (len(der)*2)
                    dp[n] = max(pali(lista , (n-1)), a)
                    return dp[n]
                else:
                    a = 0
                    dp[n] = max(pali(lista , (n-1)), a)
                    return dp[n] 
            else:
                a = 0
                dp[n] = max(pali(lista , (n-1)), a)
                return dp[n] 
        else:
            lon = len(lista[n+1:])
            com = n-lon
            cont = 0
            j = len(lista[com:n]) - 1
            print(lista[com:n],"/",lista[n+1:])
            for i in range (len(lista[com:n])):
                if lista[com:n][j] == lista[n+1:][i]:
                    cont+=1
                j-= 1
            if cont == len(lista[n+1:]):
                a = (cont)*2 + 1
            else:
                a = 0
            dp [n] = max(pali(lista , (n-1)) , a) 
            return dp[n]      
def main():
    T=int(stdin.readline().strip())
    while T!=0:
        cadena=stdin.readline().strip()
        global dp
        a = (len(cadena))
        c = (cadena)
        dp = [None]*(a+1)
        d = (pali(c , a-2))
        if d == 0:
            print((a*2) - 1)
        else:  
            print (a*2 -d)
        T-=1
main()
