from sys import stdin
def evaluador(var, var_1):
    if int(var) > int(var_1):
        return ">"
    elif int(var) < int(var_1):
        return "<"
    else:
        return "="

def main():
    var = stdin.readline().strip()
    var_1 = stdin.readline().strip()
    evaluador(var, var_1)
    print(evaluador(var, var_1))

main()
    
