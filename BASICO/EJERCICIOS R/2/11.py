from sys import stdin

def cop(x, y, diner):
    if y == "USD":
        mon = diner/2,895.79
        return mon
    else:
        mon = diner/3595.33
        return mon

def usa(x, y, diner):
    if y == "COP":
        mon = diner*2,895.79
        return mon
    else:
        mon = mon*0,799405242
        return mon
    
def euros(x, y, diner):
    if y == "COP":
        mon = diner*3595.33
        return mon
    else:
        mon = diner*1,25093
        return mon
    

def main():
    x = stdin.readline().strip()
    y = stdin.readline().strip()
    diner = int(stdin.readline().strip())
    if x == "COP":
        cop(x, y, diner)
        Z = cop(x, y, diner)
        print(Z)
    elif x == "USD":
        usa(x, y, diner)
        Z = usa(x, y, diner)
        print(Z)
    else:
        Z = euros(x, y, diner)
        print(Z)
main()
