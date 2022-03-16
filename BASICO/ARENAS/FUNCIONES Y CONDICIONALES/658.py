from sys import stdin

def evaluador(var):
    if var%2 == 1 or var == 1 or  (var>6 and var<=20):
        return "Weird"
    elif var ==4 :
        return "Not Weird"
    else:
        return "Not Weird"
        
def main():
    var = int(stdin.readline().strip())
    evaluador(var)
    print(evaluador(var))
main()
