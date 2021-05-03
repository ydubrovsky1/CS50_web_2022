import sys

try:
x = int(input("x:"))
y = int(input("Y:"))

except ValueError:
    print("error: input integer values only")
    sys.exit(1)

try:
    result = x/y

except ZeroDivisionError:
    print("error: cannot divide by 0")
    sys.exit(1)

print(f"{x}/{y}={result5}")