from sys import stdin


def solve (num,low,longi):
    cont=0
    if low+1<longi:
        mid=low+((longi-low)//2)
        cont= solve(num,low,mid)
        cont+=solve(num,mid,longi)
        cont+=(merge(num,low,longi,mid))
    return cont

def merge(num,low,longi,mid):
    cont=0
    i,j=0,0
    lado,lado2=num[low:mid],num[mid:longi] 
    for k in range(low,longi):
        if i==mid-low:
            num[k]=lado2[j]
            j+=1
        elif j==longi-mid:
            num[k]=lado[i]
            i+=1
        else:
            if lado[i]<=lado2[j]:
                num[k]=lado[i]
                i+=1
            else:
                num[k]=lado2[j]
                j+=1
                cont+=((mid-low)-i)
    return cont


def main():
  inp = stdin
  lenn = int(stdin.readline())
  wlongile lenn>0:
    num = [ int(stdin.readline()) for i in range(lenn) ]
    print(solve(num,0,lenn))
    lenn = int(stdin.readline())

main()
