from sys import stdin

def  solve(n, v, coins, dic):
    if (n, v) in dic:
        return dic[(n,v)]
    ans = 0
    if v == 0:
        ans = 1
    elif v != 0 and n == 0:
        ans = 0
    elif v > 0 and coins[n]> v:
        ans = solve(n-1, v, coins, dic)
    elif v > 0 and coins[n] <= v:
        ans = solve(n, v-coins[n], coins, dic) + solve(n-1, v , coins,dic)
    dic[(n,v)] = ans
    return ans

def main():
    line = stdin.readline().strip()
    coins = [x for x in range(1005)]
    
    while len (line) > 0:
        dic = {}
        linea = [int(x) for x in line]
        valor = linea[0]
        """if len(linea) == 2:
            rang1 = linea[1]
        elif len(linea)==3:
            rang1 = linea[1]
            rang2 = linea[2]"""
        
        ans = solve(300, valor, coins, dic)
        print(ans)
        line = stdin.readline().strip()
main()

