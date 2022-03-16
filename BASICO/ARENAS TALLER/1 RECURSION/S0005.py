from sys import stdin



def factorial(var):
    if var ==1:
        return 1
    else:
        return (factorial(var-1)*var)

def evaluador(var):
    if  var > 0 and (var - int(var)) != 0:
        print("Factorial is only defined for integers.")
    else:
        if var < 0 and (var - int(var)) != 0:
            print("Factorial is not defined for negative rational numbers.")
        elif var<0:
            print("Factorial is not defined for negative integers.")
        else:
            print(int(factorial(var)))

def main():
    var = float(stdin.readline())
    evaluador(var)
main()
