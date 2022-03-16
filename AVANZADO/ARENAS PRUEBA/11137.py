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
    coins = [x**3 for x in range(0,22)]
    dic = {}
    while len (line) > 0:
        n = int(line)
        ans = solve(21, n, coins, dic)
        print(ans)
        line = stdin.readline().strip()
main()

