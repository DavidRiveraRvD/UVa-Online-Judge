from sys import stdin

def main():
    var_1 = int(stdin.readline())
    var_2 = int(stdin.readline())
    var_3 = int(var_1+var_2)

    if var_1 < 0:
        if var_2 < 0:
            print("("+str(var_1)+")+"+"("+str(var_2)+")="+str(var_3))
        else:
            print("("+str(var_1)+")+"+str(var_2)+"="+str(var_3))
    elif var_2 <0:
        print(str(var_1)+"+("+str (var_2)+")="+str(var_3))
    else:
        print(str(var_1)+"+"+str(var_2)+"="+str(var_3))
            
main()
