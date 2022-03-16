from sys import stdin



def factorial(var):
    
    if var == 0:
        return 1
    elif var ==1:
        return 1
    else:
        return (factorial(var-1)*var)


def main():
    var = stdin.readline().strip()
    
    if '-' in var and '.' in var: print("Factorial is not defined for negative rational numbers.")
    elif '-' in var and not('.') in var: print("Factorial is not defined for negative integers.")
    elif '.' in var: print("Factorial is only defined for integers.")
    else:
        var = int(var)
        print(factorial(var))
main()
