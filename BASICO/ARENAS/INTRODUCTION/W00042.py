from sys import stdin

x = int(stdin.readline())
y = int(stdin.readline())

def main():
    if x%y == 0 or y%x == 0:
        print("SI")
    else:
        print("NO")
main()
