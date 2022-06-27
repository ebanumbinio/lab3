import sys
print("Podaj liczbeN1: ")
x=sys.stdin.readline() 
print("Podaj liczbeN2: ")
y=sys.stdin.readline() 
x=int(x)
y=int(y)
result=x*y
result=str(result)
sys.stdout.write(result)