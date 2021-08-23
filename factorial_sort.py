# __Author__ __Lencof__
# factorial_sort.py

number = 5

def factorial(n):
    if n == 0:
        return 1

    return factorial(n-1) * n

print("Factorial number {n} equals {f}".format(n=number, f =factorial(number)))

# Factorial number 5 equals 120
